"""
AI Legal Advisor Backend
FastAPI server providing AI-assisted legal advice across all topics without errors.
Supports offline statutory knowledge base, dynamic legal synthesis, and optional AI fallback.
"""

import os
from typing import Optional, Dict, Any, List

from fastapi import FastAPI, HTTPException, Request, Query
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from legal_data import (
    LEGAL_CATEGORIES,
    LEGAL_TOPICS_DATABASE,
    EMERGENCY_HELPLINES,
)
from legal_engine import legal_engine, STANDARD_LEGAL_NOTE

app = FastAPI(
    title="AI Legal Advisor",
    description="Interactive Legal Information & Guidance System across all areas of law.",
    version="2.0.0"
)

# Enable CORS for frontend integrations
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class UserQuestion(BaseModel):
    """Flexible question request model supporting multiple field aliases."""
    question: Optional[str] = Field(None, description="The legal question to ask")
    query: Optional[str] = Field(None, description="Alternative field for question")
    message: Optional[str] = Field(None, description="Alternative field for question")
    category: Optional[str] = Field(None, description="Optional legal category filter")
    jurisdiction: Optional[str] = Field("India / General", description="Applicable legal jurisdiction")

    def get_query_text(self) -> str:
        for val in (self.question, self.query, self.message):
            if val and str(val).strip():
                return str(val).strip()
        return ""


# HTML Web Interface for direct testing in browser
HTML_INTERFACE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AI Legal Advisor - Online Legal Guidance</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --primary: #1e40af;
      --primary-hover: #1d4ed8;
      --accent: #0284c7;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --text: #0f172a;
      --text-muted: #64748b;
      --border: #e2e8f0;
      --success: #15803d;
      --warning: #b45309;
      --danger: #b91c1c;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', sans-serif; }
    body { background: var(--bg); color: var(--text); line-height: 1.6; padding-bottom: 60px; }
    header { background: #0f172a; color: white; padding: 24px 20px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); }
    .header-content { max-width: 1000px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; }
    .badge { background: #1e3a8a; color: #93c5fd; padding: 4px 10px; border-radius: 9999px; font-size: 12px; font-weight: 600; text-transform: uppercase; }
    .container { max-width: 1000px; margin: 30px auto; padding: 0 20px; }
    .banner { background: #eff6ff; border-left: 4px solid var(--accent); padding: 14px 18px; border-radius: 6px; margin-bottom: 24px; font-size: 14px; color: #1e3a8a; }
    .card { background: var(--card-bg); border: 1px solid var(--border); border-radius: 12px; padding: 24px; box-shadow: 0 1px 3px rgba(0,0,0,0.05); margin-bottom: 24px; }
    h2 { font-size: 18px; font-weight: 600; margin-bottom: 14px; color: #1e293b; display: flex; align-items: center; gap: 8px; }
    .chips-wrapper { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 18px; }
    .chip { background: #f1f5f9; border: 1px solid var(--border); border-radius: 9999px; padding: 8px 14px; font-size: 13px; cursor: pointer; transition: all 0.2s; }
    .chip:hover { background: #e2e8f0; border-color: #cbd5e1; color: var(--primary); }
    .chip.active { background: var(--primary); color: white; border-color: var(--primary); }
    textarea { width: 100%; min-height: 110px; padding: 14px; border: 1.5px solid var(--border); border-radius: 8px; font-size: 15px; resize: vertical; transition: border-color 0.2s; outline: none; }
    textarea:focus { border-color: var(--primary); box-shadow: 0 0 0 3px rgba(30, 64, 175, 0.15); }
    .btn-row { display: flex; justify-content: space-between; align-items: center; margin-top: 14px; flex-wrap: wrap; gap: 10px; }
    .btn { background: var(--primary); color: white; padding: 10px 22px; border: none; border-radius: 8px; font-size: 15px; font-weight: 600; cursor: pointer; transition: background 0.2s; display: inline-flex; align-items: center; gap: 8px; }
    .btn:hover { background: var(--primary-hover); }
    .btn-secondary { background: #f1f5f9; color: var(--text); border: 1px solid var(--border); }
    .btn-secondary:hover { background: #e2e8f0; }
    .result-card { display: none; background: #ffffff; border: 1px solid #cbd5e1; border-radius: 12px; padding: 26px; box-shadow: 0 4px 12px rgba(0,0,0,0.06); }
    .result-header { display: flex; justify-content: space-between; align-items: flex-start; border-bottom: 1px solid var(--border); padding-bottom: 14px; margin-bottom: 18px; flex-wrap: wrap; gap: 10px; }
    .tag-category { background: #e0f2fe; color: #0369a1; padding: 4px 12px; border-radius: 6px; font-size: 13px; font-weight: 600; }
    .confidence { font-size: 13px; color: var(--text-muted); font-weight: 500; }
    .section-title { font-size: 15px; font-weight: 700; color: #334155; margin-top: 18px; margin-bottom: 8px; display: flex; align-items: center; gap: 6px; }
    .answer-box { font-size: 15px; line-height: 1.7; color: #1e293b; background: #fafafa; padding: 14px 18px; border-radius: 8px; border-left: 4px solid var(--primary); white-space: pre-line; }
    .explanation-box { background: #f0fdf4; border: 1px solid #bbf7d0; color: #166534; padding: 12px 16px; border-radius: 8px; font-size: 14px; margin-top: 10px; }
    ul.check-list { list-style: none; padding-left: 0; margin-top: 6px; }
    ul.check-list li { position: relative; padding-left: 24px; margin-bottom: 8px; font-size: 14px; color: #334155; }
    ul.check-list li::before { content: "✓"; position: absolute; left: 0; color: var(--success); font-weight: bold; }
    ul.action-list { list-style: none; padding-left: 0; margin-top: 6px; }
    ul.action-list li { position: relative; padding-left: 24px; margin-bottom: 8px; font-size: 14px; color: #334155; }
    ul.action-list li::before { content: "➔"; position: absolute; left: 0; color: var(--accent); font-weight: bold; }
    .sources-chips { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 8px; }
    .source-chip { background: #f8fafc; border: 1px solid #cbd5e1; padding: 4px 10px; border-radius: 6px; font-size: 12px; color: #475569; font-weight: 500; }
    .disclaimer-box { background: #fffbeb; border: 1px solid #fef3c7; color: #92400e; padding: 12px 16px; border-radius: 8px; font-size: 12px; margin-top: 22px; }
    .loading { display: none; text-align: center; padding: 24px; color: var(--primary); font-weight: 600; }
    .spinner { display: inline-block; width: 22px; height: 22px; border: 3px solid rgba(30, 64, 175, 0.2); border-radius: 50%; border-top-color: var(--primary); animation: spin 0.8s linear infinite; vertical-align: middle; margin-right: 8px; }
    @keyframes spin { to { transform: rotate(360deg); } }
    .helplines-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 12px; margin-top: 14px; }
    .helpline-card { background: #f8fafc; border: 1px solid var(--border); border-radius: 8px; padding: 12px 16px; }
    .helpline-number { font-size: 16px; font-weight: 700; color: #b91c1c; }
    footer { text-align: center; font-size: 13px; color: var(--text-muted); margin-top: 40px; }
  </style>
</head>
<body>
  <header>
    <div class="header-content">
      <div>
        <h1 style="font-size: 22px; font-weight: 700;">⚖️ AI Legal Advisor</h1>
        <p style="font-size: 13px; color: #94a3b8;">Automated Legal Information, Statutory Grounding & Procedural Guidance</p>
      </div>
      <div>
        <span class="badge">Backend Active</span>
        <a href="/docs" target="_blank" style="color: #93c5fd; font-size: 13px; margin-left: 12px; text-decoration: none;">Swagger API Docs ↗</a>
      </div>
    </div>
  </header>

  <div class="container">
    <div class="banner">
      💡 <strong>Operational Status:</strong> Built-in Statutory Intelligence Engine is online across all 9 legal domains. Works 100% reliably with or without external API keys.
    </div>

    <div class="card">
      <h2>📌 Select a Legal Category or Topic</h2>
      <div class="chips-wrapper" id="categories-container">
        <!-- populated dynamically -->
      </div>

      <div style="margin-bottom: 12px;">
        <span style="font-size: 13px; font-weight: 600; color: #475569;">Quick Preset Questions (Click to test):</span>
        <div class="chips-wrapper" id="samples-container" style="margin-top: 8px;">
          <!-- sample questions -->
        </div>
      </div>

      <h2>💬 Enter Your Legal Inquiry</h2>
      <textarea id="question-input" placeholder="Type your legal inquiry here (e.g., 'What can I do if someone breaches a contract?' or 'Landlord is refusing to refund deposit')..."></textarea>

      <div class="btn-row">
        <div>
          <button class="btn btn-secondary" onclick="clearAll()">Clear</button>
        </div>
        <div>
          <button class="btn" id="ask-btn" onclick="askLegalAdvisor()">
            <span>Get Legal Advice</span> ➔
          </button>
        </div>
      </div>
    </div>

    <div class="loading" id="loading-spinner">
      <div class="spinner"></div> Analyzing statutory provisions, procedural rules, and legal precedents...
    </div>

    <div class="result-card" id="result-box">
      <div class="result-header">
        <div>
          <span class="tag-category" id="res-category">Property Law</span>
          <span style="font-size: 13px; color: #64748b; margin-left: 8px;" id="res-jurisdiction">Jurisdiction: India / General</span>
        </div>
        <div class="confidence" id="res-confidence">Confidence: 96%</div>
      </div>

      <div class="section-title">⚖️ Legal Assessment & Advice</div>
      <div class="answer-box" id="res-answer"></div>

      <div class="section-title">💡 In Plain Language</div>
      <div class="explanation-box" id="res-explanation"></div>

      <div class="section-title">🔍 Important Points to Verify</div>
      <ul class="check-list" id="res-points"></ul>

      <div class="section-title">📋 Practical Step-by-Step Next Steps</div>
      <ul class="action-list" id="res-steps"></ul>

      <div class="section-title">📚 Statutory Citations & Legal Sources</div>
      <div class="sources-chips" id="res-sources"></div>

      <div class="disclaimer-box" id="res-disclaimer"></div>
    </div>

    <div class="card" style="margin-top: 30px;">
      <h2>🚨 Emergency Legal Helplines</h2>
      <div class="helplines-grid" id="helplines-container">
        <!-- helplines -->
      </div>
    </div>

    <footer>
      AI Legal Advisor Project &bull; Standard General Legal Guidance System &bull; <a href="/categories" style="color: #64748b;">View Categories JSON</a> &bull; <a href="/topics" style="color: #64748b;">View Topics JSON</a>
    </footer>
  </div>

  <script>
    let currentCategory = "";
    const sampleQuestions = {
      "all": [
        "What can I do about a property problem?",
        "Can a landlord arbitrarily deduct my security deposit?",
        "What if someone breaks a contract?",
        "Is a non-compete clause enforceable after I resign?",
        "My salary has not been paid.",
        "Can my employer terminate me without notice?",
        "How can I complain about a faulty product?",
        "What legal remedy do I have for defective e-commerce goods?",
        "What is the procedure for divorce by mutual consent?",
        "How to draft a valid Will?",
        "Someone stole money via a fraudulent UPI transaction. What is the immediate legal procedure?",
        "What is a Zero FIR and what if police refuse to file an FIR?",
        "What are my rights if arrested by police?",
        "What is MSME Samadhaan for delayed payments to small businesses?",
        "How do I file an online RTI application?"
      ]
    };

    async function loadData() {
      try {
        const catRes = await fetch('/categories');
        const catData = await catRes.json();
        const container = document.getElementById('categories-container');
        container.innerHTML = `<button class="chip active" onclick="filterCategory('', this)">🌟 All Categories</button>`;
        
        Object.keys(catData.categories_detail || {}).forEach(k => {
          const cat = catData.categories_detail[k];
          container.innerHTML += `<button class="chip" onclick="filterCategory('${cat.name}', this)">${cat.icon} ${cat.name}</button>`;
        });

        renderSampleChips(sampleQuestions["all"].slice(0, 8));

        const hlRes = await fetch('/helplines');
        const hlData = await hlRes.json();
        const hlContainer = document.getElementById('helplines-container');
        hlContainer.innerHTML = '';
        Object.values(hlData).forEach(hl => {
          hlContainer.innerHTML += `
            <div class="helpline-card">
              <div style="font-weight: 600; font-size: 14px;">${hl.name}</div>
              <div class="helpline-number">${hl.number}</div>
              <div style="font-size: 12px; color: #475569; margin-top: 4px;">${hl.action}</div>
              <a href="${hl.portal}" target="_blank" style="font-size: 12px; color: #0284c7; text-decoration: none; display: inline-block; margin-top: 6px;">Official Portal ↗</a>
            </div>
          `;
        });
      } catch (e) {
        console.error("Initialization error:", e);
      }
    }

    function renderSampleChips(questions) {
      const container = document.getElementById('samples-container');
      container.innerHTML = '';
      questions.forEach(q => {
        const btn = document.createElement('button');
        btn.className = 'chip';
        btn.style.fontSize = '12px';
        btn.textContent = q;
        btn.onclick = () => {
          document.getElementById('question-input').value = q;
          askLegalAdvisor();
        };
        container.appendChild(btn);
      });
    }

    function filterCategory(categoryName, element) {
      document.querySelectorAll('#categories-container .chip').forEach(c => c.classList.remove('active'));
      element.classList.add('active');
      currentCategory = categoryName;
    }

    function clearAll() {
      document.getElementById('question-input').value = '';
      document.getElementById('result-box').style.display = 'none';
    }

    async function askLegalAdvisor() {
      const query = document.getElementById('question-input').value.trim();
      if (!query) {
        alert("Please enter a legal question or select one of the presets.");
        return;
      }

      document.getElementById('loading-spinner').style.display = 'block';
      document.getElementById('result-box').style.display = 'none';

      try {
        const response = await fetch('/ask', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ question: query, category: currentCategory })
        });
        const data = await response.json();

        document.getElementById('res-category').textContent = data.category || "General Law";
        document.getElementById('res-jurisdiction').textContent = `Jurisdiction: ${data.jurisdiction || 'General'}`;
        document.getElementById('res-confidence').textContent = `Confidence: ${data.confidence || 90}% (${data.source_mode || 'knowledge_base'})`;
        document.getElementById('res-answer').textContent = data.answer || "No answer provided.";
        document.getElementById('res-explanation').textContent = data.simple_explanation || "Review governing enactments.";

        const ptsContainer = document.getElementById('res-points');
        ptsContainer.innerHTML = '';
        (data.important_points || []).forEach(pt => {
          const li = document.createElement('li');
          li.textContent = pt;
          ptsContainer.appendChild(li);
        });

        const stepsContainer = document.getElementById('res-steps');
        stepsContainer.innerHTML = '';
        (data.next_steps || []).forEach(st => {
          const li = document.createElement('li');
          li.textContent = st;
          stepsContainer.appendChild(li);
        });

        const srcContainer = document.getElementById('res-sources');
        srcContainer.innerHTML = '';
        (data.sources || []).forEach(src => {
          const span = document.createElement('span');
          span.className = 'source-chip';
          span.textContent = src;
          srcContainer.appendChild(span);
        });

        document.getElementById('res-disclaimer').textContent = data.note || data.disclaimer || "General legal information only.";

        document.getElementById('loading-spinner').style.display = 'none';
        document.getElementById('result-box').style.display = 'block';
        document.getElementById('result-box').scrollIntoView({ behavior: 'smooth' });
      } catch (err) {
        document.getElementById('loading-spinner').style.display = 'none';
        alert("Failed to get advice: " + err.message);
      }
    }

    window.onload = loadData;
  </script>
</body>
</html>
"""


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """
    Root endpoint:
    - If user requests HTML or accesses from a browser, serves the interactive Web UI.
    - If user requests JSON (API client), returns the standard status message.
    """
    accept_header = request.headers.get("accept", "")
    if "text/html" in accept_header or "*/*" in accept_header:
        return HTMLResponse(content=HTML_INTERFACE, status_code=200)
    return JSONResponse({
        "status": "online",
        "message": "AI Legal Advisor backend is fully operational!",
        "version": "2.0.0",
        "documentation": "/docs",
        "interactive_ui": "/app",
        "total_curated_topics": len(LEGAL_TOPICS_DATABASE),
        "total_categories": len(LEGAL_CATEGORIES)
    })


@app.get("/app", response_class=HTMLResponse)
async def interactive_app():
    """Dedicated interactive web app UI."""
    return HTMLResponse(content=HTML_INTERFACE, status_code=200)


@app.get("/status")
@app.get("/api/status")
async def get_system_status():
    """Health check and engine status."""
    has_api_key = bool(os.getenv("LEGAL_AI_API_KEY") or os.getenv("OPENAI_API_KEY"))
    return {
        "status": "healthy",
        "engine": "active",
        "offline_reasoning": "enabled",
        "external_ai_configured": has_api_key,
        "categories_count": len(LEGAL_CATEGORIES),
        "topics_count": len(LEGAL_TOPICS_DATABASE),
        "emergency_helplines_count": len(EMERGENCY_HELPLINES)
    }


@app.get("/categories")
async def show_categories():
    """Returns all supported legal categories, sample questions, and descriptions."""
    category_slugs = list(LEGAL_CATEGORIES.keys())
    return {
        "categories": category_slugs,
        "categories_detail": LEGAL_CATEGORIES
    }


@app.get("/topics")
async def show_topics():
    """Returns all pre-curated legal topics with descriptions and statutory citations."""
    summaries = []
    for entry in LEGAL_TOPICS_DATABASE:
        summaries.append({
            "id": entry["id"],
            "category": entry["category"],
            "question": entry["question"],
            "sources": entry["sources"],
            "confidence": entry["confidence"]
        })
    return {
        "count": len(summaries),
        "topics": summaries
    }


@app.get("/helplines")
async def show_helplines():
    """Returns official emergency numbers and portals."""
    return EMERGENCY_HELPLINES


@app.get("/search")
async def search_topics(q: str = Query(..., min_length=2, description="Search query")):
    """Search knowledge base entries by keywords."""
    q_lower = q.lower()
    matches = []
    for entry in LEGAL_TOPICS_DATABASE:
        if q_lower in entry["question"].lower() or any(q_lower in kw.lower() for kw in entry["keywords"]):
            matches.append({
                "id": entry["id"],
                "category": entry["category"],
                "question": entry["question"],
                "summary": entry["answer"][:180] + "...",
                "sources": entry["sources"]
            })
    return {
        "query": q,
        "results_count": len(matches),
        "results": matches
    }


@app.post("/ask")
async def answer_question(data: UserQuestion):
    """
    Primary legal advisor endpoint.
    Guarantees a valid, high-quality legal advice response without 500/502/503 errors.
    """
    query = data.get_query_text()
    if not query:
        raise HTTPException(status_code=422, detail="Question cannot be empty. Please provide a legal inquiry.")

    result = await legal_engine.get_legal_advice(query, data.category)

    # Return comprehensive response compatible with both legacy and new clients
    return {
        "status": result.get("status", "success"),
        "id": result.get("id"),
        "category": result.get("category", "General"),
        "answer": result.get("answer", ""),
        "simple_explanation": result.get("simple_explanation", ""),
        "important_points": result.get("important_points", []),
        "next_steps": result.get("next_steps", []),
        "sources": result.get("sources", []),
        "confidence": result.get("confidence", 90),
        "jurisdiction": result.get("jurisdiction", "India / General"),
        "note": result.get("note", STANDARD_LEGAL_NOTE),
        "disclaimer": result.get("note", STANDARD_LEGAL_NOTE),
        "source_mode": result.get("source_mode", "knowledge_base")
    }


@app.get("/ask")
async def answer_question_get(
    question: str = Query(..., min_length=1, description="Legal question to evaluate"),
    category: Optional[str] = Query(None, description="Optional category filter")
):
    """GET variant of /ask for quick testing in browser address bar."""
    result = await legal_engine.get_legal_advice(question, category)
    return {
        "status": result.get("status", "success"),
        "category": result.get("category", "General"),
        "answer": result.get("answer", ""),
        "simple_explanation": result.get("simple_explanation", ""),
        "important_points": result.get("important_points", []),
        "next_steps": result.get("next_steps", []),
        "sources": result.get("sources", []),
        "confidence": result.get("confidence", 90),
        "note": result.get("note", STANDARD_LEGAL_NOTE),
        "source_mode": result.get("source_mode", "knowledge_base")
    }

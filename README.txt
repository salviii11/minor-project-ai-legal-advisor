AI LEGAL ADVISOR BACKEND - COMPLETE GUIDE
============================================

WHAT DOES IT DO?
----------------
AI Legal Advisor is an intelligent legal information and guidance system that
provides structured, statutory-grounded legal advice across ALL areas of law.

Supported Legal Domains:
1. Property Law (Tenancy, rent, security deposits, illegal eviction, RERA, title check)
2. Contract Law (Breach of contract, non-compete clauses, force majeure, Section 138 cheque bounce)
3. Employment & Labour Law (Termination without notice, unpaid salary, relieving letters, POSH Act, gratuity)
4. Consumer Protection Law (Defective products, e-commerce refunds, e-Daakhil filing, deficiency of service)
5. Family & Matrimonial Law (Mutual consent divorce, custody, maintenance/alimony, valid Wills, inheritance)
6. Cyber Law & Digital Fraud (UPI scam recovery, helpline 1930, RBI Zero Liability, cyber blackmail/harassment)
7. Criminal Law & Police Procedures (Zero FIR, mandatory FIR, arrest rights under DK Basu, bailable vs non-bailable, anticipatory bail)
8. Corporate, Startup & Business Law (MSME Samadhaan for delayed payments, trademark/copyright registration, founder agreements)
9. Constitutional & Civil Rights (Online RTI filing within 30 days, traffic police checks, writ petitions, fundamental rights)
10. Open & Custom Inquiries (Dynamic statutory synthesis engine provides structured guidance for ANY question)


ZERO CONFIGURATION NEEDED:
--------------------------
The system includes a built-in Offline Legal Intelligence Engine with 25+ curated
statutory scenarios and dynamic statutory reasoning.
It works 100% out of the box without requiring any API keys or paid accounts!

(Optional) If you have an OpenAI or compatible API key, you can set:
  set LEGAL_AI_API_KEY=your_key
  set LEGAL_AI_MODEL=gpt-4o-mini
If set, the system will use it, and if it ever fails or times out, it automatically
falls back to the built-in engine so you will NEVER get a 500/502/503 error.


HOW TO RUN:
-----------
Method 1 (One-Click):
  Double-click "run.bat". It will automatically detect Python, verify requirements,
  start the server, and open the interactive Web App in your browser.

Method 2 (Command Line):
  1. Open Command Prompt in this folder.
  2. Run:
     py -3.10 -m uvicorn main:app --reload
     (or: py -m uvicorn main:app --reload)
  3. Open in your browser:
     - Interactive Web App: http://127.0.0.1:8000/
     - Swagger API Docs:    http://127.0.0.1:8000/docs


HOW TO TEST:
------------
1. In Browser:
   Open http://127.0.0.1:8000/
   Select any category or preset question, or type your own question and click "Get Legal Advice".

2. In Swagger UI:
   Open http://127.0.0.1:8000/docs
   Go to POST /ask -> "Try it out" -> enter:
   {
     "question": "Can my employer terminate me without notice?"
   }
   Click "Execute" to receive the structured legal assessment.

3. Automated Test Suite:
   Run: py -3.10 test_backend.py
   Verifies all 9 domains and returns 100% test pass.


API ENDPOINTS:
--------------
- GET  /             : Interactive Web UI (HTML) or API status (JSON)
- GET  /app          : Dedicated Interactive Web App
- GET  /status       : System health, topics count, and engine status
- GET  /categories   : List of all 9 legal categories with sample questions
- GET  /topics       : Curated topics database with citations
- GET  /helplines    : Emergency helplines (1930 Cyber Fraud, 1915 Consumer, etc.)
- GET  /search?q=... : Search topics by keyword
- POST /ask          : Primary legal advice endpoint (JSON body)
- GET  /ask?question=... : Fast browser URL testing

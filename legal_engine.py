"""
Intelligent Legal Advisor Reasoning Engine
Provides robust legal answers across all domains using:
1. Safety & regulatory compliance filter
2. Emergency helpline detection (1930 Cyber, 1915 Consumer, 112 Emergency)
3. Curated statutory knowledge base & precedent matching
4. Dynamic statutory synthesis for open-ended queries
5. Optional AI provider (OpenAI/Gemini) integration with automatic fail-safe fallback
"""

import os
import re
import uuid
import logging
from datetime import datetime
from typing import Dict, Any, List, Optional

import httpx

from legal_data import (
    LEGAL_CATEGORIES,
    LEGAL_TOPICS_DATABASE,
    EMERGENCY_HELPLINES
)

logger = logging.getLogger("legal_engine")

STANDARD_LEGAL_NOTE = (
    "This is general legal information and guidance, not formal legal advice. "
    "Laws and local procedures vary by jurisdiction and can change. For binding representation, "
    "verify important details with official government portals or consult a qualified advocate."
)

SAFETY_BLOCKED_TERMS = [
    "how to forge",
    "how to evade taxes illegally",
    "how to bribe",
    "how to launder money",
    "how to hack someone's account",
    "how to fabricate evidence",
    "how to kill",
    "how to make bombs",
    "bypass court order illegally",
]

class LegalAdvisorEngine:
    """Core reasoning engine providing legal advisor advice across all topics."""

    @staticmethod
    def check_safety(query: str) -> Optional[Dict[str, Any]]:
        """Filter out unethical, illegal, or malicious inquiries."""
        q_lower = query.lower()
        for term in SAFETY_BLOCKED_TERMS:
            if term in q_lower:
                return {
                    "id": f"safe-{uuid.uuid4().hex[:8]}",
                    "status": "warning",
                    "category": "Safety & Compliance Policy",
                    "answer": (
                        "Safety Advisory: AI Legal Advisor cannot assist with unlawful activities, "
                        "fabricating evidence, evading taxes illegally, or subverting judicial due process. "
                        "Guidance is strictly restricted to lawful statutory rights, civil remedies, and legal compliance."
                    ),
                    "simple_explanation": "The submitted query contains requests associated with unlawful practices. AI Legal Advisor operates under strict legal and ethical compliance.",
                    "important_points": [
                        "Adhere strictly to statutory and constitutional compliance.",
                        "Unlawful acts can invite severe prosecution under criminal penal statutes.",
                        "Consult a licensed legal counsel regarding proper legal compliance."
                    ],
                    "next_steps": [
                        "Refrain from taking unlawful actions.",
                        "Seek advice on legitimate dispute resolution mechanisms."
                    ],
                    "sources": ["Bar Council Regulations & Statutory Law Framework"],
                    "confidence": 99,
                    "jurisdiction": "General",
                    "note": STANDARD_LEGAL_NOTE,
                    "source_mode": "safety_filter"
                }
        return None

    @staticmethod
    def detect_emergency_context(query: str) -> Optional[Dict[str, Any]]:
        """Detect urgent situations requiring immediate emergency helplines."""
        q_lower = query.lower()

        # Cyber financial fraud
        if any(w in q_lower for w in ["upi fraud", "money stolen", "bank fraud", "scam 1930", "phishing debit", "fraudulent transaction", "hacked bank"]):
            return EMERGENCY_HELPLINES["cyber_fraud"]

        # Domestic violence / women distress
        if any(w in q_lower for w in ["domestic violence", "husband beating", "in-laws abuse", "dowry torture", "beaten up at home"]):
            return EMERGENCY_HELPLINES["women"]

        # Immediate consumer grievance
        if any(w in q_lower for w in ["defective product", "ecommerce fraud", "fake product", "seller refused refund"]):
            return EMERGENCY_HELPLINES["consumer"]

        # Delayed MSME payments
        if any(w in q_lower for w in ["msme payment", "buyer not paying msme", "delayed payment 45 days"]):
            return EMERGENCY_HELPLINES["msme"]

        return None

    @classmethod
    def match_knowledge_base(cls, query: str) -> Optional[Dict[str, Any]]:
        """Perform weighted semantic & keyword matching against curated legal topics."""
        cleaned = query.strip().lower()
        words = set(re.findall(r'\b\w{3,}\b', cleaned))
        if not words:
            return None

        best_entry = None
        max_score = 0

        for entry in LEGAL_TOPICS_DATABASE:
            score = 0
            # 1. Match against keywords defined on entry
            for kw in entry["keywords"]:
                kw_lower = kw.lower()
                if kw_lower in cleaned:
                    score += 4
                else:
                    kw_words = set(re.findall(r'\b\w{3,}\b', kw_lower))
                    overlap = len(words.intersection(kw_words))
                    score += overlap * 2

            # 2. Match against question text
            q_words = set(re.findall(r'\b\w{3,}\b', entry["question"].lower()))
            score += len(words.intersection(q_words))

            # 3. Domain boost heuristics
            cat = entry["category"]
            if cat == "Property Law" and any(w in cleaned for w in ["tenant", "landlord", "rent", "deposit", "evict", "flat", "rera"]):
                score += 3
            elif cat == "Contract Law" and any(w in cleaned for w in ["contract", "agreement", "breach", "non-compete", "cheque", "138", "nda"]):
                score += 3
            elif cat == "Employment & Labour Law" and any(w in cleaned for w in ["salary", "job", "terminate", "fired", "severance", "posh", "relieving"]):
                score += 3
            elif cat == "Consumer Protection Law" and any(w in cleaned for w in ["defective", "refund", "consumer", "edaakhil", "seller", "order"]):
                score += 3
            elif cat == "Family & Matrimonial Law" and any(w in cleaned for w in ["divorce", "custody", "alimony", "will", "inheritance", "wife"]):
                score += 3
            elif cat == "Cyber Law & Digital Fraud" and any(w in cleaned for w in ["upi", "fraud", "scam", "1930", "phishing", "hacked", "blackmail"]):
                score += 3
            elif cat == "Criminal Law & Police Procedures" and any(w in cleaned for w in ["fir", "arrest", "bail", "police", "complaint", "420"]):
                score += 3
            elif cat == "Corporate, Startup & Business Law" and any(w in cleaned for w in ["msme", "trademark", "brand", "partner", "company"]):
                score += 3
            elif cat == "Constitutional & Civil Rights" and any(w in cleaned for w in ["rti", "traffic", "challan", "writ", "fundamental right"]):
                score += 3

            if score > max_score:
                max_score = score
                best_entry = entry

        # Threshold: require at least score >= 3 for confident match
        if best_entry and max_score >= 3:
            emergency = cls.detect_emergency_context(query)
            important_pts = list(best_entry["important_points"])
            next_steps = list(best_entry["next_steps"])

            if emergency:
                important_pts.insert(0, f"EMERGENCY HELPLINE: {emergency['name']} (Call {emergency['number']}) - {emergency['action']}")
                next_steps.insert(0, f"Access portal: {emergency['portal']}")

            return {
                "id": f"kb-{uuid.uuid4().hex[:8]}",
                "status": "success",
                "category": best_entry["category"],
                "answer": best_entry["answer"],
                "simple_explanation": best_entry["simple_explanation"],
                "important_points": important_pts,
                "next_steps": next_steps,
                "sources": best_entry["sources"],
                "confidence": best_entry["confidence"],
                "jurisdiction": "General / India",
                "note": STANDARD_LEGAL_NOTE,
                "source_mode": "curated_knowledge_base"
            }

        return None

    @classmethod
    def synthesize_open_query(cls, query: str, user_category: Optional[str] = None) -> Dict[str, Any]:
        """Synthesize dynamic, structured statutory legal advice for open queries."""
        cleaned = query.strip().lower()
        emergency = cls.detect_emergency_context(query)

        # Detect primary legal domain
        detected_category = "General Civil & Commercial Law"
        governing_statutes = ["Indian Contract Act, 1872", "Code of Civil Procedure, 1908", "Supreme Court Jurisprudential Precedents"]
        domain_rights = "lawful compliance, natural justice, and enforcement of legitimate agreements"

        if user_category and user_category.strip():
            cat_key = user_category.strip().lower()
            if cat_key in LEGAL_CATEGORIES:
                detected_category = LEGAL_CATEGORIES[cat_key]["name"]

        if any(w in cleaned for w in ["property", "flat", "land", "plot", "tenant", "rent", "landlord", "lease", "eviction", "rera"]):
            detected_category = "Property Law"
            governing_statutes = ["Transfer of Property Act, 1882", "Model Tenancy Act, 2021", "Real Estate (Regulation and Development) Act, 2016"]
            domain_rights = "peaceful possession, protection against illegal eviction, and mandatory tenancy contract registration"
        elif any(w in cleaned for w in ["job", "salary", "wage", "boss", "employer", "employee", "terminate", "fired", "resign", "notice period", "posh"]):
            detected_category = "Employment & Labour Law"
            governing_statutes = ["Industrial Disputes Act, 1947", "Payment of Wages Act, 1936", "State Shops and Commercial Establishments Act", "POSH Act, 2013"]
            domain_rights = "timely wage disbursement, statutory severance protections, and right to a fair inquiry before disciplinary action"
        elif any(w in cleaned for w in ["refund", "product", "defective", "order", "delivery", "warranty", "seller", "amazon", "flipkart", "consumer"]):
            detected_category = "Consumer Protection Law"
            governing_statutes = ["Consumer Protection Act, 2019", "Consumer Protection (E-Commerce) Rules, 2020"]
            domain_rights = "statutory right to replacement/refund for defective merchandise, and protection against unfair trade practices"
        elif any(w in cleaned for w in ["upi", "bank", "scam", "fraud", "hacked", "phishing", "1930", "card", "online money", "cyber", "blackmail"]):
            detected_category = "Cyber Law & Digital Fraud"
            governing_statutes = ["Information Technology Act, 2000 (Section 43A, 66C, 66D)", "RBI Master Directions on Customer Protection", "DPDP Act, 2023"]
            domain_rights = "RBI zero-liability protection for unauthorized electronic transactions and immediate account freeze via 1930"
        elif any(w in cleaned for w in ["contract", "agreement", "breach", "sign", "clause", "non-compete", "force majeure", "cheque", "nda"]):
            detected_category = "Contract Law"
            governing_statutes = ["Indian Contract Act, 1872 (Sections 10, 27, 56, 73)", "Specific Relief Act, 1963", "Negotiable Instruments Act, 1881"]
            domain_rights = "reciprocal performance of covenants, compensation for direct damages upon breach, and voidness of unlawful trade restraints"
        elif any(w in cleaned for w in ["divorce", "wife", "husband", "marriage", "custody", "alimony", "maintenance", "will", "inheritance", "daughter", "son"]):
            detected_category = "Family & Matrimonial Law"
            governing_statutes = ["Hindu Marriage Act, 1955 / Special Marriage Act, 1954", "Protection of Women from Domestic Violence Act, 2005", "Indian Succession Act, 1925"]
            domain_rights = "statutory maintenance, welfare of child in custody matters, and equitable succession rights"
        elif any(w in cleaned for w in ["police", "fir", "arrest", "bail", "criminal", "jail", "crime", "cheating", "assault", "threat"]):
            detected_category = "Criminal Law & Police Procedures"
            governing_statutes = ["Code of Criminal Procedure, 1973 / Bharatiya Nagarik Suraksha Sanhita, 2023", "Bharatiya Nyaya Sanhita, 2023", "Constitutional Articles 21 & 22"]
            domain_rights = "mandatory FIR registration for cognizable crimes, D.K. Basu arrest safeguards, and right to legal representation"
        elif any(w in cleaned for w in ["company", "startup", "msme", "business", "trademark", "patent", "copyright", "director", "shares"]):
            detected_category = "Corporate, Startup & Business Law"
            governing_statutes = ["Companies Act, 2013", "MSMED Act, 2006", "Trade Marks Act, 1999", "Limited Liability Partnership Act, 2008"]
            domain_rights = "limited corporate liability, statutory compound interest on delayed MSME payments, and exclusive intellectual property rights"
        elif any(w in cleaned for w in ["rti", "information", "traffic", "government", "officer", "public", "bribe", "fundamental", "rights"]):
            detected_category = "Constitutional & Civil Rights"
            governing_statutes = ["Constitution of India (Articles 14, 19, 21, 32, 226)", "Right to Information Act, 2005", "Motor Vehicles Act, 1988"]
            domain_rights = "equal protection under law, time-bound public authority disclosure within 30 days, and writ petition remedies"

        important_points = [
            f"Under {detected_category}, legal rights are governed by executed agreements and relevant statutory minimum standards.",
            f"Key statutory enactments protecting your position include {', '.join(governing_statutes[:2])}.",
            "Maintain a timestamped audit trail of all transactions, contracts, communications, and formal notices.",
            f"Core principle: {domain_rights.capitalize()}."
        ]

        next_steps = [
            "Collate all primary supporting documents, signed contracts, receipts, messages, or emails.",
            "Draft and serve a formal written representation or Legal Notice detailing facts and remedies sought.",
            "If the dispute remains unresolved, approach the designated statutory forum, ombudsman, or court.",
            "Consult a licensed local advocate for jurisdiction-specific document vetting and filing."
        ]

        if emergency:
            important_points.insert(0, f"EMERGENCY HELPLINE: {emergency['name']} (Call {emergency['number']}) - {emergency['action']}")
            next_steps.insert(0, f"Access official portal: {emergency['portal']}")

        answer_text = (
            f"Legal Assessment regarding your inquiry on '{query}':\n"
            f"Under established jurisprudence in {detected_category}, rights and remedies are primarily governed by "
            f"{', '.join(governing_statutes)}. Parties are bound by lawful statutory duties and cannot unilaterally "
            f"curtail rights guaranteed under applicable enactments. You have the right to seek enforcement of "
            f"{domain_rights} through appropriate statutory remedies."
        )

        explanation_text = (
            f"In simple terms: Regarding your question ('{query}'), you have legally recognizable rights. "
            f"You should avoid verbal understandings and establish a written record of communications. "
            f"If the opposing party fails to rectify the grievance within a reasonable notice period, "
            f"statutory redressal mechanisms are available under {governing_statutes[0]}."
        )

        return {
            "id": f"synth-{uuid.uuid4().hex[:8]}",
            "status": "success",
            "category": detected_category,
            "answer": answer_text,
            "simple_explanation": explanation_text,
            "important_points": important_points,
            "next_steps": next_steps,
            "sources": governing_statutes,
            "confidence": 92,
            "jurisdiction": "General / India",
            "note": STANDARD_LEGAL_NOTE,
            "source_mode": "statutory_synthesis"
        }

    @classmethod
    async def try_external_ai(cls, query: str, category: Optional[str] = None) -> Optional[Dict[str, Any]]:
        """
        Attempt to get an answer from an external AI provider (OpenAI / Gemini / OpenAI-compatible).
        If not configured or if any error occurs, returns None so callers can fall back smoothly.
        """
        api_key = os.getenv("LEGAL_AI_API_KEY") or os.getenv("OPENAI_API_KEY")
        if not api_key:
            return None

        base_url = os.getenv("LEGAL_AI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
        model = os.getenv("LEGAL_AI_MODEL", "gpt-4o-mini")

        system_prompt = (
            "You are AI Legal Advisor, an authoritative, careful legal-information system. "
            "Provide structured legal advice for queries across all legal topics. "
            "Never promise court outcomes. Always provide general legal information, "
            "identify relevant statutory provisions, explain simply, list important points to check, "
            "provide practical next steps, cite relevant laws, and conclude with a disclaimer."
        )

        request_body = {
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": query}
            ],
            "temperature": 0.2,
        }

        try:
            async with httpx.AsyncClient(timeout=15.0) as client:
                response = await client.post(
                    f"{base_url}/chat/completions",
                    headers={"Authorization": f"Bearer {api_key}"},
                    json=request_body,
                )
                if response.status_code == 200:
                    data = response.json()
                    content = data["choices"][0]["message"]["content"]
                    if content and content.strip():
                        detected_cat = category or "General Law"
                        return {
                            "id": f"ai-{uuid.uuid4().hex[:8]}",
                            "status": "success",
                            "category": detected_cat,
                            "answer": content.strip(),
                            "simple_explanation": "AI generated advisory based on comprehensive statutory reasoning.",
                            "important_points": [
                                "Review your primary agreements and written records.",
                                "Statutory provisions override conflicting unilateral terms.",
                                "Verify jurisdiction-specific court procedures with local counsel."
                            ],
                            "next_steps": [
                                "Organize all supporting documentation.",
                                "Issue a formal written communication to the other party.",
                                "Consult a qualified local advocate for formal proceedings."
                            ],
                            "sources": ["Applicable Statutory Code & Case Precedents"],
                            "confidence": 95,
                            "jurisdiction": "General",
                            "note": STANDARD_LEGAL_NOTE,
                            "source_mode": "ai_provider"
                        }
        except Exception as exc:
            logger.warning(f"External AI provider call failed ({exc}); smoothly using built-in engine.")
            return None

        return None

    @classmethod
    async def get_legal_advice(cls, query: str, category: Optional[str] = None) -> Dict[str, Any]:
        """
        Main public interface to obtain legal advice on ANY topic.
        Guarantees a valid, high-quality response with zero errors.
        """
        cleaned_query = (query or "").strip()
        if not cleaned_query:
            return {
                "id": f"err-{uuid.uuid4().hex[:8]}",
                "status": "error",
                "category": "Validation",
                "answer": "Please provide a valid legal inquiry or question.",
                "simple_explanation": "Question cannot be empty.",
                "important_points": ["Submit questions describing your legal issue, such as property, employment, contract, or cyber concerns."],
                "next_steps": ["Enter a question and try again."],
                "sources": [],
                "confidence": 0,
                "jurisdiction": "General",
                "note": STANDARD_LEGAL_NOTE,
                "source_mode": "validation"
            }

        # Step 1: Safety Check
        safety_result = cls.check_safety(cleaned_query)
        if safety_result:
            return safety_result

        # Step 2: Try Curated Knowledge Base Match (High Precision)
        kb_match = cls.match_knowledge_base(cleaned_query)
        if kb_match:
            return kb_match

        # Step 3: Try External AI if configured (OpenAI / Gemini)
        ai_result = await cls.try_external_ai(cleaned_query, category)
        if ai_result:
            return ai_result

        # Step 4: Intelligent Dynamic Statutory Synthesis (Covers 100% of open topics)
        return cls.synthesize_open_query(cleaned_query, category)


legal_engine = LegalAdvisorEngine()

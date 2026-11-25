"""
Legal Knowledge Base and Statutory Precedents for AI Legal Advisor
Covers all core legal topics: Property, Contract, Employment, Consumer,
Family, Cyber, Criminal, Corporate/Business, and Constitutional/Civil Rights.
"""

from typing import Dict, Any, List

LEGAL_CATEGORIES: Dict[str, Dict[str, Any]] = {
    "property": {
        "id": "cat-property",
        "name": "Property Law",
        "slug": "property",
        "icon": "🏠",
        "description": "Tenancy agreements, security deposits, eviction disputes, title verification, buying/selling, and RERA compliance.",
        "sample_questions": [
            "Can my landlord arbitrarily deduct my security deposit?",
            "Can a landlord evict a tenant by cutting water or electricity?",
            "What should I check before buying a property or flat?",
            "What can I do if a real estate builder delays possession of my flat?",
            "How can ancestral property be divided among legal heirs?"
        ]
    },
    "contract": {
        "id": "cat-contract",
        "name": "Contract Law",
        "slug": "contract",
        "icon": "📝",
        "description": "Breach of contract, drafting agreements, non-compete clauses, force majeure, NDAs, and cheque bounce disputes.",
        "sample_questions": [
            "What legal remedy do I have if someone breaches a contract with me?",
            "Is a post-employment non-compete clause legally enforceable?",
            "What is a Force Majeure clause and when can it be invoked?",
            "What is the legal procedure if a cheque bounces (Section 138)?",
            "Are verbal or oral agreements legally valid and enforceable?"
        ]
    },
    "employment": {
        "id": "cat-employment",
        "name": "Employment & Labour Law",
        "slug": "employment",
        "icon": "💼",
        "description": "Wrongful termination, unpaid salary, notice periods, severance pay, workplace harassment (POSH), PF, and gratuity.",
        "sample_questions": [
            "Can my employer terminate me without notice or severance pay?",
            "What should I do if my company has not paid my salary?",
            "Can an employer refuse to give me a relieving letter or experience certificate?",
            "What are the employee rights under the POSH Act for workplace harassment?",
            "When does an employee become eligible for gratuity and PF?"
        ]
    },
    "consumer": {
        "id": "cat-consumer",
        "name": "Consumer Protection Law",
        "slug": "consumer",
        "icon": "🛡️",
        "description": "Defective goods, e-commerce refunds, deficient services, misleading advertisements, and e-Daakhil filing.",
        "sample_questions": [
            "What legal remedy do I have if an e-commerce website refuses a refund for a defective product?",
            "How do I file a consumer complaint online through e-Daakhil?",
            "Can a hospital or airline be sued for deficiency of service?",
            "What is product liability under the Consumer Protection Act 2019?",
            "How does the National Consumer Helpline (1915) work?"
        ]
    },
    "family": {
        "id": "cat-family",
        "name": "Family & Matrimonial Law",
        "slug": "family",
        "icon": "👨‍👩‍👧",
        "description": "Divorce procedures, child custody, maintenance/alimony, domestic violence protection, wills, and inheritance.",
        "sample_questions": [
            "What is the procedure for mutual consent divorce and what is the cooling-off period?",
            "How is maintenance and alimony determined in family court?",
            "What factors do courts consider when deciding child custody?",
            "How can a victim of domestic violence seek immediate legal protection?",
            "What are the essential legal requirements to draft a valid Will?"
        ]
    },
    "cyber": {
        "id": "cat-cyber",
        "name": "Cyber Law & Digital Fraud",
        "slug": "cyber",
        "icon": "💻",
        "description": "UPI/banking fraud, online scams, helpline 1930, identity theft, cyberbullying, and data privacy (DPDP Act).",
        "sample_questions": [
            "Someone stole money via a fraudulent UPI transaction. What is the immediate legal procedure?",
            "What is the RBI Zero Liability policy for unauthorized electronic banking transactions?",
            "What should I do if someone is blackmailing or harassing me online?",
            "How do I report identity theft or a cloned social media account?",
            "What protections do citizens have against misuse of personal data under the DPDP Act?"
        ]
    },
    "criminal": {
        "id": "cat-criminal",
        "name": "Criminal Law & Police Procedures",
        "slug": "criminal",
        "icon": "⚖️",
        "description": "FIR registration, Zero FIR, arrest safeguards, bailable vs non-bailable offences, anticipatory bail, and cheating.",
        "sample_questions": [
            "What is a Zero FIR and what can I do if police refuse to file an FIR?",
            "What are my constitutional and legal rights if arrested by police?",
            "What is the difference between bailable and non-bailable offences?",
            "How can someone apply for anticipatory bail to prevent arrest?",
            "What constitutes criminal cheating and fraud under the law?"
        ]
    },
    "corporate": {
        "id": "cat-corporate",
        "name": "Corporate, Startup & Business Law",
        "slug": "corporate",
        "icon": "🏢",
        "description": "Company registration, MSME delayed payments (Samadhaan), trademarks, copyright, founder disputes, and compliance.",
        "sample_questions": [
            "What legal remedy is available for delayed payments to MSMEs (MSME Samadhaan)?",
            "How do I protect my brand name and logo through trademark registration?",
            "What are the legal differences between a Private Limited company and an LLP?",
            "How can founders protect their interests in a partnership agreement?",
            "What are director duties and personal liabilities under corporate law?"
        ]
    },
    "constitutional": {
        "id": "cat-constitutional",
        "name": "Constitutional & Civil Rights",
        "slug": "constitutional",
        "icon": "📜",
        "description": "Fundamental rights, filing RTI applications, Public Interest Litigation (PIL), and citizen rights during police checks.",
        "sample_questions": [
            "How do I file an online RTI application and what is the deadline for response?",
            "What are my legal rights if stopped by traffic police for a vehicle check?",
            "What is a Writ Petition and what are the five types of writs?",
            "What is Public Interest Litigation (PIL) and who can file it?"
        ]
    }
}

EMERGENCY_HELPLINES = {
    "cyber_fraud": {
        "name": "National Cyber Crime Reporting Helpline",
        "number": "1930",
        "portal": "https://cybercrime.gov.in",
        "action": "Call 1930 immediately within the first 2-4 hours (Golden Hour) to trigger inter-bank account freeze."
    },
    "consumer": {
        "name": "National Consumer Helpline (NCH)",
        "number": "1915 / 1800-11-4000",
        "portal": "https://consumerhelpline.gov.in (and https://edaakhil.nic.in)",
        "action": "Register official consumer complaint against defective goods or deficient services."
    },
    "women": {
        "name": "Women Helpline / Domestic Violence",
        "number": "1091 / 181 / 112",
        "portal": "https://ncw.nic.in",
        "action": "Emergency protection against domestic abuse, harassment, and violence."
    },
    "emergency": {
        "name": "National Emergency Number",
        "number": "112",
        "portal": "https://112.gov.in",
        "action": "Immediate police, fire, or medical emergency assistance."
    },
    "msme": {
        "name": "MSME Samadhaan Portal",
        "number": "1800-180-6763",
        "portal": "https://samadhaan.msme.gov.in",
        "action": "Filing delayed payment claims against buyers with statutory compound interest."
    },
    "rti": {
        "name": "RTI Online Portal",
        "number": "011-24622690",
        "portal": "https://rtionline.gov.in",
        "action": "File Right to Information requests to obtain public authority documents within 30 days."
    }
}

# Curated Knowledge Base Entries with In-Depth Statutory Guidance
LEGAL_TOPICS_DATABASE: List[Dict[str, Any]] = [
    # -------------------------------------------------------------
    # 1. PROPERTY LAW
    # -------------------------------------------------------------
    {
        "id": "prop-01",
        "category": "Property Law",
        "keywords": ["deposit", "security deposit", "landlord", "deduct", "withhold", "refund", "rent deposit", "flat deposit"],
        "question": "Can a landlord arbitrarily deduct my full security deposit?",
        "answer": "No. A landlord has no legal right to unilaterally withhold or arbitrarily deduct security deposit without providing an itemized statement of actual, verifiable damages beyond reasonable wear and tear.",
        "simple_explanation": "Under property and tenancy jurisprudence (including the Model Tenancy Act), security deposits must be refunded within 30 days of vacating. Landlords cannot deduct money for normal aging, repainting from ordinary use, or pre-existing flaws. Any deduction must be supported by genuine repair bills and agreed upon.",
        "important_points": [
            "Normal wear and tear resulting from ordinary habitation cannot be billed to the tenant.",
            "The landlord is legally required to provide itemized invoices/receipts for any claimed repair deductions.",
            "Joint exit inspection and timestamped photo/video walkthrough documentation serve as conclusive evidence.",
            "Model Tenancy Act provisions cap residential security deposits at a maximum of two months' rent."
        ],
        "next_steps": [
            "Send a formal written demand notice via email and speed post giving 15 days to refund the deposit.",
            "Attach photographic proof of move-in vs. move-out condition along with handed-over key acknowledgment.",
            "If the landlord refuses, file an application before the local Rent Authority / Rent Tribunal or District Consumer Commission for deficiency of service and unlawful trade practice."
        ],
        "sources": [
            "Model Tenancy Act, Section 13 (Refund of Security Deposit)",
            "Transfer of Property Act, 1882 (Section 106 & 108)",
            "Consumer Protection Act, 2019 (Deficiency of Service in Rental Services)"
        ],
        "confidence": 96
    },
    {
        "id": "prop-02",
        "category": "Property Law",
        "keywords": ["evict", "eviction", "landlord", "electricity", "water", "lock", "throw out", "forceful", "tenant rights"],
        "question": "Can a landlord evict a tenant by cutting water, electricity, or locking the premises?",
        "answer": "Strictly illegal. A landlord cannot resort to self-help eviction methods such as disconnecting electricity, shutting off water supply, throwing out tenant belongings, or changing locks.",
        "simple_explanation": "Due process of law is mandatory. Essential utilities (water, electricity, sewage) are protected civil and statutory rights. Even if a tenant defaults on rent, the landlord must issue a formal legal notice and obtain an eviction decree from the competent Rent Court or Civil Court.",
        "important_points": [
            "Disconnection of essential services constitutes a criminal offence and an actionable civil wrong.",
            "The tenant can immediately approach the local Rent Authority or Magistrate under police assistance to restore utilities.",
            "Police cannot assist a landlord in forceful eviction without a certified court order.",
            "Tenants are entitled to interim injunctions restraining the landlord from disturbing peaceful possession."
        ],
        "next_steps": [
            "Dial 112 / visit local police station immediately and lodge a written complaint regarding harassment and utility disconnection.",
            "File an urgent petition before the Rent Authority or Civil Court seeking an interim mandatory injunction to restore electricity and water.",
            "Document all threats, audio/video recordings, and utility disconnection dates.",
            "Continue tendering rent through bank transfer or court deposit to avoid being declared a willful defaulter."
        ],
        "sources": [
            "Model Tenancy Act, Section 20 & 21 (Protection Against Withholding Essential Services)",
            "Transfer of Property Act, 1882 (Section 111 - Determination of Lease)",
            "Supreme Court: Ramesh Gobindram v. Sugra Humayun Mirza (Eviction Due Process)"
        ],
        "confidence": 98
    },
    {
        "id": "prop-03",
        "category": "Property Law",
        "keywords": ["buy property", "buying flat", "purchase flat", "title check", "encumbrance", "rera", "registry", "builder"],
        "question": "What legal due diligence should I conduct before buying a property or flat?",
        "answer": "Before purchasing real estate, comprehensive title verification, encumbrance checks, statutory municipal approval verification, and RERA registration compliance are essential.",
        "simple_explanation": "You must verify that the seller has clear, marketable title without pending bank mortgages, litigation, or unpaid municipal taxes. If purchasing from a builder, the project must have valid RERA registration and sanctioned floor plans.",
        "important_points": [
            "Obtain an Encumbrance Certificate (EC) for the preceding 13 to 30 years from the Sub-Registrar's Office.",
            "Verify Title Deeds going back at least 30 years to confirm an unbroken chain of ownership.",
            "Check RERA registration number and project status on your state RERA portal.",
            "Demand Sanctioned Building Plan, Commencement Certificate (CC), and Occupancy Certificate (OC)."
        ],
        "next_steps": [
            "Hire a local property advocate to issue a formal Title Search Report.",
            "Publish a public notice in two local newspapers inviting third-party objections before signing the final sale deed.",
            "Ensure the Sale Agreement includes clear possession date and penalty clauses.",
            "Pay stamp duty and register the Sale Deed at the local Sub-Registrar office."
        ],
        "sources": [
            "Transfer of Property Act, 1882 (Section 54 - Sale of Immovable Property)",
            "Real Estate (Regulation and Development) Act, 2016 (RERA Sections 3, 11, 14)",
            "Registration Act, 1908 (Section 17 - Compulsory Registration)"
        ],
        "confidence": 95
    },
    {
        "id": "prop-04",
        "category": "Property Law",
        "keywords": ["builder delay", "possession", "rera delay", "flat possession", "builder refund", "rera section 18"],
        "question": "What legal remedy do I have if a builder delays possession of my apartment?",
        "answer": "Under Section 18 of the RERA Act, 2016, a homebuyer has the statutory right to either withdraw from the project with a full refund plus compound interest, or claim monthly interest for every month of delay until possession is delivered.",
        "simple_explanation": "Builders cannot hide behind arbitrary delay excuses. RERA provides that if possession is not handed over within the date committed in the agreement, the builder must pay interest at the State Bank of India (SBI) Highest Marginal Cost of Funds Based Lending Rate (MCLR) plus 2%.",
        "important_points": [
            "You are not obligated to accept indefinite delay extensions.",
            "RERA orders are binding and can be executed through revenue recovery certificates.",
            "Homebuyers can also approach the Consumer Commission if the delay constitutes deficiency of service.",
            "Force majeure cannot be cited for routine labor shortages or funding bottlenecks."
        ],
        "next_steps": [
            "Check the promised possession date in your Builder-Buyer Agreement (BBA).",
            "File a formal online complaint on the State RERA portal under Section 18.",
            "Demand either refund with interest or monthly delay compensation.",
            "Attend RERA conciliation or hearing with proof of all payment installments made."
        ],
        "sources": [
            "Real Estate (Regulation and Development) Act, 2016 (Section 18 - Return of amount & compensation)",
            "Supreme Court: Pioneer Urban Land & Infrastructure Ltd. v. Govindan Raghavan",
            "State Real Estate Regulatory Authority (RERA) Rules"
        ],
        "confidence": 97
    },

    # -------------------------------------------------------------
    # 2. CONTRACT LAW
    # -------------------------------------------------------------
    {
        "id": "cont-01",
        "category": "Contract Law",
        "keywords": ["breach of contract", "broken agreement", "contract violation", "sue for contract", "damages", "breach"],
        "question": "What legal remedies are available when a party breaches a contract?",
        "answer": "When a breach of contract occurs, the aggrieved party is legally entitled to sue for compensatory damages, specific performance of the contract, or an injunction restraining further breach.",
        "simple_explanation": "Under the Indian Contract Act, the party that breaks an agreement must compensate the non-breaching party for naturally arising direct financial losses. If monetary compensation is inadequate, courts can compel the breaching party to actually execute their contractual promise.",
        "important_points": [
            "Damages are compensatory, not punitive; they cover actual direct loss caused by the breach (Section 73).",
            "Liquidated damages stipulated in the agreement must represent a genuine pre-estimate of loss (Section 74).",
            "The injured party has a legal duty to take reasonable steps to mitigate losses.",
            "Under the Specific Relief Act (as amended in 2018), specific performance is a primary remedy rather than a discretionary one."
        ],
        "next_steps": [
            "Collate the executed contract, amendment riders, correspondence, invoices, and delivery receipts.",
            "Serve a formal Legal Notice of Breach giving 15 to 30 days to cure the defect or remit damages.",
            "Check if the contract contains a mandatory Dispute Resolution or Arbitration clause.",
            "File a commercial suit or invoke arbitration if the party fails to comply."
        ],
        "sources": [
            "Indian Contract Act, 1872 (Sections 73, 74 & 75 - Consequences of Breach)",
            "Specific Relief Act, 1963 (Section 10 - Specific Performance)",
            "Commercial Courts Act, 2015"
        ],
        "confidence": 95
    },
    {
        "id": "cont-02",
        "category": "Contract Law",
        "keywords": ["non-compete", "non compete", "restraint of trade", "join competitor", "working for competitor", "job restriction"],
        "question": "Is a post-employment non-compete clause legally enforceable against an employee?",
        "answer": "No. In India and common law jurisdictions, post-termination non-compete clauses are void and unenforceable under statutory provisions against restraint of trade.",
        "simple_explanation": "Section 27 of the Indian Contract Act declares that every agreement restraining anyone from exercising a lawful profession, trade, or business is void. While an employer can restrict you while you are actively employed, they cannot legally stop you from working for a competitor after your employment ends.",
        "important_points": [
            "Post-employment restrictions on working anywhere in the industry are completely void under Section 27.",
            "However, confidentiality, proprietary data protection, and non-solicitation clauses remain legally binding.",
            "Employers cannot withhold relieving letters or full-and-final settlement solely based on joining a competitor.",
            "An ex-employee must not misappropriate trade secrets, codebases, or proprietary client databases."
        ],
        "next_steps": [
            "Carefully review the exact wording of the employment contract clause.",
            "Ensure you return all company hardware, source code, data, and access tokens before departing.",
            "Obtain written relieving confirmation upon completion of notice period.",
            "If an ex-employer sends a threatening legal notice, respond citing Section 27 and landmark Supreme Court precedents."
        ],
        "sources": [
            "Indian Contract Act, 1872 (Section 27 - Agreement in restraint of trade, void)",
            "Supreme Court: Niranjan Shankar Golikari v. Century Spg. & Mfg. Co. Ltd. (1967)",
            "Supreme Court: Percept D'Mark (India) Pvt. Ltd. v. Zaheer Khan (2006)"
        ],
        "confidence": 98
    },
    {
        "id": "cont-03",
        "category": "Contract Law",
        "keywords": ["cheque bounce", "bounced cheque", "dishonoured cheque", "section 138", "insufficient funds", "stop payment"],
        "question": "What is the legal procedure when a cheque bounces due to insufficient funds?",
        "answer": "Under Section 138 of the Negotiable Instruments Act, 1881, dishonour of a cheque for insufficiency of funds is a criminal offence punishable by up to two years imprisonment, a fine up to twice the cheque amount, or both.",
        "simple_explanation": "When a bank returns a cheque unpaid, you must issue a formal statutory demand notice to the drawer within 30 days of receiving the bank memo. If they do not pay within 15 days of receiving your notice, you have 30 days to file a criminal complaint before the Judicial Magistrate.",
        "important_points": [
            "The cheque must have been issued towards the discharge of a legally enforceable debt or liability.",
            "Strict limitation timeline: Statutory legal notice must be dispatched within 30 days of the bank memo.",
            "The drawer gets 15 days from notice delivery to make payment.",
            "If unpaid after 15 days, the criminal complaint must be filed within 30 days under Section 142.",
            "Under Section 143A, the court can direct the accused to deposit interim compensation up to 20% of the cheque amount."
        ],
        "next_steps": [
            "Preserve original cheque, bank return memo, and postal delivery slips.",
            "Have an advocate issue a Section 138 Statutory Demand Notice via Registered Speed Post.",
            "Track postal delivery proof and preserve screenshot of delivery confirmation.",
            "File a complaint before the competent Metropolitan/Judicial Magistrate upon expiry of the 15-day period."
        ],
        "sources": [
            "Negotiable Instruments Act, 1881 (Sections 138, 141, 142 & 143A)",
            "Supreme Court: Meters and Instruments Pvt. Ltd. v. Kanchan Mehta",
            "Supreme Court: Bir Singh v. Mukesh Kumar (2019)"
        ],
        "confidence": 99
    },
    {
        "id": "cont-04",
        "category": "Contract Law",
        "keywords": ["force majeure", "pandemic", "act of god", "contract frustration", "section 56", "impossibility"],
        "question": "What is a Force Majeure clause and when can a party legally invoke it?",
        "answer": "A Force Majeure clause excuses contractual performance when unforeseen, extraordinary events beyond human control (acts of God, war, pandemics, government bans) render performance physically or legally impossible.",
        "simple_explanation": "Force majeure cannot be claimed merely because a contract has become less profitable or commercially difficult. The invoking party must prove that the event was outside their control, could not be mitigated, and matches the specific triggering events enumerated in the agreement.",
        "important_points": [
            "The doctrine of frustration of contract is governed by Section 56 of the Indian Contract Act.",
            "Mandatory notice within the contractual deadline (e.g., within 7 days of occurrence) must be served.",
            "Commercial hardship or financial insolvency does not constitute force majeure.",
            "Courts strictly interpret force majeure clauses based on explicit contractual definitions."
        ],
        "next_steps": [
            "Inspect the exact wording of the Force Majeure clause in your agreement.",
            "Issue a formal written invocation notice citing the specific triggering event.",
            "Document all reasonable mitigation attempts and logs.",
            "Check if the clause provides for contract renegotiation, temporary suspension, or termination."
        ],
        "sources": [
            "Indian Contract Act, 1872 (Section 56 - Agreement to do impossible act)",
            "Supreme Court: Energy Watchdog v. CERC & Ors. (2017)",
            "Supreme Court: Satyabrata Ghose v. Mugneeram Bangur & Co. (1954)"
        ],
        "confidence": 94
    },

    # -------------------------------------------------------------
    # 3. EMPLOYMENT & LABOUR LAW
    # -------------------------------------------------------------
    {
        "id": "emp-01",
        "category": "Employment & Labour Law",
        "keywords": ["fire", "terminate", "wrongful termination", "fired without notice", "laid off", "pink slip", "severance"],
        "question": "Can my employer terminate me without notice or severance pay?",
        "answer": "Generally, no. Arbitrary termination without notice or salary in lieu of notice violates labour statutes and employment contract covenants.",
        "simple_explanation": "Employers are bound by statutory labour protections and state Shops and Commercial Establishments Acts. Unless you are terminated for proven gross misconduct following a fair domestic inquiry, the company must provide the contractual notice period (usually 30 to 90 days), salary in lieu thereof, and statutory retrenchment compensation.",
        "important_points": [
            "For workmen with over one year of continuous service, Section 25F of the Industrial Disputes Act mandates 1 month notice and 15 days average pay per completed year of service.",
            "For non-workmen / corporate staff, state Shops & Establishments legislation and employment appointment terms govern notice and severance.",
            "Termination for alleged misconduct without issuing a show-cause charge sheet and inquiry violates natural justice.",
            "Withholding earned wages, accrued leave encashment, or statutory dues is strictly unlawful."
        ],
        "next_steps": [
            "Check your appointment letter, probation clause, and termination provisions.",
            "Request written reasons for termination and detailed full-and-final (FnF) statement.",
            "Do not sign blank resignation or release waivers under duress.",
            "Serve a formal legal notice or file a complaint before the Labour Commissioner / Labour Court if severance is withheld."
        ],
        "sources": [
            "Industrial Disputes Act, 1947 (Section 25F - Conditions precedent to retrenchment)",
            "State Shops and Commercial Establishments Acts",
            "Payment of Gratuity Act, 1972"
        ],
        "confidence": 96
    },
    {
        "id": "emp-02",
        "category": "Employment & Labour Law",
        "keywords": ["unpaid salary", "delayed salary", "wages not paid", "salary hold", "pending salary", "company not paying"],
        "question": "What legal action can I take if my employer refuses to pay my salary?",
        "answer": "Non-payment of earned salary is illegal. Employees can recover unpaid wages with interest through the Labour Commissioner under the Payment of Wages Act, or by filing a summary suit / insolvency petition in court.",
        "simple_explanation": "An employer cannot unilaterally hold or refuse wages for work already performed. Employers are legally obligated to disburse salaries within 7 to 10 days of the wage period end. Unpaid salary is a debt owed to the employee.",
        "important_points": [
            "The Payment of Wages Act mandates timely payment and prohibits unauthorized wage deductions.",
            "Section 33C(2) of the Industrial Disputes Act allows recovery of money due from an employer.",
            "Corporate employees can file a summary suit under Order 37 of the CPC for fast recovery.",
            "If the company is defaulting systematically, employees can initiate operational insolvency proceedings before the NCLT."
        ],
        "next_steps": [
            "Send a formal written email to HR and Management detailing unpaid months, bank details, and total outstanding dues.",
            "Issue a statutory Demand Notice through an advocate giving 15 days for payment.",
            "File a complaint with the District Labour Commissioner / Labour Officer.",
            "Preserve salary slips, bank statements, offer letter, and attendance records as conclusive proof."
        ],
        "sources": [
            "Payment of Wages Act, 1936 (Sections 3, 5 & 15)",
            "Industrial Disputes Act, 1947 (Section 33C - Recovery of Money Due)",
            "Insolvency and Bankruptcy Code, 2016 (Operational Creditor Claims)"
        ],
        "confidence": 97
    },
    {
        "id": "emp-03",
        "category": "Employment & Labour Law",
        "keywords": ["relieving letter", "experience letter", "experience certificate", "fnf", "company refusing relieving", "notice period buy out"],
        "question": "Can an employer legally withhold my relieving letter or experience certificate after I resign?",
        "answer": "No. Once an employee has served the contractual notice period (or paid notice buy-out) and completed official handover, the employer cannot lawfully withhold the relieving letter, experience certificate, or statutory full-and-final settlement.",
        "simple_explanation": "An experience certificate is an acknowledgment of service rendered; it cannot be held hostage for unreasonable demands. High Courts have repeatedly ruled that withholding relieving documents impairs an individual's constitutional right to livelihood.",
        "important_points": [
            "Withholding service certificates after successful handover violates Article 19(1)(g) (Right to practice profession).",
            "The employer must provide an itemized handover clearance checklist.",
            "Notice period can either be served or settled through contractual notice pay buy-out.",
            "Employers cannot impose arbitrary penalties that were not part of the signed employment agreement."
        ],
        "next_steps": [
            "Send an email with signed asset handover confirmation, clearance slips, and request for relieving letter within 7 days.",
            "Have an advocate issue a formal legal notice warning of damages for loss of subsequent job opportunities.",
            "Approach the Labour Commissioner or file a civil writ petition if the employer causes willful career sabotage."
        ],
        "sources": [
            "Constitution of India, Article 19(1)(g) & Article 21 (Right to Livelihood)",
            "Bombay High Court: Dr. Sneha v. State of Maharashtra (Withholding service certificates)",
            "Relevant State Shops and Commercial Establishments Rules"
        ],
        "confidence": 95
    },
    {
        "id": "emp-04",
        "category": "Employment & Labour Law",
        "keywords": ["posh", "sexual harassment", "workplace harassment", "icc", "internal complaints committee", "posh act"],
        "question": "What are employee rights and protections under the POSH Act for workplace sexual harassment?",
        "answer": "Under the POSH Act 2013, every organization with 10 or more employees must constitute an Internal Complaints Committee (ICC). Employees are entitled to a time-bound, confidential inquiry, interim protection, and strict safety against retaliation.",
        "simple_explanation": "Sexual harassment includes unwelcome physical contact, sexually colored remarks, demands for sexual favors, showing pornography, or creating a hostile working environment. The inquiry must be completed within 90 days, and the complainant's identity must remain strictly confidential.",
        "important_points": [
            "Complaint must be submitted in writing to the ICC within 3 months of the incident (extendable by 3 months with valid reasons).",
            "The ICC is headed by a senior woman employee and must include an independent external NGO/legal expert.",
            "Complainants can request interim relief such as transfer, paid leave up to 3 months, or restraining the respondent from reporting on them.",
            "Retaliation or victimization against the complainant or witnesses attracts severe penalties."
        ],
        "next_steps": [
            "Submit a formal written complaint with detailed dates, times, messages, and witness names directly to the Presiding Officer of the ICC.",
            "If the employer has fewer than 10 employees or the complaint is against the employer, file with the District Local Complaints Committee (LCC).",
            "Preserve all digital evidence (WhatsApp chats, emails, recordings, CCTV requests).",
            "Call the National Commission for Women (NCW) helpline 7827170170 or emergency 112 if immediate safety is threatened."
        ],
        "sources": [
            "Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act, 2013 (POSH)",
            "Supreme Court Landmark: Vishaka v. State of Rajasthan (1997)",
            "Supreme Court: Aureliano Fernandes v. State of Goa (2023 Guidelines)"
        ],
        "confidence": 99
    },

    # -------------------------------------------------------------
    # 4. CONSUMER PROTECTION LAW
    # -------------------------------------------------------------
    {
        "id": "cons-01",
        "category": "Consumer Protection Law",
        "keywords": ["defective product", "refund", "return product", "faulty item", "ecommerce refund", "amazon refund", "flipkart refund"],
        "question": "What legal remedy do I have if an e-commerce website refuses a refund for a defective product?",
        "answer": "Under the Consumer Protection Act 2019, consumers have a statutory right to replacement or a full refund for defective merchandise, and sellers/platforms cannot enforce blanket 'no refund' terms against defective goods.",
        "simple_explanation": "E-commerce platforms and marketplace sellers are liable for delivering goods that fail to match advertised specifications, are damaged, or are counterfeit. You can file an instant online grievance with the National Consumer Helpline (1915) or an e-Daakhil consumer petition.",
        "important_points": [
            "Sellers cannot evade liability by citing arbitrary '7-day return policy expired' if the product has latent manufacturing defects.",
            "Marketplace entities must provide an acknowledgment number within 48 hours of grievance receipt and resolve it within 30 days.",
            "Consumers can claim reimbursement for the product cost plus compensation for harassment and legal expenses.",
            "District Consumer Commissions handle claims up to ₹50 Lakhs with minimal court fees."
        ],
        "next_steps": [
            "Save tax invoice, order confirmation, unboxing video/photographs, and customer support chat transcripts.",
            "Call the National Consumer Helpline at 1915 or register online at consumerhelpline.gov.in.",
            "Send a formal pre-litigation legal notice giving 15 days for a full refund.",
            "If unresolved, file an online consumer case on edaakhil.nic.in without requiring an advocate."
        ],
        "sources": [
            "Consumer Protection Act, 2019 (Sections 2(47), 35 & 84 - Product Liability)",
            "Consumer Protection (E-Commerce) Rules, 2020",
            "National Consumer Disputes Redressal Commission (NCDRC) Precedents"
        ],
        "confidence": 98
    },
    {
        "id": "cons-02",
        "category": "Consumer Protection Law",
        "keywords": ["edaakhil", "e-daakhil", "consumer forum", "consumer court", "file consumer complaint", "how to file complaint"],
        "question": "How do I file a consumer complaint online through e-Daakhil?",
        "answer": "e-Daakhil (edaakhil.nic.in) is the official government portal for paperless online filing of consumer disputes before District, State, and National Consumer Commissions across India.",
        "simple_explanation": "You do not need a lawyer to file a consumer case. Create an account on edaakhil.nic.in, draft your grievance stating facts, attach the purchase invoice and evidence, pay the nominal statutory court fee online, and submit.",
        "important_points": [
            "Pecuniary Jurisdiction: District Commission (up to ₹50 Lakh), State Commission (₹50 Lakh to ₹2 Crore), National Commission (above ₹2 Crore).",
            "Territorial Jurisdiction: You can file where you reside or work, not just where the seller is located.",
            "Statutory limitation period: Complaint must be filed within 2 years from the date of cause of action.",
            "Nominal fees: Claims up to ₹5 Lakh have zero court fee; higher slabs have minimal fees."
        ],
        "next_steps": [
            "Register on edaakhil.nic.in using your Aadhaar/Mobile OTP.",
            "Prepare a complaint petition in PDF stating: purchase facts, defect/deficiency, evidence, and relief sought.",
            "Upload supporting documents: invoices, emails, warranty card, photographs.",
            "Pay online fee via net banking / UPI and note the assigned Case Filing Reference Number."
        ],
        "sources": [
            "Consumer Protection Act, 2019 (Section 35 - Manner of Making Complaint)",
            "Consumer Protection (Consumer Commission Procedure) Regulations, 2020",
            "National Consumer Commission Portal (e-Daakhil Rules)"
        ],
        "confidence": 97
    },

    # -------------------------------------------------------------
    # 5. FAMILY & MATRIMONIAL LAW
    # -------------------------------------------------------------
    {
        "id": "fam-01",
        "category": "Family & Matrimonial Law",
        "keywords": ["divorce", "mutual divorce", "mutual consent divorce", "cooling off", "section 13b", "divorce procedure"],
        "question": "What is the procedure for divorce by mutual consent and what is the cooling-off period?",
        "answer": "Mutual consent divorce is governed by Section 13B of the Hindu Marriage Act (or Section 28 of the Special Marriage Act). Both spouses jointly petition the Family Court after living separately for at least one year.",
        "simple_explanation": "The process involves two motions. The First Motion records joint statements and terms of settlement (maintenance, child custody, asset division). A statutory 6-month cooling-off period is observed before the Second Motion, after which the decree of divorce is granted. The Supreme Court has held that the 6-month period can be waived if reconciliation is impossible.",
        "important_points": [
            "Pre-condition: Parties must have lived separately for a minimum period of one year prior to filing.",
            "Both spouses must mutually agree on permanent alimony, division of assets/stridhan, and child custody.",
            "First Motion: Statements recorded under oath; Second Motion: moved between 6 to 18 months thereafter.",
            "Cooling-off waiver: Under Amardeep Singh v. Harveen Kaur, the 6-month delay can be waived by submitting an application."
        ],
        "next_steps": [
            "Draft a comprehensive Memorandum of Understanding (MoU) detailing custody, alimony, and asset separation.",
            "File joint petition for First Motion before the Family Court having jurisdiction.",
            "Attend court hearing for recording statements and verification of settlement terms.",
            "File waiver application if parties have settled all issues and seek expedited decree."
        ],
        "sources": [
            "Hindu Marriage Act, 1955 (Section 13B - Divorce by Mutual Consent)",
            "Special Marriage Act, 1954 (Section 28)",
            "Supreme Court: Amardeep Singh v. Harveen Kaur (2017) (Waiver of statutory cooling-off period)"
        ],
        "confidence": 96
    },
    {
        "id": "fam-02",
        "category": "Family & Matrimonial Law",
        "keywords": ["will", "draft will", "valid will", "testament", "inheritance", "executor", "succession", "property will"],
        "question": "What are the essential legal requirements to draft a valid and dispute-free Will?",
        "answer": "Under the Indian Succession Act, 1925, a valid Will requires a testator of sound mind, written intent regarding property disposition, the testator's signature, and mandatory attestation by at least two independent witnesses.",
        "simple_explanation": "Anyone of sound mind who has attained majority can make a Will. It does not require stamp paper and can be written on plain paper. While registration at the Sub-Registrar's office is optional, registering it provides strong evidentiary protection against future claims of forgery or coercion.",
        "important_points": [
            "Capacity: Testator must possess sound disposing mind and act without undue influence or coercion.",
            "Attestation rule: Must be signed in the presence of at least two independent witnesses who must also sign in the testator's presence.",
            "Critical caution: Beneficiaries of the Will or their spouses should NEVER be attesting witnesses.",
            "Medical certificate: Attaching a fitness certificate from an MBBS doctor confirms mental alertness at execution."
        ],
        "next_steps": [
            "Prepare a complete schedule of all self-acquired properties, bank accounts, shares, and assets.",
            "Draft clear bequeathal clauses specifying exact shares for each beneficiary.",
            "Appoint a trusted Executor to oversee probate and distribution.",
            "Execute before two non-beneficiary witnesses and register at the Sub-Registrar's office."
        ],
        "sources": [
            "Indian Succession Act, 1925 (Sections 59, 63 & 68)",
            "Registration Act, 1908 (Section 18 - Optional Registration of Wills)",
            "Supreme Court: H. Venkatachala Iyengar v. B.N. Thimmajamma (Proof of Wills)"
        ],
        "confidence": 98
    },

    # -------------------------------------------------------------
    # 6. CYBER LAW & DIGITAL FRAUD
    # -------------------------------------------------------------
    {
        "id": "cyb-01",
        "category": "Cyber Law & Digital Fraud",
        "keywords": ["upi fraud", "scam", "cyber fraud", "money stolen", "fraudulent transaction", "1930", "bank hack", "phishing"],
        "question": "Someone stole money via a fraudulent UPI transaction. What is the immediate legal procedure?",
        "answer": "Immediately call the National Cyber Crime Helpline at 1930 within the 'Golden Hour' (first 2-4 hours) and report on cybercrime.gov.in. Simultaneously notify your bank in writing within 72 hours under RBI Zero Liability rules.",
        "simple_explanation": "Dialing 1930 activates the Citizen Financial Cyber Fraud Reporting System (CFCFRMS), which triggers automated inter-bank freeze tokens across recipient banks and payment gateways before the fraudsters can withdraw the funds.",
        "important_points": [
            "Golden Hour action: The first 2 to 4 hours are critical before stolen money passes through mule accounts.",
            "RBI Circular on Customer Protection: If you report unauthorized electronic banking within 3 working days, your liability is zero.",
            "Never share OTPs, UPI PINs, or screen-sharing apps (AnyDesk, TeamViewer) with anyone claiming to be bank staff.",
            "Bank branches cannot refuse to accept unauthorized transaction dispute forms."
        ],
        "next_steps": [
            "Dial 1930 immediately, provide transaction ID, amount, debit account number, and recipient UPI ID.",
            "Log onto cybercrime.gov.in and file a formal cyber fraud complaint with screenshots.",
            "Visit your home bank branch, submit a written dispute letter requesting account/card blocking, and obtain an acknowledgment stamp.",
            "Obtain acknowledgment token from Cyber Police for follow-up with the bank ombudsman."
        ],
        "sources": [
            "Information Technology Act, 2000 (Sections 43, 66C & 66D)",
            "RBI Circular: Customer Protection – Limiting Liability in Unauthorized Electronic Banking Transactions",
            "Indian Cyber Crime Coordination Centre (I4C) Operating Protocols"
        ],
        "confidence": 99
    },
    {
        "id": "cyb-02",
        "category": "Cyber Law & Digital Fraud",
        "keywords": ["blackmail", "online harassment", "cyber bullying", "nude", "morphing", "sextortion", "photos leaked"],
        "question": "What should I do if someone is blackmailing, stalking, or harassing me online with morphed photos or threats?",
        "answer": "Do not pay ransom or delete messages. Immediately lodge a complaint on the National Cyber Crime Reporting Portal (cybercrime.gov.in) under the Women & Children Cyber Crime module, and contact cyber police helpline 1930 or 112.",
        "simple_explanation": "Extortion, cyberstalking, creating morphed images, and non-consensual transmission of sexually explicit material are non-bailable criminal offences under the IT Act and Bharatiya Nyaya Sanhita (BNS). Police have dedicated cyber cells to trace IP addresses and compel social media platforms to remove defamatory content.",
        "important_points": [
            "Preserve digital evidence: Capture screenshots of profiles, chats, phone numbers, payment demands, and URLs before blocking.",
            "Never transfer money: Extortionists invariably demand more money after receiving an initial payment.",
            "Platform reporting: Use StopNCII.org and in-app reporting tools to hash and block image distribution across platforms.",
            "Police are legally required to keep the victim's identity completely confidential."
        ],
        "next_steps": [
            "Document all evidence: screenshots with visible timestamps, URLs, and phone numbers.",
            "File a report on cybercrime.gov.in under 'Report Women/Child Related Crime' (can be filed anonymously if needed).",
            "Submit a hash request on StopNCII.org to prevent image circulation.",
            "Approach the local Cyber Crime Police Station to register an FIR under Section 66E/67A of the IT Act."
        ],
        "sources": [
            "Information Technology Act, 2000 (Sections 66E - Violation of Privacy, 67 & 67A - Obscenity)",
            "Bharatiya Nyaya Sanhita, 2023 (Sections 308 - Extortion, 354D - Cyber Stalking)",
            "National Cyber Crime Reporting Portal Protocol"
        ],
        "confidence": 99
    },

    # -------------------------------------------------------------
    # 7. CRIMINAL LAW & POLICE PROCEDURES
    # -------------------------------------------------------------
    {
        "id": "crim-01",
        "category": "Criminal Law & Police Procedures",
        "keywords": ["fir", "zero fir", "police refuse fir", "refusing fir", "police complaint", "register fir"],
        "question": "What is a Zero FIR and what legal remedies do I have if police refuse to register an FIR?",
        "answer": "A Zero FIR allows any police station to register a First Information Report for a cognizable offence regardless of jurisdictional territory. If police refuse to register an FIR, you can approach the Superintendent of Police (SP) or file a Section 156(3) application before the Magistrate.",
        "simple_explanation": "Under landmark Supreme Court rulings (Lalita Kumari), registration of an FIR is mandatory for cognizable offences (theft, assault, rape, cheating, robbery). Police cannot refuse registration citing that the crime occurred outside their precinct. A Zero FIR is transferred to the competent jurisdiction after initial registration.",
        "important_points": [
            "Mandatory duty: Station House Officers (SHOs) are statutorily required to register an FIR upon disclosure of a cognizable offence.",
            "Refusal remedy 1: Send the written complaint via Registered Post to the Superintendent of Police / Deputy Commissioner of Police (DCP).",
            "Refusal remedy 2: File an application under Section 156(3) of CrPC (Section 175 BNSS) before the Judicial Magistrate to direct police to register an FIR.",
            "Police officers refusing to register an FIR for specified offences face criminal prosecution under the law."
        ],
        "next_steps": [
            "Submit a signed written complaint to the Station House Officer (SHO) and demand a dated receiving acknowledgment stamp.",
            "If refused, dispatch the complaint to the district SP / Commissioner of Police via Registered Post.",
            "Engage an advocate to file a private complaint under Section 200 CrPC or Section 156(3) direction before the local Magistrate.",
            "Retain postal tracking slips and copies of all submitted representations."
        ],
        "sources": [
            "Code of Criminal Procedure, 1973 (Section 154 - Information in cognizable cases & Section 156(3))",
            "Bharatiya Nagarik Suraksha Sanhita, 2023 (Section 173 - Zero FIR & Section 175)",
            "Supreme Court Constitution Bench: Lalita Kumari v. Govt. of U.P. (2014) (Mandatory FIR)"
        ],
        "confidence": 99
    },
    {
        "id": "crim-02",
        "category": "Criminal Law & Police Procedures",
        "keywords": ["arrest", "police arrest", "arrest rights", "dk basu", "handcuff", "bail", "arrested"],
        "question": "What are my constitutional and legal rights if arrested or detained by the police?",
        "answer": "Every arrested individual is protected by strict constitutional safeguards and the D.K. Basu guidelines, including the right to know grounds of arrest, right to inform a family member, right to legal counsel, mandatory medical examination, and production before a Magistrate within 24 hours.",
        "simple_explanation": "Police cannot arbitrarily arrest or torture anyone. Under Article 22 of the Constitution, you have the right to remain silent, consult an advocate of your choice, and demand a written Arrest Memo signed by a witness. Women cannot be arrested after sunset and before sunrise without prior magistrate permission.",
        "important_points": [
            "Right to know grounds: Police must communicate the full particulars of the offence and whether the offence is bailable.",
            "Arrest Memo: Police must prepare a formal arrest memo recording time, date, location, signed by at least one family member or respectable local witness.",
            "Right to inform: Police must inform a nominated friend or family member within 8-12 hours of arrest.",
            "Mandatory 24-hour rule: The arrested person must be produced before the nearest Judicial Magistrate within 24 hours of arrest (excluding travel time).",
            "Medical examination: You are entitled to a medical checkup every 48 hours and upon arrest to document physical condition."
        ],
        "next_steps": [
            "Politely state your right to legal counsel and request to speak with your advocate.",
            "Request the arresting officer's full name, rank, and police station designation.",
            "Demand that a family member be notified immediately and that an Arrest Memo be prepared.",
            "Ensure injuries or health conditions are recorded in the official Medico-Legal Certificate (MLC)."
        ],
        "sources": [
            "Constitution of India, Article 21 & Article 22 (Protection against arrest and detention)",
            "Code of Criminal Procedure, 1973 (Sections 41A, 41B, 50, 54 & 57)",
            "Supreme Court: D.K. Basu v. State of West Bengal (1997) (Landmark Arrest Guidelines)",
            "Supreme Court: Arnesh Kumar v. State of Bihar (2014) (Restricting routine arrests for offences under 7 years)"
        ],
        "confidence": 99
    },
    {
        "id": "crim-03",
        "category": "Criminal Law & Police Procedures",
        "keywords": ["bail", "anticipatory bail", "bailable", "non-bailable", "section 438", "prevent arrest"],
        "question": "What is the difference between bailable and non-bailable offences, and how does Anticipatory Bail work?",
        "answer": "In bailable offences, bail is an absolute statutory right that the police or court must grant upon furnishing surety. In non-bailable offences, bail is discretionary. Anticipatory Bail (Section 438 CrPC / Section 482 BNSS) is a pre-arrest protective order granted by the Sessions Court or High Court.",
        "simple_explanation": "If you apprehend that you may be falsely implicated or arrested in a non-bailable case, your advocate can petition the Sessions Court or High Court for Anticipatory Bail. If granted, the police cannot arrest you in custody upon booking the offence and must release you on bail.",
        "important_points": [
            "Bailable offences: Police station itself is bound to release the accused on executing a personal bond with or without sureties.",
            "Non-bailable offences: Does not mean bail cannot be granted; it means the court exercises judicial discretion considering gravity, flight risk, and evidence tampering.",
            "Anticipatory bail: Can be applied for even before an FIR is officially registered if there is genuine apprehension of arrest.",
            "Conditions: Courts typically impose conditions such as surrendering passport, cooperating with investigation, and not contacting witnesses."
        ],
        "next_steps": [
            "Engage a criminal defence advocate immediately upon suspecting an imminent false complaint.",
            "Draft an Anticipatory Bail petition detailing facts, clean background, roots in society, and reasons for false implication.",
            "File the application before the Principal District and Sessions Judge or High Court.",
            "Keep sureties and address proofs ready for executing the bail bond upon grant."
        ],
        "sources": [
            "Code of Criminal Procedure, 1973 (Sections 436 - Bailable, 437 & 439 - Regular Bail, 438 - Anticipatory Bail)",
            "Bharatiya Nagarik Suraksha Sanhita, 2023 (Sections 478 to 484)",
            "Supreme Court Constitution Bench: Sushila Aggarwal v. State (NCT of Delhi) (2020)"
        ],
        "confidence": 97
    },

    # -------------------------------------------------------------
    # 8. CORPORATE, STARTUP & BUSINESS LAW
    # -------------------------------------------------------------
    {
        "id": "corp-01",
        "category": "Corporate, Startup & Business Law",
        "keywords": ["msme", "delayed payment", "msme samadhaan", "buyer not paying", "supplier payment", "msme act 45 days"],
        "question": "What legal remedy do small businesses have for delayed payments under MSME Samadhaan?",
        "answer": "Under the MSMED Act, 2006, buyers are legally required to make payment within 45 days. Delayed payments attract statutory compound interest at 3 times the RBI bank rate, recoverable through the MSME Samadhaan conciliation council.",
        "simple_explanation": "If your business has Udyam MSME registration, the buyer cannot delay payment beyond 45 days (or 15 days without written agreement). You can file a claim online on samadhaan.msme.gov.in. The Micro and Small Enterprises Facilitation Council (MSEFC) issues legally enforceable awards that have the force of a court decree.",
        "important_points": [
            "Maximum payment window: Cannot exceed 45 days from the date of acceptance of goods/services.",
            "Penal interest: Buyer must pay monthly compound interest at three times the RBI Bank Rate on outstanding amounts.",
            "Appeals restriction: The buyer cannot appeal an MSEFC award without first depositing 75% of the awarded amount in court.",
            "Income Tax clause (Section 43B(h)): Buyers cannot claim tax deduction on unpaid MSME expenses unless cleared on time."
        ],
        "next_steps": [
            "Ensure your Udyam MSME Registration was active on the date the purchase order/invoice was issued.",
            "Log into samadhaan.msme.gov.in and upload the invoices, delivery challans, and purchase order.",
            "The Facilitation Council will issue a conciliation notice to the defaulting buyer.",
            "If conciliation fails, the council conducts arbitration and issues a binding award for principal plus compound interest."
        ],
        "sources": [
            "Micro, Small and Medium Enterprises Development (MSMED) Act, 2006 (Sections 15 to 19)",
            "Income Tax Act, 1961 (Section 43B(h) - Deductions on actual payment)",
            "Supreme Court: Silpi Industries v. Kerala State Road Transport Corporation (2021)"
        ],
        "confidence": 98
    },
    {
        "id": "corp-02",
        "category": "Corporate, Startup & Business Law",
        "keywords": ["trademark", "brand protection", "ipr", "copyright", "infringement", "register brand", "trademark logo"],
        "question": "How do I legally protect my brand name and logo through trademark registration?",
        "answer": "Trademark registration under the Trade Marks Act, 1999 grants exclusive nationwide proprietary rights to use a brand name, logo, or tagline for goods/services within specific classes for a renewable 10-year period.",
        "simple_explanation": "Filing a trademark application allows you to use the ™ symbol immediately and prevents competitors from copying your identity. Once registered after public examination and advertisement in the Trademark Journal, you receive the ® symbol and can sue infringers for statutory damages and injunctions.",
        "important_points": [
            "Trademark Search: Conduct public search on ipindiaonline.gov.in across relevant Nice Classes (1-45).",
            "Distinctiveness: Descriptive or generic names are routinely objected to; inventive, coined words receive strongest legal protection.",
            "Right to sue: Registered owners can file civil suits for infringement and claim account of profits, interim injunctions, and delivery-up of counterfeit goods.",
            "Opposition window: Following publication in the journal, a 4-month public opposition period applies."
        ],
        "next_steps": [
            "Conduct comprehensive clearance search on ipindiaonline.gov.in to confirm no identical or deceptively similar marks exist.",
            "File Form TM-A online through an IP attorney with the trademark representation and user affidavit.",
            "Respond to Examination Report objections (Sections 9 & 11) within 30 days.",
            "Track status until registration certificate is issued and renew every 10 years."
        ],
        "sources": [
            "Trade Marks Act, 1999 (Sections 9, 11, 28 & 29 - Rights and Infringement)",
            "Trade Marks Rules, 2017",
            "Supreme Court: Cadila Health Care Ltd. v. Cadila Pharmaceuticals Ltd."
        ],
        "confidence": 96
    },

    # -------------------------------------------------------------
    # 9. CONSTITUTIONAL & CIVIL RIGHTS
    # -------------------------------------------------------------
    {
        "id": "const-01",
        "category": "Constitutional & Civil Rights",
        "keywords": ["rti", "right to information", "file rti", "public information officer", "government records", "rti timeline"],
        "question": "How do I file a Right to Information (RTI) application and what are the timelines?",
        "answer": "Under the RTI Act 2005, every Indian citizen has the statutory right to seek information from public authorities. Applications can be filed online at rtionline.gov.in with a ₹10 fee. The Public Information Officer (PIO) must furnish information within 30 days.",
        "simple_explanation": "Any information held by government departments, ministries, municipal corporations, public sector banks, and government universities can be requested. If the requested information concerns a person's life or liberty, it must be provided within 48 hours.",
        "important_points": [
            "Application fee: Just ₹10 (free for citizens below poverty line / BPL card holders).",
            "Mandatory 30-day timeline: PIO must either provide information or reject under Section 8 exemptions within 30 calendar days.",
            "First Appeal: If no response is received in 30 days or unsatisfactory data is given, file a First Appeal within 30 days to the First Appellate Authority (FAA).",
            "Second Appeal & Penalty: The Central/State Information Commission can impose personal fines of ₹250 per day up to ₹25,000 on defaulting PIOs."
        ],
        "next_steps": [
            "Visit rtionline.gov.in (for Central ministries) or state RTI portals.",
            "Draft clear, specific, numbered questions requesting certified copies or inspecting records (avoid asking for opinions).",
            "Pay the ₹10 fee online via UPI, net banking, or debit card.",
            "Track registration number; if no reply is received within 30 days, file First Appeal online."
        ],
        "sources": [
            "Right to Information Act, 2005 (Sections 6, 7 - Timelines, 8 - Exemptions & 20 - Penalties)",
            "Supreme Court: CBSE v. Aditya Bandopadhyay (2011)",
            "Central Information Commission (CIC) Guidelines"
        ],
        "confidence": 98
    },
    {
        "id": "const-02",
        "category": "Constitutional & Civil Rights",
        "keywords": ["traffic police", "vehicle check", "police stop", "driving license", "seize vehicle", "traffic rules", "challan"],
        "question": "What are a citizen's legal rights if stopped by traffic police for a vehicle check?",
        "answer": "Traffic police can stop vehicles to check documents and enforce traffic rules, but officers must be in uniform wearing a visible name badge. Only officers of Sub-Inspector rank or above are authorized to issue compounding fines, and police cannot confiscate car keys or physically assault drivers.",
        "simple_explanation": "You are legally permitted to present digital versions of your Driving License, RC, Insurance, and PUC via government-recognized DigiLocker or mParivahan apps. Traffic police cannot force you out of your car without cause or snatch your ignition key.",
        "important_points": [
            "Digital validity: Under Motor Vehicles Rules, original physical documents are not mandatory; DigiLocker / mParivahan digital copies are legally valid.",
            "Compounding fines: Constables or head constables cannot issue spot challans above prescribed limits; a Sub-Inspector (one star or above) is required.",
            "Key snatching illegal: Police officers have no legal authority to forcefully remove car keys from vehicle ignitions.",
            "Breathalyzer test: If alcohol is suspected, police must use a calibrated breathalyzer; refusal can lead to hospital medical examination and Section 185 charges."
        ],
        "next_steps": [
            "Keep documents updated on DigiLocker or mParivahan on your smartphone.",
            "Politely request the officer's name and identity badge if they demand spot cash fines without an e-challan receipt.",
            "Demand an official electronic e-challan or court summons receipt.",
            "If an officer engages in misconduct or extortion, capture video evidence and file a complaint with the Traffic Police Complaints Authority / Vigilance cell."
        ],
        "sources": [
            "Motor Vehicles Act, 1988 (Sections 130, 185 & 207)",
            "Central Motor Vehicles Rules, 1989 (Rule 139 - DigiLocker acceptance)",
            "Ministry of Road Transport and Highways (MoRTH) Circulars on Digital Documents"
        ],
        "confidence": 97
    }
]

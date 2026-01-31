"""
╔══════════════════════════════════════════════════════════════════╗
║   DPDP Act 2023 — Internal Audit Tool  (Streamlit App)          ║
║   Digital Personal Data Protection Act, 2023 | India             ║
║   All 44 Sections | 9 Chapters | Audit Procedures + Checklists  ║
╚══════════════════════════════════════════════════════════════════╝

Run:  streamlit run dpdp_audit_tool.py
"""

import streamlit as st
from datetime import datetime

# ─── PAGE CONFIG ─────────────────────────────────────────────────
st.set_page_config(
    page_title="DPDP Act 2023 – Internal Audit Tool",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── CUSTOM CSS ──────────────────────────────────────────────────
CUSTOM_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=DM+Sans:wght@400;500;600&display=swap');

    :root {
        --navy: #0f1b2d;
        --navy-mid: #1a2e4a;
        --saffron: #f59e0b;
        --green: #10b981;
        --green-light: #d1fae5;
        --red: #ef4444;
        --cream: #f8f7f2;
    }

    /* Full-page background */
    .stApp { background-color: var(--cream); font-family: 'DM Sans', sans-serif; }

    /* Header banner */
    .dpdp-header {
        background: linear-gradient(135deg, #0f1b2d 0%, #1a2e4a 60%, #243b5e 100%);
        border-radius: 0 0 16px 16px;
        padding: 28px 36px;
        display: flex;
        align-items: center;
        gap: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.25);
        margin: -16px -16px 24px -16px;
    }

    .dpdp-header .logo-circle {
        width: 64px; height: 64px;
        background: rgba(245,158,11,0.15);
        border: 2.5px solid #f59e0b;
        border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        font-size: 1.8rem; flex-shrink: 0;
    }

    .dpdp-header h1 {
        font-family: 'Playfair Display', serif;
        color: #fff; font-size: 1.7rem; margin: 0;
    }

    .dpdp-header .sub { color: #fcd34d; font-size: 0.72rem; text-transform: uppercase; letter-spacing: 2.5px; margin-top: 4px; }

    /* Chapter card */
    .ch-card {
        background: #fff;
        border-radius: 12px;
        border: 1.5px solid #e2e8f0;
        margin-bottom: 12px;
        box-shadow: 0 2px 10px rgba(15,27,45,0.06);
        overflow: hidden;
    }

    .ch-card-header {
        background: #fafafa;
        padding: 14px 20px;
        display: flex; align-items: center; gap: 14px;
        border-bottom: 1.5px solid #e2e8f0;
        cursor: pointer;
    }

    .ch-card-header:hover { background: #f0f4f8; }

    .ch-badge {
        background: var(--navy);
        color: #fff;
        font-size: 0.68rem; font-weight: 600;
        padding: 3px 10px; border-radius: 12px;
        white-space: nowrap;
    }

    .ch-card-header h3 { font-family: 'Playfair Display', serif; margin: 0; font-size: 1rem; color: #1e293b; }
    .ch-card-header .ch-sub { font-size: 0.72rem; color: #94a3b8; margin-top: 2px; }

    /* Section detail box */
    .sec-detail-box {
        background: #f8fafc;
        border: 1px solid #eef1f5;
        border-radius: 8px;
        padding: 14px 18px;
        margin-top: 8px;
    }

    .sec-detail-box .det-label {
        font-size: 0.68rem; font-weight: 600;
        text-transform: uppercase; letter-spacing: 1.2px;
        color: var(--saffron); margin-bottom: 6px; margin-top: 12px;
    }
    .sec-detail-box .det-label:first-child { margin-top: 0; }

    .sec-detail-box .det-text { font-size: 0.8rem; color: #475569; line-height: 1.65; }

    .audit-step-row { display: flex; gap: 10px; align-items: flex-start; margin-bottom: 8px; }
    .audit-step-row .step-circle {
        background: var(--navy); color: #fff;
        width: 24px; height: 24px; border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        font-size: 0.7rem; font-weight: 700; flex-shrink: 0;
    }
    .audit-step-row .step-text { font-size: 0.79rem; color: #475569; line-height: 1.55; padding-top: 4px; }

    .risk-high { color: #ef4444; background: #fee2e2; padding: 2px 8px; border-radius: 10px; font-size: 0.68rem; font-weight: 600; }
    .risk-medium { color: #b45309; background: #fef3c7; padding: 2px 8px; border-radius: 10px; font-size: 0.68rem; font-weight: 600; }
    .risk-low { color: #047857; background: #d1fae5; padding: 2px 8px; border-radius: 10px; font-size: 0.68rem; font-weight: 600; }

    /* Progress bar override */
    .stProgress .st-ca { background-color: var(--green) !important; }

    /* Footer */
    .dpdp-footer {
        background: var(--navy);
        border-radius: 12px;
        padding: 20px 28px;
        margin-top: 32px;
        display: flex; justify-content: space-between; align-items: center;
        flex-wrap: wrap; gap: 12px;
    }
    .dpdp-footer .f-left .f-title { color: #fff; font-weight: 600; font-size: 0.82rem; }
    .dpdp-footer .f-left .f-copy { color: #94a3b8; font-size: 0.68rem; margin-top: 2px; }
    .dpdp-footer .f-right { color: #94a3b8; font-size: 0.67rem; text-align: right; line-height: 1.6; }
    .dpdp-footer .f-right span { color: #fcd34d; }

    /* Streamlit widget tweaks */
    .stCheckbox label { font-size: 0.82rem !important; font-weight: 500; }
    div[data-testid="stExpander"] { border-radius: 8px; }
</style>
"""

# ─── DATA ────────────────────────────────────────────────────────
CHAPTERS = [
    {
        "id": "ch1",
        "title": "Chapter I — Preliminary",
        "sections": [
            {
                "num": "1", "title": "Short Title and Commencement", "risk": "low",
                "desc": "Defines the Act's name and provides that it comes into force on dates notified by the Central Government in phases.",
                "steps": [
                    "Verify the organisation is aware of the phased enforcement timeline notified by the Central Government.",
                    "Confirm internal legal/compliance teams have mapped which sections are currently in force vs. upcoming.",
                    "Cross-reference with the official MeitY Gazette notification dates."
                ]
            },
            {
                "num": "2", "title": "Definitions", "risk": "medium",
                "desc": "Establishes key terms: Personal Data, Data Fiduciary, Data Principal, Data Processor, Consent, Legitimate Use, etc.",
                "steps": [
                    "Audit whether the organisation's internal data glossary aligns with the Act's statutory definitions.",
                    "Verify that 'Data Fiduciary' and 'Data Principal' roles are correctly identified across all business units.",
                    "Check that 'Personal Data' classification is consistently applied in data inventories."
                ]
            }
        ]
    },
    {
        "id": "ch2",
        "title": "Chapter II — Obligations of Data Fiduciary",
        "sections": [
            {
                "num": "3", "title": "Application of the Act", "risk": "high",
                "desc": "Defines territorial and extra-territorial scope: applies to digital personal data collected in India or processed outside India for offering goods/services to Indian Data Principals.",
                "steps": [
                    "Map all data flows — identify personal data processed within and outside India.",
                    "Confirm cross-border processing activities are documented and linked to offering goods/services in India.",
                    "Validate that personal/domestic-use exclusions are correctly applied."
                ]
            },
            {
                "num": "4", "title": "Processing of Personal Data", "risk": "high",
                "desc": "Personal data shall be processed only for a lawful purpose for which the Data Principal has given consent or for a Legitimate Use.",
                "steps": [
                    "Audit all processing activities against documented lawful purposes.",
                    "Verify each processing activity has a corresponding valid consent record or a documented legitimate-use basis.",
                    "Review data processing registers for completeness and accuracy."
                ]
            },
            {
                "num": "5", "title": "Notice to Data Principal", "risk": "high",
                "desc": "Before or at the time of collecting consent, the Data Fiduciary must provide a clear, concise notice of what data is collected and for what purpose.",
                "steps": [
                    "Review all consent collection touchpoints (web forms, apps, SMS, etc.) for presence of privacy notices.",
                    "Validate that notices are available in at least one of the 22 scheduled languages.",
                    "Test notice clarity — ensure a lay user can understand the purpose and scope of data processing."
                ]
            },
            {
                "num": "6", "title": "Consent", "risk": "high",
                "desc": "Consent must be free, specific, informed, and unambiguous. It can be withdrawn at any time. Consent for children requires parental/guardian verification.",
                "steps": [
                    "Audit consent mechanisms for clarity and granularity (specific, informed, unambiguous).",
                    "Verify a functional consent-withdrawal mechanism exists and is easily accessible.",
                    "Check child-data processes — confirm parental/guardian consent verification is in place for users under 18.",
                    "Review Consent Manager integration if applicable."
                ]
            },
            {
                "num": "7", "title": "Legitimate Uses", "risk": "medium",
                "desc": "Lists specific scenarios where personal data may be processed without consent — e.g., employment, medical emergencies, legal compliance, government services.",
                "steps": [
                    "Identify all processing activities relying on legitimate-use grounds.",
                    "Map each legitimate-use claim to the specific enumerated purpose in the Act.",
                    "Ensure proper documentation exists for each legitimate-use invocation."
                ]
            },
            {
                "num": "8", "title": "Obligations of Data Fiduciary", "risk": "high",
                "desc": "Core obligations: ensure accuracy, implement reasonable security measures, notify breaches, and honour Data Principal rights within reasonable timelines.",
                "steps": [
                    "Audit data accuracy practices — validate update/correction workflows.",
                    "Review security controls: encryption, access controls, penetration testing, incident response.",
                    "Confirm breach notification procedures exist and include reporting to the Data Protection Board.",
                    "Verify timelines for responding to Data Principal requests are defined and tracked."
                ]
            },
            {
                "num": "9", "title": "Duty to Erase Personal Data", "risk": "medium",
                "desc": "Data Fiduciaries must erase personal data when it is no longer needed for the purpose it was collected, or when consent is withdrawn.",
                "steps": [
                    "Audit data retention schedules across all systems and databases.",
                    "Verify automated or manual erasure workflows are operational.",
                    "Test the erasure mechanism — confirm data is actually deleted (including backups, logs).",
                    "Cross-check with Data Processors to ensure downstream erasure compliance."
                ]
            },
            {
                "num": "10", "title": "Significant Data Fiduciary", "risk": "high",
                "desc": "Central Government may designate certain Data Fiduciaries as 'Significant' based on volume, sensitivity, and risk. Such entities face additional obligations: DPO appointment, data audits, and DPIA.",
                "steps": [
                    "Assess whether the organisation meets criteria for Significant Data Fiduciary designation.",
                    "If designated (or likely), confirm a Data Protection Officer (DPO) based in India is appointed.",
                    "Verify an independent data audit is conducted periodically.",
                    "Review whether a Data Protection Impact Assessment (DPIA) has been performed."
                ]
            }
        ]
    },
    {
        "id": "ch3",
        "title": "Chapter III — Rights & Duties of Data Principal",
        "sections": [
            {
                "num": "11", "title": "Right to Access Information", "risk": "medium",
                "desc": "Data Principals have the right to obtain a summary of personal data processed, the identities of Data Fiduciaries and Processors, and details of processing activities.",
                "steps": [
                    "Verify a mechanism exists for Data Principals to request access to their data.",
                    "Test the request-to-response workflow end-to-end.",
                    "Confirm the response includes all mandatory elements: data summary, fiduciary identities, processing details."
                ]
            },
            {
                "num": "12", "title": "Right to Correction and Erasure", "risk": "medium",
                "desc": "Data Principals may request correction of inaccurate or incomplete personal data and erasure of their data, subject to legal retention requirements.",
                "steps": [
                    "Audit the correction-request workflow for completeness.",
                    "Verify erasure requests are actioned within a reasonable timeframe.",
                    "Ensure legal-hold and retention exceptions are properly documented and communicated."
                ]
            },
            {
                "num": "13", "title": "Right to Nominate", "risk": "low",
                "desc": "A Data Principal may nominate another individual to exercise their rights in case of death or incapacity.",
                "steps": [
                    "Check whether a nomination mechanism is available within the organisation's data services.",
                    "Verify the nomination process is documented and legally sound.",
                    "Confirm the nominated person can actually exercise rights upon the triggering event."
                ]
            },
            {
                "num": "14", "title": "Grievance Redressal", "risk": "medium",
                "desc": "Data Fiduciaries must provide an accessible grievance redressal mechanism. Data Principals must exhaust this before approaching the Data Protection Board.",
                "steps": [
                    "Audit the grievance redressal portal/process for accessibility and responsiveness.",
                    "Verify response timelines are defined and met.",
                    "Check that the mechanism is prominently displayed in all privacy notices and communications."
                ]
            },
            {
                "num": "15", "title": "Duties of Data Principal", "risk": "low",
                "desc": "Data Principals must not supply false or fabricated personal data, and must not impersonate another person when giving consent.",
                "steps": [
                    "Review terms-of-service and onboarding flows to ensure these duties are clearly communicated.",
                    "Confirm that fraud-detection measures are in place for identity verification at consent stage."
                ]
            }
        ]
    },
    {
        "id": "ch4",
        "title": "Chapter IV — Special Provisions",
        "sections": [
            {
                "num": "16", "title": "Processing of Children's Personal Data", "risk": "high",
                "desc": "Children (under 18) require verifiable parental/guardian consent. Central Government may exempt certain Data Fiduciaries if they demonstrate adequate safeguards for children's data.",
                "steps": [
                    "Map all services or products accessible to users under 18.",
                    "Verify age-verification mechanisms are in place before data collection.",
                    "Confirm parental/guardian consent workflows are robust and verifiable.",
                    "Document any exemption application if applicable."
                ]
            },
            {
                "num": "17", "title": "Exemptions", "risk": "medium",
                "desc": "Certain processing activities are exempt from Act obligations — including national security, public order, research, and startup exemptions notified by the Central Government.",
                "steps": [
                    "Identify any processing activities that may qualify for an exemption.",
                    "Confirm the exemption has been formally notified by the Central Government.",
                    "Document the basis for claiming each exemption and maintain audit trail."
                ]
            }
        ]
    },
    {
        "id": "ch5",
        "title": "Chapter V — Data Protection Board of India",
        "sections": [
            {
                "num": "18", "title": "Establishment of the Board", "risk": "low",
                "desc": "Establishes the Data Protection Board of India as the statutory adjudicatory body for resolving disputes related to personal data breaches and Act violations.",
                "steps": [
                    "Confirm internal awareness of the Board's existence and its role.",
                    "Ensure the organisation's breach notification procedures include reporting to the Board.",
                    "Monitor Board notifications and guidance for compliance updates."
                ]
            },
            {
                "num": "19", "title": "Composition of the Board", "risk": "low",
                "desc": "The Board comprises a Chairperson and members appointed by the Central Government; tenure is two years with possibility of reappointment.",
                "steps": ["No direct organisational obligation — monitor for any changes in Board composition that affect regulatory stance."]
            },
            {
                "num": "20", "title": "Qualification and Conditions of Service", "risk": "low",
                "desc": "Prescribes qualifications, service conditions, and removal grounds for Board members.",
                "steps": ["No direct organisational obligation — track for governance changes."]
            },
            {
                "num": "21", "title": "Meetings of the Board", "risk": "low",
                "desc": "Governs how and when the Board meets and conducts its proceedings.",
                "steps": ["No direct organisational obligation — monitor Board meeting outcomes for compliance implications."]
            },
            {
                "num": "22", "title": "Powers and Duties of the Board", "risk": "medium",
                "desc": "The Board can investigate complaints, summon information, inspect records, and direct remedial/mitigation measures in case of breaches.",
                "steps": [
                    "Ensure the organisation is prepared to respond to Board summons or information requests.",
                    "Maintain a readiness plan for Board inspections — data access logs, records, and remediation evidence."
                ]
            },
            {
                "num": "23", "title": "Adjudication of Complaints", "risk": "medium",
                "desc": "Data Principals may file complaints with the Board only after exhausting the grievance redressal mechanism of the Data Fiduciary.",
                "steps": [
                    "Audit the completeness and effectiveness of the internal grievance mechanism to minimise Board escalations.",
                    "Track any complaints filed with the Board and their outcomes."
                ]
            },
            {
                "num": "24", "title": "Powers regarding Breach", "risk": "high",
                "desc": "Upon receipt of a breach intimation, the Board may direct urgent remedial or mitigation measures and investigate the root cause.",
                "steps": [
                    "Test the breach notification workflow — simulate a breach scenario end-to-end.",
                    "Ensure incident response plans include Board communication protocols.",
                    "Validate that remedial measures can be executed promptly post-breach."
                ]
            },
            {
                "num": "25", "title": "Voluntary Undertaking", "risk": "low",
                "desc": "A Data Fiduciary may voluntarily offer an undertaking to the Board to take specific actions; violation of such undertaking triggers penalties.",
                "steps": [
                    "Review any voluntary undertakings made to the Board.",
                    "Monitor compliance with each undertaking term and maintain evidence."
                ]
            },
            {
                "num": "26", "title": "Penalty Determination", "risk": "high",
                "desc": "The Board determines penalties based on factors including gravity, repetitiveness, and nature of the breach. Maximum penalty is ₹250 crore.",
                "steps": [
                    "Understand the penalty framework and factors that influence quantum.",
                    "Conduct risk assessment of potential penalty exposure based on current compliance gaps.",
                    "Prioritise remediation of high-risk areas to minimise penalty exposure."
                ]
            }
        ]
    },
    {
        "id": "ch6",
        "title": "Chapter VI — Powers & Procedures of the Board",
        "sections": [
            {
                "num": "27", "title": "Powers of the Board", "risk": "medium",
                "desc": "Detailed powers including directing compliance, ordering data erasure, and imposing interim measures during investigations.",
                "steps": [
                    "Ensure the organisation has documented procedures for responding to Board orders.",
                    "Maintain legal counsel availability for urgent Board interactions."
                ]
            },
            {
                "num": "28", "title": "Procedure for Adjudication", "risk": "low",
                "desc": "Prescribes the procedural framework for how the Board hears and decides complaints.",
                "steps": ["Familiarise internal teams with the Board's adjudication procedure for preparedness."]
            }
        ]
    },
    {
        "id": "ch7",
        "title": "Chapter VII — Appeals & Alternate Dispute Resolution",
        "sections": [
            {
                "num": "29", "title": "Appeals to High Court", "risk": "medium",
                "desc": "Any person aggrieved by a Board order may appeal to the High Court within the prescribed timeframe.",
                "steps": [
                    "Confirm the organisation's legal team tracks all Board orders and assesses appeal viability.",
                    "Document timelines for appeal filing."
                ]
            },
            {
                "num": "30", "title": "Alternate Dispute Resolution", "risk": "low",
                "desc": "The Board may refer disputes to mediation or other ADR mechanisms before formal adjudication.",
                "steps": [
                    "Assess whether ADR might be a preferable resolution path for any pending disputes.",
                    "Include ADR preparedness in the legal team's training."
                ]
            }
        ]
    },
    {
        "id": "ch8",
        "title": "Chapter VIII — Penalties & Adjudication",
        "sections": [
            {
                "num": "31", "title": "Penalties — Schedule", "risk": "high",
                "desc": "Prescribes the penalty schedule: up to ₹250 crore for security failures, ₹200 crore for breach non-reporting or children's data violations, ₹50 crore for other non-compliance.",
                "steps": [
                    "Map all penalty categories to relevant organisational processes.",
                    "Conduct a gap analysis to identify which penalty-triggering areas have the highest risk.",
                    "Prioritise controls for security safeguards, breach reporting, and children's data."
                ]
            },
            {
                "num": "32", "title": "Adjudication of Penalties", "risk": "medium",
                "desc": "The Board may impose penalties after giving the Data Fiduciary a reasonable opportunity to be heard.",
                "steps": [
                    "Ensure the organisation can present a well-documented defence if a penalty proceeding is initiated.",
                    "Maintain records of all compliance actions taken as evidence."
                ]
            },
            {
                "num": "33", "title": "Recovery of Penalties", "risk": "medium",
                "desc": "Penalties imposed by the Board are recoverable as arrears of land revenue through the prescribed authority.",
                "steps": [
                    "Include potential penalty costs in the organisation's financial risk assessment.",
                    "Engage finance and treasury teams in understanding penalty implications."
                ]
            },
            {
                "num": "34", "title": "Compensation", "risk": "high",
                "desc": "Data Principals may seek compensation for harm suffered due to breach of the Act. The Board determines the quantum based on harm, gravity, and circumstances.",
                "steps": [
                    "Assess liability exposure for potential compensation claims.",
                    "Implement measures to minimise harm in case of any breach.",
                    "Ensure insurance coverage is reviewed with awareness of DPDP compensation provisions."
                ]
            }
        ]
    },
    {
        "id": "ch9",
        "title": "Chapter IX — Miscellaneous",
        "sections": [
            {
                "num": "35", "title": "Cross-Border Transfer of Personal Data", "risk": "high",
                "desc": "Data may be transferred abroad unless the Central Government blacklists a specific country. Higher-protection sectoral laws prevail where applicable.",
                "steps": [
                    "Map all cross-border data transfers and their destination countries.",
                    "Monitor the Central Government's blacklisted-country notifications.",
                    "Verify compliance with any stricter sectoral regulations applicable to specific data transfers."
                ]
            },
            {
                "num": "36", "title": "Obligations of Data Processor", "risk": "medium",
                "desc": "Data Processors must process data only as directed by the Data Fiduciary and are bound by the same security and confidentiality obligations.",
                "steps": [
                    "Audit all third-party Data Processor contracts for DPDP compliance clauses.",
                    "Verify Processors implement equivalent security safeguards.",
                    "Conduct periodic due-diligence assessments of critical Processors."
                ]
            },
            {
                "num": "37", "title": "Consent Manager", "risk": "medium",
                "desc": "A Consent Manager is a registered entity that acts as a single point of contact for a Data Principal to manage consent across multiple Data Fiduciaries.",
                "steps": [
                    "Assess whether the organisation should integrate with a registered Consent Manager.",
                    "If applicable, verify the Consent Manager's registration and operational compliance."
                ]
            },
            {
                "num": "38", "title": "Deemed Consent / Legitimate Use Details", "risk": "medium",
                "desc": "Provides further operational detail on how Legitimate Uses are documented and applied in practice.",
                "steps": [
                    "Ensure all Legitimate Use invocations are documented with specific references to the enumerated grounds.",
                    "Audit documentation completeness for all non-consent-based processing."
                ]
            },
            {
                "num": "39", "title": "Liability of Data Fiduciary for Processor Actions", "risk": "high",
                "desc": "The Data Fiduciary remains liable for the actions of its Data Processors unless the Processor has acted contrary to the Fiduciary's instructions.",
                "steps": [
                    "Review all Processor agreements to ensure clear instruction protocols.",
                    "Implement monitoring mechanisms for Processor compliance.",
                    "Maintain evidence of instructions given to Processors to establish due diligence."
                ]
            },
            {
                "num": "40", "title": "Power to Make Rules", "risk": "low",
                "desc": "Empowers the Central Government to frame rules under the Act — these are the DPDP Rules 2025, which operationalise the Act's provisions.",
                "steps": [
                    "Monitor DPDP Rules 2025 notifications for new obligations.",
                    "Update internal compliance frameworks as new rules come into force."
                ]
            },
            {
                "num": "41", "title": "Laying of Rules Before Parliament", "risk": "low",
                "desc": "Rules framed under the Act are to be laid before Parliament for scrutiny.",
                "steps": ["No direct organisational obligation — monitor parliamentary discussions for policy direction."]
            },
            {
                "num": "42", "title": "Penalties for Obstruction", "risk": "low",
                "desc": "Penalty for willfully obstructing any officer of the Board in the exercise of their powers or duties.",
                "steps": [
                    "Ensure all staff are trained on cooperating with Board officers during inspections.",
                    "Maintain a clear internal protocol for handling Board visits."
                ]
            },
            {
                "num": "43", "title": "Amendment of Act", "risk": "low",
                "desc": "Provides that the Act may be amended by Parliament as needed.",
                "steps": ["Monitor legislative amendments and update compliance plans accordingly."]
            },
            {
                "num": "44", "title": "Repeal and Savings", "risk": "low",
                "desc": "Upon full enforcement, Section 43A of the IT Act 2000 and associated IT Rules 2011 are repealed. Ongoing proceedings under repealed provisions continue under the new Act.",
                "steps": [
                    "Verify that legacy IT Act 43A compliance processes are transitioned to DPDP Act frameworks.",
                    "Confirm all pending proceedings under old rules are tracked and handled under the new Act."
                ]
            }
        ]
    }
]

# ─── SESSION STATE INIT ──────────────────────────────────────────
def init_session():
    if "checked" not in st.session_state:
        st.session_state.checked = {}
    for ch in CHAPTERS:
        for sec in ch["sections"]:
            key = f"{ch['id']}-{sec['num']}"
            if key not in st.session_state.checked:
                st.session_state.checked[key] = False

init_session()


# ─── HELPERS ─────────────────────────────────────────────────────
def risk_badge(risk: str) -> str:
    icons = {"high": "🔴", "medium": "🟡", "low": "🟢"}
    return f"{icons.get(risk,'')} {risk.capitalize()} Risk"


def get_stats():
    total = sum(len(ch["sections"]) for ch in CHAPTERS)
    done = sum(1 for v in st.session_state.checked.values() if v)
    return total, done, total - done


# ─── LOGO SVG (inline) ───────────────────────────────────────────
LOGO_SVG = """
<svg width="56" height="56" viewBox="0 0 54 54" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="sg" x1="0" y1="0" x2="54" y2="54">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#fcd34d"/>
    </linearGradient>
  </defs>
  <path d="M27 3L6 13v18c0 11.5 9 22 21 25 12-3 21-13.5 21-25V13L27 3z" stroke="url(#sg)" stroke-width="2.5" stroke-linejoin="round" fill="none"/>
  <rect x="20" y="27" width="14" height="11" rx="2.5" fill="#f59e0b"/>
  <path d="M22 27v-4a5 5 0 0110 0v4" stroke="#f59e0b" stroke-width="2.5" stroke-linecap="round" fill="none"/>
  <circle cx="27" cy="33" r="1.6" fill="#0f1b2d"/>
  <circle cx="12" cy="17" r="2" fill="#3b82f6" opacity="0.7"/>
  <circle cx="42" cy="17" r="2" fill="#10b981" opacity="0.7"/>
  <circle cx="27" cy="8" r="1.5" fill="#fcd34d" opacity="0.9"/>
</svg>
"""


# ─── RENDER APP ──────────────────────────────────────────────────
def main():
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

    # ── HEADER ──
    total, done, pending = get_stats()
    pct = round((done / total) * 100, 1) if total else 0

    st.markdown(f"""
    <div class="dpdp-header">
      <div class="logo-circle">{LOGO_SVG}</div>
      <div>
        <h1 style="margin:0; font-family:'Playfair Display',serif; color:#fff; font-size:1.6rem;">🛡️ DataShield Audit</h1>
        <div class="sub">DPDP Act 2023 — Internal Compliance Audit Tool</div>
      </div>
      <div style="margin-left:auto; display:flex; gap:32px; text-align:center;">
        <div><div style="color:#fff; font-size:1.4rem; font-weight:600;">{total}</div><div style="color:#94a3b8; font-size:0.62rem; text-transform:uppercase; letter-spacing:1.5px;">Sections</div></div>
        <div><div style="color:#10b981; font-size:1.4rem; font-weight:600;">{done}</div><div style="color:#94a3b8; font-size:0.62rem; text-transform:uppercase; letter-spacing:1.5px;">Completed</div></div>
        <div><div style="color:#f59e0b; font-size:1.4rem; font-weight:600;">{pending}</div><div style="color:#94a3b8; font-size:0.62rem; text-transform:uppercase; letter-spacing:1.5px;">Pending</div></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── GLOBAL PROGRESS ──
    col_prog, col_pct = st.columns([5, 1])
    with col_prog:
        st.progress(done / total if total else 0)
    with col_pct:
        st.markdown(f"<div style='text-align:right; font-weight:600; color:#1e293b; padding-top:4px;'>{pct}% Complete</div>", unsafe_allow_html=True)

    # ── INFO BOX ──
    st.info(
        "**DPDP Act 2023 — Internal Audit Checklist**\n\n"
        "This tool covers all 44 sections across 9 chapters. Expand each chapter, review the audit procedure, "
        "and tick off completed items. Full compliance deadline: **13 May 2027**."
    )

    # ── ACTION BUTTONS ──
    col_a, col_b, _ = st.columns([1.2, 1.2, 4])
    with col_a:
        if st.button("↺ Reset All", type="secondary", use_container_width=True):
            for key in st.session_state.checked:
                st.session_state.checked[key] = False
            st.rerun()
    with col_b:
        # Download a simple text report
        lines = [f"DPDP Act 2023 — Audit Report | Generated: {datetime.now().strftime('%d %b %Y %H:%M')}", "=" * 70]
        for ch in CHAPTERS:
            lines.append(f"\n{ch['title']}")
            lines.append("-" * 50)
            for sec in ch["sections"]:
                key = f"{ch['id']}-{sec['num']}"
                status = "✅ DONE" if st.session_state.checked.get(key) else "⬜ PENDING"
                lines.append(f"  [{status}] § {sec['num']} — {sec['title']}  ({sec['risk'].upper()} RISK)")
        report_text = "\n".join(lines)
        st.download_button("⬇ Export Report", data=report_text, file_name="DPDP_Audit_Report.txt", mime="text/plain", use_container_width=True)

    st.markdown("---")

    # ── CHAPTERS & SECTIONS ──
    for ch in CHAPTERS:
        ch_sections = ch["sections"]
        ch_done = sum(1 for s in ch_sections if st.session_state.checked.get(f"{ch['id']}-{s['num']}"))
        ch_total = len(ch_sections)
        ch_pct = round((ch_done / ch_total) * 100) if ch_total else 0
        ch_all_done = ch_done == ch_total

        # Chapter header label
        badge_color = "#10b981" if ch_all_done else "#f59e0b"
        header_label = (
            f"<span style='color:{badge_color}; font-weight:700;'>[{ch_done}/{ch_total}]</span> "
            f"<strong>{ch['title']}</strong> "
            f"<span style='font-size:0.75rem; color:#94a3b8;'>— {ch_pct}% complete</span>"
        )

        with st.expander(ch["title"], expanded=False):
            # Chapter-level "select all" toggle
            col_sel, col_prog2 = st.columns([2, 3])
            with col_sel:
                toggle_val = st.checkbox(
                    f"**Mark all {ch_total} sections as complete**",
                    value=ch_all_done,
                    key=f"toggle_all_{ch['id']}"
                )
                # If toggled, apply to all sections in chapter
                if toggle_val != ch_all_done:
                    for s in ch_sections:
                        st.session_state.checked[f"{ch['id']}-{s['num']}"] = toggle_val
                    st.rerun()
            with col_prog2:
                st.progress(ch_done / ch_total if ch_total else 0, text=f"{ch_pct}%")

            st.divider()

            # ── Individual Sections ──
            for sec in ch_sections:
                key = f"{ch['id']}-{sec['num']}"
                is_checked = st.session_state.checked.get(key, False)
                risk_label = risk_badge(sec["risk"])

                # Row: checkbox + section expander
                col_cb, col_sec = st.columns([0.35, 8])

                with col_cb:
                    new_val = st.checkbox("", value=is_checked, key=f"cb_{key}")
                    if new_val != is_checked:
                        st.session_state.checked[key] = new_val
                        st.rerun()

                with col_sec:
                    sec_label = f"**§ {sec['num']} — {sec['title']}**  {risk_label}"
                    with st.expander(sec_label, expanded=False):
                        # Overview
                        st.markdown(f"<div class='sec-detail-box'>"
                                    f"<div class='det-label'>📄 Section Overview</div>"
                                    f"<div class='det-text'>{sec['desc']}</div>"
                                    f"<div class='det-label'>✅ Audit Procedure</div>",
                                    unsafe_allow_html=True)

                        for i, step in enumerate(sec["steps"], 1):
                            st.markdown(
                                f'<div class="audit-step-row">'
                                f'<div class="step-circle">{i}</div>'
                                f'<div class="step-text">{step}</div>'
                                f'</div>',
                                unsafe_allow_html=True
                            )

                        st.markdown("</div>", unsafe_allow_html=True)

    # ── SUMMARY TABLE ──
    st.markdown("---")
    st.subheader("📊 Compliance Summary by Chapter")

    summary_data = []
    for ch in CHAPTERS:
        ch_done = sum(1 for s in ch["sections"] if st.session_state.checked.get(f"{ch['id']}-{s['num']}"))
        ch_total = len(ch["sections"])
        high_risk = sum(1 for s in ch["sections"] if s["risk"] == "high")
        high_done = sum(1 for s in ch["sections"] if s["risk"] == "high" and st.session_state.checked.get(f"{ch['id']}-{s['num']}"))
        summary_data.append({
            "Chapter": ch["title"],
            "Total Sections": ch_total,
            "Completed": ch_done,
            "Pending": ch_total - ch_done,
            "High-Risk Sections": high_risk,
            "High-Risk Done": high_done,
            "Progress (%)": round((ch_done / ch_total) * 100) if ch_total else 0
        })

    import pandas as pd
    df = pd.DataFrame(summary_data)
    st.dataframe(df, use_container_width=True, hide_index=True)

    # ── FOOTER ──
    st.markdown(f"""
    <div class="dpdp-footer">
      <div class="f-left">
        <div class="f-title">🛡️ © 2025 DataShield Audit Tool</div>
        <div class="f-copy">All rights reserved. For internal use only. Not for distribution.</div>
      </div>
      <div class="f-right">
        Built for compliance with the <span>Digital Personal Data Protection Act, 2023</span><br/>
        Reference: MeitY Gazette Notification &nbsp;|&nbsp; Act No. 22 of 2023<br/>
        <span style="opacity:0.5;">Version 1.0 &nbsp;|&nbsp; January 2025</span>
      </div>
    </div>
    """, unsafe_allow_html=True)


# ─── RUN ─────────────────────────────────────────────────────────
if __name__ == "__main__":
    main()

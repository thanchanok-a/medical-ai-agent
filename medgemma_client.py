import os
import anthropic
from dotenv import load_dotenv

load_dotenv()

MEDICAL_SYSTEM_PROMPT = """You are a clinical AI assistant specialized in 
medical text analysis. Extract and summarize clinical information precisely 
using appropriate medical terminology. Do NOT explain in plain English — 
that is handled by a separate communication layer."""

def analyze_medical_text(report_text: str) -> str:
    """Medical analysis layer — extracts clinical information."""
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=600,
        system=MEDICAL_SYSTEM_PROMPT,
        messages=[{
            "role": "user",
            "content": f"""Analyze this medical report and provide:
1. Key clinical findings (bullet points, clinical language)
2. Identified conditions/diagnoses
3. Medications and dosages
4. Lab values — note if normal or abnormal
5. Clinical severity: Mild / Moderate / Severe / Critical

Report:
---
{report_text}
---"""
        }]
    )
    return message.content[0].text


def medical_qa(report_text: str, question: str) -> str:
    """Clinical Q&A layer."""
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=300,
        system=MEDICAL_SYSTEM_PROMPT,
        messages=[{
            "role": "user",
            "content": f"""Answer this clinical question based only on
what is documented in the report.

Report:
---
{report_text}
---

Question: {question}"""
        }]
    )
    return message.content[0].text


if __name__ == "__main__":
    sample = """
    Patient: Jane Smith, 65F
    Medications: Metformin 1000mg BID, Lisinopril 10mg QD
    Vitals: BP 158/94, HR 88, O2 sat 94%
    Assessment: Heart failure with preserved ejection fraction (HFpEF)
    Plan: Start Furosemide 20mg daily, follow up in 2 weeks
    """
    print("Running medical analysis layer...")
    result = analyze_medical_text(sample)
    print("\nClinical Analysis:")
    print(result)
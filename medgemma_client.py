# medgemma_client.py
#
# ARCHITECTURE NOTE:
# In production this layer would call the MedGemma API directly.
# In this prototype it uses Claude with a clinical system prompt
# as a substitute, because MedGemma requires a CUDA GPU not
# available in the local MacBook or Streamlit Cloud environment.
#
# Real MedGemma 4B inference is demonstrated in:
# → medgemma_colab_comparison.ipynb (Google Colab, Tesla T4 GPU)
#
# To swap in real MedGemma: replace the anthropic.Anthropic() call
# below with a HuggingFace Inference Endpoint call. Nothing else changes.

import os
import anthropic
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

MEDICAL_SYSTEM_PROMPT = """You are a clinical AI assistant specialized in
medical text analysis. Extract and summarize clinical information precisely
using appropriate medical terminology. Do NOT explain in plain English —
that is handled by a separate communication layer."""


def get_api_key():
    """
    Get Anthropic API key.
    Works in both environments:
    - Locally (VS Code): reads from .env file
    - Streamlit Cloud: reads from st.secrets
    """
    try:
        key = st.secrets.get("ANTHROPIC_API_KEY")
        if key:
            return key
    except Exception:
        pass

    key = os.getenv("ANTHROPIC_API_KEY")
    if not key:
        raise ValueError(
            "ANTHROPIC_API_KEY not found. "
            "Add it to .env (local) or Streamlit secrets (cloud)."
        )
    return key


def analyze_medical_text(report_text: str) -> str:
    """Medical analysis layer — extracts clinical information."""
    client = anthropic.Anthropic(api_key=get_api_key())
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
    client = anthropic.Anthropic(api_key=get_api_key())
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
    # Use real synthetic reports instead of placeholder patient
    from synthetic_reports import REPORTS

    # Print available keys so you can always check
    print("Available report keys:")
    for key in REPORTS.keys():
        print(f"  - {key}")
    print()

    # Test on the chest X-ray — the most interesting case
    # Use next() to find the key safely instead of hardcoding
    chest_key = next(
        (k for k in REPORTS if "chest" in k.lower() or "xray" in k.lower()),
        None
    )

    if chest_key:
        test_report = REPORTS[chest_key]["text"]
        expected    = REPORTS[chest_key]["urgency_true"]

        print(f"Testing: {chest_key}  |  Expected urgency: {expected}")
        print("-" * 50)

        result = analyze_medical_text(test_report)
        print("\nClinical Analysis:")
        print(result)

        print("\n" + "-" * 50)
        qa_result = medical_qa(
            test_report,
            "Is this patient's condition serious? What should they do right now?"
        )
        print("\nQ&A Test:")
        print(qa_result)
    else:
        print("chest_xray report not found — available keys printed above.")
        print("Update the key name in __main__ to match one from the list.")
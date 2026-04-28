# prompts.py

CLAUDE_SYSTEM_PROMPT = """You are a medical AI assistant that helps patients and 
caregivers understand medical reports. You receive a medical report and an analysis 
from MedGemma (a specialized medical AI), then translate both into clear, 
compassionate, plain English.

CRITICAL RULES:
- You are an AI assistant, NOT a doctor
- Never provide medical diagnoses or treatment recommendations  
- Always recommend consulting a qualified healthcare provider
- Frame everything as educational information only
- Be empathetic and avoid alarming language unnecessarily
"""

EXPLAIN_TEMPLATE = """I have a medical report analyzed by MedGemma (a specialized 
medical AI). Please help explain it to a patient in plain English.

ORIGINAL REPORT:
{report_text}

MEDGEMMA'S CLINICAL ANALYSIS:
{medgemma_analysis}

Please provide:
1. **Plain-English Summary** (2-3 sentences a non-medical person can understand)
2. **What This Means For You** (key points the patient should know)
3. **Medical Terms Explained** (define any jargon from the report)
4. **Urgency Level**: Low / Moderate / High — with a one-sentence reason
5. **Questions to Ask Your Doctor** (3 specific, useful questions)

Remember: educational information only, not medical advice."""

PATIENT_QA_TEMPLATE = """A patient has a follow-up question about their medical report.

ORIGINAL REPORT:
{report_text}

MEDGEMMA'S CLINICAL ANSWER:
{medgemma_answer}

PATIENT'S QUESTION:
{question}

Please answer in clear, compassionate plain English. If you cannot answer 
confidently from the available information, say so and suggest they ask 
their doctor."""
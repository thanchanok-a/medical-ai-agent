# claude_agent.py
import anthropic
import os
from dotenv import load_dotenv
from prompts import CLAUDE_SYSTEM_PROMPT, EXPLAIN_TEMPLATE, PATIENT_QA_TEMPLATE
from mcp_tools import python_exec_tool_run_medgemma, python_exec_tool_run_medgemma_qa

load_dotenv()

def get_claude_client():
    key = os.getenv("ANTHROPIC_API_KEY")
    if not key:
        raise ValueError("ANTHROPIC_API_KEY not found in .env")
    return anthropic.Anthropic(api_key=key)

def full_pipeline_explain(report_text: str) -> dict:
    """Full pipeline: Clinical analysis → Claude patient explanation."""
    
    # Step 1: MCP python_exec_tool triggers clinical analysis
    print("  [MCP] python_exec_tool → running clinical analysis...")
    clinical_analysis = python_exec_tool_run_medgemma(report_text)
    
    # Step 2: MCP filesystem_tool passes context to Claude
    print("  [MCP] filesystem_tool → passing context to Claude...")
    client = get_claude_client()
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system=CLAUDE_SYSTEM_PROMPT,
        messages=[{
            "role": "user",
            "content": EXPLAIN_TEMPLATE.format(
                report_text=report_text,
                medgemma_analysis=clinical_analysis
            )
        }]
    )
    
    return {
        "medgemma_analysis": clinical_analysis,
        "claude_explanation": message.content[0].text
    }

def full_pipeline_qa(report_text: str, question: str) -> dict:
    """Full Q&A pipeline: Clinical answer → Claude patient answer."""
    
    print("  [MCP] python_exec_tool → running clinical Q&A...")
    clinical_answer = python_exec_tool_run_medgemma_qa(report_text, question)
    
    print("  [MCP] passing answer to Claude...")
    client = get_claude_client()
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=512,
        system=CLAUDE_SYSTEM_PROMPT,
        messages=[{
            "role": "user",
            "content": PATIENT_QA_TEMPLATE.format(
                report_text=report_text,
                medgemma_answer=clinical_answer,
                question=question
            )
        }]
    )
    
    return {
        "medgemma_answer": clinical_answer,
        "claude_explanation": message.content[0].text
    }

# Test when run directly
if __name__ == "__main__":
    sample = """
    Patient: John Doe, 58M
    Dx: Type 2 DM, HTN
    Meds: Metformin 500mg BID, Lisinopril 10mg QD
    Labs: HbA1c 7.8%, BP 145/90
    Assessment: Suboptimal glycemic control
    Plan: Increase Metformin to 1000mg BID. Follow up 3 months.
    """

    print("Running full pipeline...\n")
    result = full_pipeline_explain(sample)

    print("\n=== Clinical Analysis ===")
    print(result["medgemma_analysis"])
    print("\n=== Claude Patient Explanation ===")
    print(result["claude_explanation"])
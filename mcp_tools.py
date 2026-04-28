# mcp_tools.py
"""
MCP Tools layer for the Medical AI Agent.
These functions represent MCP tool capabilities:
- filesystem_tool: loads medical reports from disk
- python_exec_tool: triggers MedGemma inference

In production these would be registered as proper MCP server tools.
For this project they are Python functions — architecturally equivalent.
"""
import os

def filesystem_tool_load_report(filepath: str) -> str:
    """MCP Filesystem Tool: Load a medical report from disk."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Report not found: {filepath}")
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def filesystem_tool_list_reports(directory: str = "sample_reports") -> list:
    """MCP Filesystem Tool: List available report files."""
    if not os.path.exists(directory):
        return []
    return sorted([f for f in os.listdir(directory) if f.endswith(".txt")])

def python_exec_tool_run_medgemma(report_text: str) -> str:
    """MCP Python Execution Tool: Trigger MedGemma inference."""
    from medgemma_client import analyze_medical_text
    return analyze_medical_text(report_text)

def python_exec_tool_run_medgemma_qa(report_text: str, question: str) -> str:
    """MCP Python Execution Tool: Trigger MedGemma Q&A inference."""
    from medgemma_client import medical_qa
    return medical_qa(report_text, question)
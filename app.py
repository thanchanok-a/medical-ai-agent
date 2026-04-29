# app.py — Medical AI Explanation Agent
# Streamlit web application with 20 synthetic reports

import streamlit as st
from claude_agent import full_pipeline_explain, full_pipeline_qa
from mcp_tools import filesystem_tool_list_reports, filesystem_tool_load_report
from synthetic_reports import REPORTS

# ── Page Config ───────────────────────────────────────────────
st.set_page_config(
    page_title="Medical AI Explanation Agent",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Custom CSS ────────────────────────────────────────────────
st.markdown("""
<style>
    .urgency-high     { background:#FDECEA; border-left:5px solid #C0392B;
                        padding:12px; border-radius:4px; margin:8px 0; }
    .urgency-moderate { background:#FEF9E7; border-left:5px solid #D97706;
                        padding:12px; border-radius:4px; margin:8px 0; }
    .urgency-low      { background:#EAFAF1; border-left:5px solid #1A7A4A;
                        padding:12px; border-radius:4px; margin:8px 0; }
    .disclaimer       { background:#F8F9FA; border:1px solid #DEE2E6;
                        padding:10px; border-radius:4px; font-size:0.85em;
                        color:#6C757D; margin-top:12px; }
</style>
""", unsafe_allow_html=True)

# ── Build Report Lookups ──────────────────────────────────────
# Display label → report text
SAMPLE_REPORTS = {}
# Display label → full metadata dict
REPORT_METADATA = {}

for report_id, data in REPORTS.items():
    label = f"{data['domain']} — {data['urgency_true']}"
    SAMPLE_REPORTS[label]  = data["text"]
    REPORT_METADATA[label] = data

# ── Session State Init ────────────────────────────────────────
if "report_text"  not in st.session_state:
    st.session_state.report_text = ""
if "last_analysis" not in st.session_state:
    st.session_state.last_analysis = None

# ══════════════════════════════════════════════════════════════
# SIDEBAR
# ══════════════════════════════════════════════════════════════
with st.sidebar:
    st.title("🧬 Medical AI Agent")
    st.caption("MedGemma Impact Challenge · Grad AI Class")
    st.divider()

    # ── Urgency filter ────────────────────────────────────────
    st.subheader("📋 Sample Reports")
    st.caption(f"{len(REPORTS)} synthetic reports · 12 clinical domains")

    urgency_filter = st.radio(
        "Filter by urgency level",
        ["All 20", "🟢 Low (7)", "🟡 Moderate (7)", "🔴 High (6)"],
        index=0
    )

    # Build filtered dropdown
    filter_map = {
        "All 20":        None,
        "🟢 Low (7)":    "Low",
        "🟡 Moderate (7)": "Moderate",
        "🔴 High (6)":   "High",
    }
    selected_urgency = filter_map[urgency_filter]

    if selected_urgency:
        filtered_reports = {
            k: v for k, v in SAMPLE_REPORTS.items()
            if selected_urgency in k
        }
    else:
        filtered_reports = SAMPLE_REPORTS

    selected_label = st.selectbox(
        "Select a report",
        options=list(filtered_reports.keys()),
        index=0
    )

    # Show metadata preview
    if selected_label:
        meta = REPORT_METADATA[selected_label]
        st.caption(
            f"**Domain:** {meta['domain']}  \n"
            f"**Words:** {meta['word_count']}  \n"
            f"**Has labs:** {'Yes' if meta['has_lab_values'] else 'No'}  \n"
            f"**Has meds:** {'Yes' if meta['has_medications'] else 'No'}"
        )

    if st.button("📂 Load This Report", use_container_width=True, type="primary"):
        st.session_state.report_text = filtered_reports[selected_label]
        st.session_state.last_analysis = None
        st.success("Report loaded ✓")

    st.divider()

    # ── Ethics notice ─────────────────────────────────────────
    st.markdown("""
    <div class='disclaimer'>
    ⚠️ <strong>Research Prototype Only</strong><br>
    All sample reports are entirely fictional.
    This is NOT medical advice. Not for clinical use.
    </div>
    """, unsafe_allow_html=True)

    # ── Live app link ─────────────────────────────────────────
    st.divider()
    st.caption("🌐 Live App")
    st.markdown("[medical-ai-agent.streamlit.app]"
                "(https://medical-ai-agent-ayjwazwnbg4pfbaknekmzr.streamlit.app)")

# ══════════════════════════════════════════════════════════════
# MAIN AREA — 3 TABS
# ══════════════════════════════════════════════════════════════
st.title("Medical AI Explanation Agent")
st.caption("Two AIs. One Pipeline. Medical Reports in Plain English.")

tab1, tab2, tab3 = st.tabs([
    "📋 Report Explainer",
    "❓ Ask the Medical AI",
    "📊 About & Architecture"
])

# ──────────────────────────────────────────────────────────────
# TAB 1: REPORT EXPLAINER
# ──────────────────────────────────────────────────────────────
with tab1:
    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.subheader("Input")
        report_text = st.text_area(
            "Medical report text",
            value=st.session_state.report_text,
            height=280,
            placeholder="Paste a medical report here, or load a sample from the sidebar...",
            label_visibility="collapsed"
        )

        # Update session state when user types
        st.session_state.report_text = report_text

        analyze_btn = st.button(
            "🔍 Analyze Report",
            type="primary",
            use_container_width=True,
            disabled=not report_text.strip()
        )

    with col2:
        st.subheader("Results")

        if analyze_btn and report_text.strip():
            with st.spinner("Step 1: Running clinical analysis layer..."):
                try:
                    result = full_pipeline_explain(report_text)
                    st.session_state.last_analysis = result
                except Exception as e:
                    st.error(f"Error: {e}")
                    st.stop()

        if st.session_state.last_analysis:
            result = st.session_state.last_analysis
            explanation = result["claude_explanation"]
            text_lower  = explanation.lower()

            # Urgency indicator
            if any(w in text_lower for w in ["high", "urgent", "emergency",
                                              "immediately", "today"]):
                urgency, css = "🔴 HIGH", "urgency-high"
            elif "moderate" in text_lower or "soon" in text_lower:
                urgency, css = "🟡 MODERATE", "urgency-moderate"
            else:
                urgency, css = "🟢 LOW", "urgency-low"

            st.markdown(
                f"<div class='{css}'><strong>Urgency: {urgency}</strong></div>",
                unsafe_allow_html=True
            )

            st.markdown("**Patient-Friendly Explanation**")
            st.write(explanation)

            with st.expander("🧬 Clinical Analysis (MedGemma layer)"):
                st.text(result["medgemma_analysis"])

        else:
            st.info("Load a sample from the sidebar or paste a report, "
                    "then click Analyze Report.")

# ──────────────────────────────────────────────────────────────
# TAB 2: Q&A
# ──────────────────────────────────────────────────────────────
with tab2:
    st.subheader("Ask a Question About a Report")

    # Use whatever is loaded in session state
    qa_report = st.text_area(
        "Medical report (auto-filled from sidebar)",
        value=st.session_state.report_text,
        height=180,
        key="qa_report_input"
    )

    # Quick question buttons
    st.caption("Quick questions:")
    qcols = st.columns(4)
    quick_questions = [
        "Is this patient's condition serious?",
        "What do these lab values mean?",
        "What medications are mentioned?",
        "When should I see a doctor?",
    ]
    for i, (col, q) in enumerate(zip(qcols, quick_questions)):
        with col:
            if st.button(q, key=f"quick_{i}", use_container_width=True):
                st.session_state.question_text = q

    question = st.text_input(
        "Your question",
        value=st.session_state.get("question_text", ""),
        placeholder="Type your question here..."
    )
    st.session_state.question_text = question

    ask_btn = st.button(
        "Ask",
        type="primary",
        disabled=not (qa_report.strip() and question.strip())
    )

    if ask_btn and qa_report.strip() and question.strip():
        with st.spinner("Analyzing..."):
            try:
                result = full_pipeline_qa(qa_report, question)
                st.divider()
                st.markdown("**Answer (Patient-Friendly)**")
                st.write(result["claude_explanation"])
                with st.expander("🧬 Clinical Answer (MedGemma layer)"):
                    st.text(result["medgemma_answer"])
            except Exception as e:
                st.error(f"Error: {e}")

# ──────────────────────────────────────────────────────────────
# TAB 3: ABOUT
# ──────────────────────────────────────────────────────────────
with tab3:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Architecture")
        st.markdown("""
        **Two-layer AI pipeline:**

        1. **MCP filesystem_tool** — loads report from disk
        2. **MCP python_exec_tool** — triggers clinical analysis
        3. **Clinical layer** (`medgemma_client.py`)
           - Uses Claude with `MEDICAL_SYSTEM_PROMPT`
           - Writes like a doctor: ICD codes, clinical shorthand
           - Substitute for MedGemma API (requires GPU)
        4. **Communication layer** (`claude_agent.py`)
           - Uses Claude with `CLAUDE_SYSTEM_PROMPT`
           - Translates clinical output to plain English
           - Adds urgency framing and patient action steps
        5. **Streamlit UI** — displays results to patient

        **Real MedGemma 4B** inference demonstrated separately in
        Google Colab (Tesla T4 GPU, 15.6 GB VRAM).
        """)

    with col2:
        st.subheader("Dataset")
        st.markdown(f"""
        **{len(REPORTS)} synthetic reports** across 12 clinical domains:
        """)

        # Show breakdown table
        from collections import Counter
        urgency_counts = Counter(d["urgency_true"] for d in REPORTS.values())
        domain_counts  = Counter(d["domain"] for d in REPORTS.values())

        st.markdown(f"""
        | Urgency | Count |
        |---------|-------|
        | 🟢 Low     | {urgency_counts['Low']} |
        | 🟡 Moderate | {urgency_counts['Moderate']} |
        | 🔴 High    | {urgency_counts['High']} |
        """)

        st.caption("All reports are entirely fictional — for research only.")

        st.subheader("Ethics")
        st.markdown("""
        ⚠️ **NOT medical advice.** Research prototype only.
        All sample reports are fictional. Real deployment would require
        HIPAA compliance, clinician validation, and fairness evaluation.
        """)

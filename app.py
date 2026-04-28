import streamlit as st
from claude_agent import full_pipeline_explain, full_pipeline_qa
from mcp_tools import filesystem_tool_load_report, filesystem_tool_list_reports

st.set_page_config(
    page_title="Medical AI Explanation Agent",
    page_icon="🏥",
    layout="wide"
)

def main():
    st.title("🏥 Medical AI Explanation Agent")
    st.markdown("**Powered by MedGemma + Claude | MedGemma Impact Challenge**")
    st.warning(
        "⚠️ Educational purposes only. This tool does not provide medical advice. "
        "Always consult a qualified healthcare provider."
    )

    # Sidebar
    with st.sidebar:
        st.header("📂 Sample Reports")
        reports = filesystem_tool_list_reports()
        if reports:
            selected = st.selectbox(
                "Load a sample:",
                ["(paste your own)"] + reports
            )
            if selected != "(paste your own)":
                if st.button("📄 Load Report"):
                    text = filesystem_tool_load_report(f"sample_reports/{selected}")
                    st.session_state["report_text"] = text
                    st.success(f"Loaded: {selected}")

        st.divider()
        st.header("ℹ️ How It Works")
        st.markdown("""
        1. **Clinical Layer** analyzes medical content
        2. **Claude** translates into patient-friendly language
        3. **MCP Tools** connect the pipeline
        """)

    # Main layout
    col1, col2 = st.columns([1, 1])

    with col1:
        st.header("📋 Medical Report Input")
        report_text = st.text_area(
            "Paste a medical report here:",
            value=st.session_state.get("report_text", ""),
            height=300,
            placeholder="Paste medical text here..."
        )

        analyze_btn = st.button(
            "🔬 Analyze Report",
            type="primary",
            use_container_width=True
        )

    with col2:
        st.header("🤖 AI Analysis")

        if analyze_btn:
            if not report_text.strip():
                st.error("Please paste a medical report first.")
            else:
                st.session_state["current_report"] = report_text

                with st.status("Running pipeline...", expanded=True) as status:
                    st.write("🧬 Step 1: Clinical analysis layer (MCP tool)...")
                    try:
                        result = full_pipeline_explain(report_text)
                        st.write("✅ Clinical analysis complete")
                        st.write("💬 Step 2: Claude translating for patient...")
                        st.write("✅ Explanation ready")
                        status.update(
                            label="✅ Analysis complete!",
                            state="complete"
                        )
                        st.session_state["last_result"] = result
                    except Exception as e:
                        status.update(label="❌ Error", state="error")
                        st.error(f"Error: {str(e)}")

        if "last_result" in st.session_state:
            result = st.session_state["last_result"]

            with st.expander("🧬 Clinical Analysis (Technical)", expanded=False):
                st.markdown(result["medgemma_analysis"])

            st.markdown("### 📖 Patient-Friendly Explanation")
            st.markdown(result["claude_explanation"])

    # Feature 2: Q&A
    if "current_report" in st.session_state:
        st.divider()
        st.header("💬 Ask the Medical AI")

        col3, col4 = st.columns([1, 1])

        with col3:
            question = st.text_input(
                "Ask a question about this report:",
                placeholder="e.g., Is this serious? What does HbA1c mean?"
            )
            ask_btn = st.button(
                "💬 Ask",
                use_container_width=True
            )

        with col4:
            if ask_btn and question:
                with st.spinner("Both AIs are thinking..."):
                    try:
                        qa_result = full_pipeline_qa(
                            st.session_state["current_report"],
                            question
                        )
                        with st.expander("🧬 Clinical Answer (Technical)"):
                            st.markdown(qa_result["medgemma_answer"])
                        st.markdown("**Patient-Friendly Answer:**")
                        st.markdown(qa_result["claude_explanation"])
                    except Exception as e:
                        st.error(f"Error: {str(e)}")

    # Feature 3: Urgency
    if "last_result" in st.session_state:
        st.divider()
        st.header("🚦 Decision Support")

        explanation = st.session_state["last_result"]["claude_explanation"]

        if "High" in explanation or "SEVERE" in explanation or "CRITICAL" in explanation:
            st.error("🔴 Urgency: HIGH — Seek medical attention soon")
        elif "Moderate" in explanation or "MODERATE" in explanation:
            st.warning("🟡 Urgency: MODERATE — Follow up with your doctor")
        else:
            st.success("🟢 Urgency: LOW — Routine follow-up recommended")

        st.caption(
            "⚠️ AI urgency assessment for educational purposes only. "
            "Call 911 for any medical emergency."
        )

if __name__ == "__main__":
    main()

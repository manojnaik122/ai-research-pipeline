import streamlit as st
from pipeline import run_research_pipeline

# Page Configuration
st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🔍",
    layout="wide"
)

# App Header
st.title("🔍 Multi-Agent Research Pipeline")
st.markdown("Powered by Search Agents, Web Scrapers, Writers, and Critics.")

# Sidebar for Input
with st.sidebar:
    st.header("Configuration")
    topic_input = st.text_input("Enter a research topic:", placeholder="e.g., Quantum Computing breakthroughs 2026")
    run_button = st.button("Run Research Pipeline", type="primary", use_container_width=True)

# Main Container for Output
if run_button:
    if not topic_input.strip():
        st.warning("Please enter a valid research topic.")
    else:
        # Create placeholders for live progress
        status_container = st.status("Initializing pipeline...", expanded=True)
        
        try:
            with status_container:
                st.write("Step 1: Search agent gathering initial information...")
                # We can run the pipeline directly since it prints to stdout, 
                # but to capture/display nicely in Streamlit, we call it here:
                result = run_research_pipeline(topic_input)
                st.update(label="Pipeline executed successfully!", state="complete", expanded=False)

            # Display Results in Tabs
            tab1, tab2, tab3, tab4 = st.tabs(["Final Report", "Critic Feedback", "Search Results", "Scraped Content"])

            with tab1:
                st.subheader("📝 Generated Research Report")
                st.markdown(result.get("report", "No report generated."))

            with tab2:
                st.subheader("⭐ Critic Review & Feedback")
                st.markdown(result.get("feedback", "No feedback generated."))

            with tab3:
                st.subheader("🌐 Initial Search Results")
                st.text(result.get("search_results", "No search results found."))

            with tab4:
                st.subheader("📄 Deep Scraped Content")
                st.text(result.get("scrape_content", "No content scraped."))

        except Exception as e:
            status_container.update(label="Pipeline failed!", state="error", expanded=True)
            st.error(f"An error occurred: {e}")
else:
    st.info("👈 Enter a topic in the sidebar and click **Run Research Pipeline** to get started.")
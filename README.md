# 🔍 Autonomous Multi-Agent Research Pipeline

An automated multi-agent research assistant built with **LangChain**, **Google Gemini**, and an interactive **Streamlit** user interface. This project orchestrates specialized AI agents to autonomously search, scrape, draft, and critically review research reports on any given topic.

---

## 🛠️ How It Works

The research pipeline delegates tasks across four distinct steps:
1. **Search Agent:** Queries and retrieves recent, reliable information from the web.
2. **Reader/Scraper Agent:** Selects the most relevant URL from search results and extracts deep content.
3. **Writer Agent:** Synthesizes the search results and scraped data into a well-structured, professional report.
4. **Critic Agent:** Reviews the final report strictly, evaluating its strengths, areas for improvement, and providing a final score out of 10.

---

## 🚀 Tech Stack

* **Python**
* **LangChain** (Runnables, Chat Prompts, Output Parsers)
* **Google Gemini API** (LLM backend)
* **Streamlit** (Interactive Web UI)

---

## 📂 Project Structure

```text
aimlproject1/
│
├── agent.py          # Defines the LLM prompts, chains, and agents
├── pipeline.py       # Orchestrates the 4-step multi-agent workflow
├── app.py            # Streamlit user interface
├── requirements.txt  # Project dependencies
└── README.md         # Project documentation

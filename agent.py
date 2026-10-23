from langchain.agents import create_agent
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from tools import web_search,scrap_url
from langchain_core.output_parsers import StrOutputParser
from langchain.chat_models import init_chat_model
gemini_base = init_chat_model(
    "gemini-3.6-flash",
    model_provider="google_genai"
)

model1 = init_chat_model(
    "openai/gpt-oss-20b",
    model_provider="groq"
)


gemini = gemini_base.bind(max_output_tokens=2048)
groq = model1.bind(max_tokens=2048)
def build_search_agent():
    return create_agent(model = gemini,
                        tools = [web_search])

def build_reader_agent():
    return create_agent(model = gemini,
                        tools=[scrap_url])

writer_prompt = ChatPromptTemplate.from_messages(
    [
    ("system", "You are an expert research writer. Write clear, structured and insightful reports."),
    ("human", """Write a detailed research report on the topic below.

Topic: {topic}

Research Gathered:
{research}

Structure the report as:
- Introduction
- Key Findings (minimum 3 well-explained points)
- Conclusion
- Sources (list all URLs found in the research)

Be detailed, factual and professional."""),
])

writer_chain = writer_prompt | gemini | StrOutputParser()
critic_prompt = ChatPromptTemplate.from_messages(
    [
("system", "You are a sharp and constructive research critic. Be honest and specific."),
("human","""Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
...""")
    ]
)

critic_chain = critic_prompt | gemini | StrOutputParser()



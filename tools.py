from langchain.tools import tool 
import requests 
from bs4 import BeautifulSoup 
import os 
from dotenv import load_dotenv 

load_dotenv() 

firecrawl = os.getenv("FIRECRAWL_API_KEY") 
openweather = os.getenv("OPENWEATHER_API_KEY") 

@tool 
def web_search(query: str) -> str: 
    """A tool that performs a web search using the api and returns the result in str format.""" 
    if not firecrawl: 
        return "Error: firecrawl api key is not set. please set the firecrawl api key in the .env file" 
    
    url = "https://api.firecrawl.dev/v2/search" 
    headers = { 
        "Authorization": f"bearer {firecrawl}", 
        "Content-type": "application/json" 
    } 
    payload = { 
        "query": query, 
        "limit": 5 
    } 
    try: 
        response = requests.post(url, headers=headers, json=payload, timeout=30) 
        response.raise_for_status()  # Check for HTTP errors (4xx/5xx)
           
        
        data = response.json()

        results = data.get("data", {}).get("web", [])
        out = []

        for r in results:
            out.append(
                f"Title: {r.get('title', 'N/A')}\n"
                f"URL: {r.get('url', 'N/A')}\n"
                f"Snippet: {r.get('description', '')[:300]}\n"
            )

        return "\n----\n".join(out)

    except requests.RequestException as e: 
        return f"firecrawl search failed : {e}" 


@tool
def scrap_url(url:str) -> str:
    """Scrape and return clean text content from a given URL for deeper reading."""
    try:
        resp=requests.get(url,timeout=8,headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.text,"html.parser")
        for tag in soup(["script","style","nav","footer"]):
            tag.decompose()

        return soup.get_text(separator=" ",strip = True)[:3000]

    except Exception as e:
        return f"Could not scrape URL: {str(e)}"


# google_scraper.py
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

def search_google(query, num_results=3):
    try:
        # Construct Google search URL
        url = f"https://www.google.com/search?q={quote(query)}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        
        # Fetch the page
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        # Parse HTML with BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extract search result snippets (adjust selector based on Google's current structure)
        results = []
        for g in soup.find_all("div", class_="tF2Cxc")[:num_results]:
            title = g.find("h3")
            snippet = g.find("div", class_="VwiC3b")
            if title and snippet:
                results.append(f"{title.text}: {snippet.text}")
        
        return results if results else ["No relevant results found."]
    
    except Exception as e:
        return [f"Error searching Google: {str(e)}"]

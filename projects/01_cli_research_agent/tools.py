
from ddgs import DDGS

def web_search(query: str, max_results: int = 5) -> list[dict]:
    """
    Search the web using DuckDuckGo.
    Returns a list of results with title, body and href.
    """
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=max_results)
    return results

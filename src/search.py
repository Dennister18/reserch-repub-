from duckduckgo_search import DDGS

def web_search(query: str, max_results: int = 5):
    with DDGS() as ddgs:
        results = []
        for r in ddgs.text(query, max_results=max_results):
            results.append({
                "title": r["title"],
                "url": r["href"],
                "snippet": r["body"]
            })
        return results

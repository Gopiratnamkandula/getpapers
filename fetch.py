import requests
from typing import List, Dict

def fetch_pubmed_articles(query: str, max_results: int = 20) -> List[Dict]:
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

    # Step 1: Get IDs
    search_url = f"{base_url}esearch.fcgi"
    search_params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "retmode": "json"
    }
    search_res = requests.get(search_url, params=search_params).json()
    ids = search_res.get("esearchresult", {}).get("idlist", [])

    if not ids:
        return []

    # Step 2: Get Details
    fetch_url = f"{base_url}esummary.fcgi"
    fetch_params = {
        "db": "pubmed",
        "id": ",".join(ids),
        "retmode": "json"
    }
    fetch_res = requests.get(fetch_url, params=fetch_params).json()
    result = fetch_res.get("result", {})

    papers = []
    for pid in ids:
        record = result.get(pid)
        if not record:
            continue
        papers.append({
            "title": record.get("title", ""),
            "authors": [a.get("name") for a in record.get("authors", [])],
            "source": record.get("source", ""),
            "pubdate": record.get("pubdate", "")
        })
    return papers

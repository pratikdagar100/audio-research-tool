import requests
import xml.etree.ElementTree as ET

HEADERS = {"User-Agent": "Mozilla/5.0"}

def arxiv_search(keyword):
    try:
        url = f"http://export.arxiv.org/api/query?search_query=all:{keyword.replace(' ','+')}&start=0&max_results=5"
        r = requests.get(url, headers=HEADERS, timeout=5)
        root = ET.fromstring(r.content)

        links = []
        for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
            link = entry.find("{http://www.w3.org/2005/Atom}id").text
            links.append(link)
            if len(links) == 3:
                break
        return links
    except:
        return []

def semantic_search(keyword):
    try:
        url = (
            "https://api.semanticscholar.org/graph/v1/paper/search"
            f"?query={keyword}&limit=5&fields=url,openAccessPdf,paperId"
        )
        data = requests.get(url, headers=HEADERS, timeout=5).json()

        links = []
        for p in data.get("data", []):
            if p.get("url"):
                links.append(p["url"])
            elif p.get("openAccessPdf") and p["openAccessPdf"].get("url"):
                links.append(p["openAccessPdf"]["url"])
            elif p.get("paperId"):
                links.append(f"https://www.semanticscholar.org/paper/{p['paperId']}")
            if len(links) == 3:
                break
        return links
    except:
        return []

def crossref_search(keyword):
    try:
        url = f"https://api.crossref.org/works?query={keyword}&rows=5"
        data = requests.get(url, headers=HEADERS, timeout=5).json()

        links = []
        for item in data["message"]["items"]:
            if "URL" in item:
                links.append(item["URL"])
            if len(links) == 3:
                break
        return links
    except:
        return []

def search_papers(keyword):

    # Try sources in order, no delay, no skip
    results = arxiv_search(keyword)

    if len(results) < 3:
        results += semantic_search(keyword)

    if len(results) < 3:
        results += crossref_search(keyword)

    # remove duplicates
    results = list(dict.fromkeys(results))

    # ensure exactly 3 (even if mixed sources)
    return results[:3] if results else ["No research papers found"]
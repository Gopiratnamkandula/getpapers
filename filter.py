from typing import List, Dict

def is_non_academic_author(authors: List[str]) -> bool:
    # Heuristic: if any author name lacks a university/hospital pattern, assume non-academic
    for author in authors:
        if author and not any(keyword in author.lower() for keyword in ["university", "institute", "college", "hospital"]):
            return True
    return False

def filter_papers(papers: List[Dict]) -> List[Dict]:
    return [paper for paper in papers if is_non_academic_author(paper["authors"])]

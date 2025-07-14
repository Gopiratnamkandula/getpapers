import csv
from typing import List, Dict

def write_to_csv(papers: List[Dict], filename: str) -> None:
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["title", "authors", "source", "pubdate"])
        writer.writeheader()
        for paper in papers:
            writer.writerow({
                "title": paper["title"],
                "authors": ", ".join(paper["authors"]),
                "source": paper["source"],
                "pubdate": paper["pubdate"]
            })

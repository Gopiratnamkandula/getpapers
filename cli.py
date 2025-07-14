import argparse
from getpapers.fetch import fetch_pubmed_articles
from getpapers.filter import filter_papers
from getpapers.utils import write_to_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed research papers and filter non-academic authors.")
    parser.add_argument("query", help="Search query for PubMed")
    parser.add_argument("--max", type=int, default=20, help="Maximum number of results")
    parser.add_argument("--csv", type=str, help="CSV output filename")

    args = parser.parse_args()

    print(f"Searching PubMed for: {args.query}")
    papers = fetch_pubmed_articles(args.query, args.max)
    print(f"Found {len(papers)} papers.")

    filtered = filter_papers(papers)
    print(f"{len(filtered)} papers have at least one non-academic author.")

    if args.csv:
        write_to_csv(filtered, args.csv)
        print(f"Results saved to {args.csv}")
    else:
        for paper in filtered:
            print(f"- {paper['title']} ({paper['pubdate']})")

if __name__ == "__main__":
    main()

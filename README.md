# getpapers

A Python command-line tool that searches research papers from **PubMed**, filters those with at least one **non-academic author**, and outputs results to **CSV** or prints them in the terminal.

---

## 📁 Code Structure
getpapers/
├── getpapers/
│ ├── init.py
│ ├── fetch.py # Logic to call PubMed API and retrieve paper data
│ ├── filter.py # Filters papers based on author affiliations
│ └── utils.py # Utility functions (e.g., CSV writing)
├── cli.py # Command-line interface entry point
├── pyproject.toml # Poetry configuration and dependencies
├── results.csv # Sample output
└── README.md # Documentation and usage

---

## 🚀 How to Run the Program

### 1️⃣ Install Python (version 3.10 or above)

Check version:

```bash
python --version
2️⃣ Install Dependencies
pip install requests
3️⃣ Run the Program
python cli.py "covid vaccine" --csv results.csv
🛠 Tools & Libraries Used
Python 3.10+

requests – for sending HTTP requests

Entrez E-utilities API – to fetch PubMed research data
(LLM) – used to plan, design, and debug this project
results.csv --- output

https://github.com/Gopiratnamkandula/getpapers 

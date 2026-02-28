"""
 Challenge: Scrape Wikipedia h2 Headers

Use the `requests` and `BeautifulSoup` libraries to fetch the Wikipedia page on Python (programming language).

Your task is to:
1. Download the HTML of the page.
2. Parse all `<h2>` section headers.
3. Store the clean header titles in a list.
4. Print the total count and display the first 10 section titles.

Bonus:
- Remove any trailing "[edit]" from the headers.
- Handle network errors gracefully.
"""

import requests
from bs4 import BeautifulSoup

URL = input("Enter the Wikipedia URL: ").strip()

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def get_h2_headers(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=20)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch page with {e} error!")
        return []
    
    soup =  BeautifulSoup(response.text,"html.parser")
    h2_tags = soup.find_all("h2")
    headers = []
    for h2 in h2_tags:
        header_text = h2.get_text().strip()
        clean_header = header_text.replace("[edit]", "").strip()
        headers.append(clean_header)
    return headers

headers = get_h2_headers(URL)
print(f"Total headers: {len(headers)}")
print("First 10 headers:")
for i, header in enumerate(headers[:10], 1):
    print(f"{i}. {header}")
"""
 Challenge: Download Cover Images of First 10 Books

Goal:
- Visit https://books.toscrape.com/
- Scrape the first 10 books listed on the homepage
- For each book, extract:
  • Title
  • Image URL

Then:
- Download each image
- Save it to a local `images/` folder with the filename as the book title (sanitized)

Example:
 Title: "A Light in the Attic"
 Saved as: images/A_Light_in_the_Attic.jpg

Bonus:
- Handle invalid filename characters
- Show download progress
"""

import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin
import os

URL = "https://books.toscrape.com/"
NEXT_PAGE_URL = "catalogue/page-1.html"
IMAGES = "images"
TARGETED_IMAGES = 15


def sanitize_title_for_filename(title):
    return re.sub(r'[^\w\-_. ]','',title).replace(" ","_")

def download_image(img_url,filename):
    try:
        response = requests.get(img_url, stream=True, timeout=10)
        response.raise_for_status()
        
        with open(filename,"wb") as file:
            for chunks in response.iter_content(1024):
                file.write(chunks)
        
    except requests.RequestException as e:
        print(f"Failed to download the {filename},Error {e}")
        return

def scrape_images():
    title_and_links = []
    current_url = urljoin(URL,NEXT_PAGE_URL)
    
    while(len(title_and_links)) < TARGETED_IMAGES and current_url:
        response = requests.get(current_url)
        soup = BeautifulSoup(response.text,"html.parser")
        
        books = soup.select("article.product_pod")
        for book in books:
            title = book.h3.a['title']
            relative_image_url = book.find("img")["src"]
            image_url = urljoin(current_url,relative_image_url)
            title_and_links.append((title,image_url))
            
        next_page_link = soup.select_one("li.next a")
        if next_page_link:
            current_url = urljoin(current_url,next_page_link['href'])
        else:
            current_url = None

def main():
    url = URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    books = soup.select("article.product_pod")[:TARGETED_IMAGES]
    
    if not os.path.exists(IMAGES):
        os.makedirs(IMAGES)
        
    for book in books:
        title = book.h3.a['title']
        relative_image_url = book.find("img")["src"]
        image_url = urljoin(url,relative_image_url)
        print(f"url - {image_url}")
        
        filename = sanitize_title_for_filename(title) + ".jpg"
        filepath = os.path.join(IMAGES,filename)
        print(f"filepath - {filepath}")
    
        print(f"Downloading.. {title}")
        download_image(image_url,filepath)
    
    print(f"All {TARGETED_IMAGES} books are covers downloaded to images")
    
    
    
if __name__ == "__main__":
    main()
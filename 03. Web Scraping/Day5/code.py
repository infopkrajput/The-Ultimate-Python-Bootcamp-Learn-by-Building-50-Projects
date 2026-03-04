"""
 Challenge: Download Cover Images Using wget

Goal:
- Scrape https://books.toscrape.com/
- Collect the first 10 books on the homepage
- Extract the title and image URL for each book
- Use the `wget` library to download and save images in a folder called 'images/'
- Use book titles (sanitized) as image filenames

Bonus:
- Add progress for each download
- Ensure folder is created if it doesn't exist
"""

import os
import wget
import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://books.toscrape.com/"
IMAGES_DIR = "images"
TARGET_IMAGES = 10

def sanitize_title_for_filename(title):
    return re.sub(r'[^\w\-_. ]','',title).replace(" ","_")

def scrape_images():
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text,"html.parser")
    books = soup.select("article.product_pod")[:TARGET_IMAGES]
    
    if not os.path.exists(IMAGES_DIR):
        os.makedirs(IMAGES_DIR)
    
    for book in books:
        title = book.h3.a['title']
        relative_image_url = book.find("img")["src"]
        image_url = urljoin(BASE_URL,relative_image_url)
        
        filename = sanitize_title_for_filename(title) + ".jpg"
        filepath = os.path.join(IMAGES_DIR,filename)
        
        print(f"Downloading: {title}")
        wget.download(image_url,filepath)
    
    print(f"All {TARGET_IMAGES} books are covers downloaded to images")
        
            
        
if __name__ == "__main__":
    scrape_images()
    
    
    
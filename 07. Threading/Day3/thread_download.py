import threading
import requests
import time

def download_file(url):
    print(f"Starting download from {url}...")
    response = requests.get(url)
    print(f"File downloaded successfully of size {len(response.content)} bytes.")
urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg",
    "https://httpbin.org/image/webp",
    "https://httpbin.org/image/gif"
]

star_time = time.time()

threads = []
for url in urls:
    thread = threading.Thread(target=download_file, args=(url,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

end_time = time.time()
print(f"All files downloaded in {end_time - star_time:.2f} seconds.")

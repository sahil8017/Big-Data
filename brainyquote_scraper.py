import requests
from bs4 import BeautifulSoup

url = "https://www.brainyquote.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

links = soup.find_all("a")

for link in links:
    text = link.text.strip()
    href = link.get("href")

    if href:
        print("Text:", text)
        print("Link:", href)
        print()
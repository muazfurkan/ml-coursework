import requests
from bs4 import BeautifulSoup


def find_urls(page_count):
  urls = []

  for _ in range(0, page_count):

    url = f"https://siir.sitesi.web.tr/siirler-{_ * 50}.html"

    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    anchors = soup.find_all("a")

    for anchor in anchors[15:-18]:
      urls.append(anchor['href'])

  return urls


def save_urls(url_list):
  with open("poems_urls.txt", "a") as file:
    for url in url_list:
      file.write(url + "\n")


save_urls(find_urls(110))

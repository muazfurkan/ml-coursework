import requests
from bs4 import BeautifulSoup
import pandas as pd


def find_lyrics(urls):
  urls_length = len(urls)
  lyrics = []

  for i, url in enumerate(urls):
    print(f"%{100 * (i + 1) / urls_length: .2f} tamamlandı.")

    response = requests.get(url)
    response.encoding = ('UTF-8')
    html = response.content

    soup = BeautifulSoup(html, 'html.parser')

    paragraphs = soup.find_all('p')

    for p in paragraphs:
      lines = p.find_all(string=True)
      for line in lines:
        line = line.strip()
        if line:
          lyrics.append(line)

  return lyrics


with open('poems_urls.txt', "r") as file:
  url_list = file.readlines()

lyrics_list = find_lyrics(url_list)

lyrics_series = pd.Series(lyrics_list)
lyric_df = pd.DataFrame({'Lyrics': lyrics_series})
lyric_df.to_excel('poem_lyrics.xlsx', index=False)

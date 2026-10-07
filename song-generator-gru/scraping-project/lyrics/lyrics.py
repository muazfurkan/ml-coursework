import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

def find_songs(urls):
  lyric_list = []
  j = 1
  len_list = len(urls)

  for url in urls:
    progress = 100 * j / len_list
    print(f"%{progress: .2f} tamamlandı. url: {url}")
    j = j + 1
    response = requests.get(url)

    if response.status_code == 200:
      html = response.text
    else:
      print('Sayfa alınamadı.')

    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find_all('div', {"class": "lyric-text margint20 marginb20"})

    sents = []
    sent = ""
    compound1 = ""
    compound2 = ""

    for div in divs:
      paragraph = div.text[:-25].split()

      for i, _word in enumerate(paragraph):
        if i <= len(paragraph) - 2:
          _word = _word.replace("I", "l")
          if _word.istitle():
            sent += _word + " "
          elif not _word.istitle() and not paragraph[i + 1].istitle():
            if _word.islower():
              sent += _word + " "
            else:
              for letter in _word:
                if letter.islower():
                  compound1 = compound1 + letter
                else:
                  compound2 = _word[len(compound1):]
                  break

              sent += compound1
              sents.append(sent)
              sent = ""
              sent += compound2
              compound1 = ""
              compound2 = ""

          elif not _word.istitle() and paragraph[i + 1].istitle():
            sent += _word + " "
            sents.append(sent)
            sent = ""

        else:
          sent += _word
          sents.append(sent)
          sent = ""

    lyric_list.append(sents)

  return lyric_list


file = "song_urls4.txt"

with open(file, "r") as file:
  url_list = file.readlines()

songs = find_songs(url_list)

lyrics_list = []

for song in songs:
    for lyrics in song:
        lyrics_list.append(lyrics)

lyrics_series = pd.Series(lyrics_list)

song_df = pd.DataFrame({'Lyrics': lyrics_series})
song_df.to_excel('lyrics-v5.xlsx', index=False)
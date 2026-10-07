import requests
from bs4 import BeautifulSoup


def find_song_names(url, singer):
  # url = 'https://www.sarkisozlerihd.com/sarkici/azer-bulbul/'
  response = requests.get(url)
  song_urls = []

  if response.status_code == 200:
    html = response.text
  else:
    print('Sayfa alınamadı.')

  soup = BeautifulSoup(html, 'html.parser')
  anchors = soup.find_all("a")

  for anchor in anchors:
    if singer in anchor["href"]:
      song_urls.append(anchor["href"])
    else:
      continue

  return song_urls


def save_urls(url_list):
  with open("song_urls3.txt", "a") as file:
    for url in url_list:
      file.write(url + "\n")


def main():
  urls = {
    # "muslum": "https://www.sarkisozlerihd.com/sarkici/muslum-gurses/",
    # "azer": "https://www.sarkisozlerihd.com/sarkici/azer-bulbul/",
    # "ferdi": "https://www.sarkisozlerihd.com/sarkici/ferdi-tayfur/",
    # "neset": "https://www.sarkisozlerihd.com/sarkici/neset-ertas/"
    # "adnan": "https://www.sarkisozlerihd.com/sarkici/adnan-senses/",
    # "ahmet": "https://www.sarkisozlerihd.com/sarkici/ahmet-safak/",
    # "ali": "https://www.sarkisozlerihd.com/sarkici/ali-kinik/",
    # "arap": "https://www.sarkisozlerihd.com/sarkici/arap-sukru/",
    # "candan": "https://www.sarkisozlerihd.com/sarkici/candan-ercetin/",
    # "cengiz": "https://www.sarkisozlerihd.com/sarkici/cengiz-ozkan/",
    # "ceylan": "https://www.sarkisozlerihd.com/sarkici/ceylan-ertem/",
    # "ebru": "https://www.sarkisozlerihd.com/sarkici/ebru-gundes/",
    # "erkan": "https://www.sarkisozlerihd.com/sarkici/erkan-ogur/",
    # "fatih": "https://www.sarkisozlerihd.com/sarkici/fatih-kisaparmak/",
    # "ferdi": "https://www.sarkisozlerihd.com/sarkici/ferdi-ozbegen/",
    # "ferhat": "https://www.sarkisozlerihd.com/sarkici/ferhat-gocer/",
    # "fettah": "https://www.sarkisozlerihd.com/sarkici/fettah-can/",
    # "funda": "https://www.sarkisozlerihd.com/sarkici/funda-arar/",
    # "gokhan": "https://www.sarkisozlerihd.com/sarkici/gokhan-tepe/",
    # "hakan": "https://www.sarkisozlerihd.com/sarkici/hakan-altun/",
    # "halil": "https://www.sarkisozlerihd.com/sarkici/halil-sezai/",
    # "haluk": "https://www.sarkisozlerihd.com/sarkici/haluk-levent/",
    # "erkal": "https://www.sarkisozlerihd.com/sarkici/ibrahim-erkal/",
    # "ibrahim": "https://www.sarkisozlerihd.com/sarkici/ibrahim-tatlises/",
    # "ilyas": "https://www.sarkisozlerihd.com/sarkici/ilyas-yalcintas/",
    # "intizar": "https://www.sarkisozlerihd.com/sarkici/intizar/",
    # "latif": "https://www.sarkisozlerihd.com/sarkici/latif-dogan/",
    # "mehmet": "https://www.sarkisozlerihd.com/sarkici/mehmet-erdem/",
    # "melike": "https://www.sarkisozlerihd.com/sarkici/melike-sahin/",
    # "merve": "https://www.sarkisozlerihd.com/sarkici/merve-ozbey/",
    # "mfo": "https://www.sarkisozlerihd.com/sarkici/mfo/",
    # "murat": "https://www.sarkisozlerihd.com/sarkici/murat-gogebakan/",
    # "musa": "https://www.sarkisozlerihd.com/sarkici/musa-eroglu/",
    # "mustafa": "https://www.sarkisozlerihd.com/sarkici/mustafa-ceceli/",
    # "sandal": "https://www.sarkisozlerihd.com/sarkici/mustafa-sandal/",
    # "nilufer": "https://www.sarkisozlerihd.com/sarkici/nilufer/",
    # "nurettin": "https://www.sarkisozlerihd.com/sarkici/nilufer/",
    # "oguzhan": "https://www.sarkisozlerihd.com/sarkici/oguzhan-koc/",
    # "onur": "https://www.sarkisozlerihd.com/sarkici/onur-can-ozcan/",
    # "orhan": "https://www.sarkisozlerihd.com/sarkici/orhan-gencebay/",
    # "oyku": "https://www.sarkisozlerihd.com/sarkici/oyku-gurman/",
    # "ozcan": "https://www.sarkisozlerihd.com/sarkici/ozcan-deniz/",
    # "pinhani": "https://www.sarkisozlerihd.com/sarkici/pinhani/",
    # "selami": "https://www.sarkisozlerihd.com/sarkici/selami-sahin/",
    # "serdar": "https://www.sarkisozlerihd.com/sarkici/serdar-ortac/",
    # "sertab": "https://www.sarkisozlerihd.com/sarkici/sertab-erener/",
    # "sibel": "https://www.sarkisozlerihd.com/sarkici/sibel-can/",
    # "sila": "https://www.sarkisozlerihd.com/sarkici/sila/",
    # "sura": "https://www.sarkisozlerihd.com/sarkici/sura-iskenderli/",
    # "tarkan": "https://www.sarkisozlerihd.com/sarkici/tarkan/",
    # "tugba": "https://www.sarkisozlerihd.com/sarkici/tugba-yurt/",
    # "umit": "https://www.sarkisozlerihd.com/sarkici/umit-besen/",
    # "yalin": "https://www.sarkisozlerihd.com/sarkici/yalin/",
    # "yavuz": "https://www.sarkisozlerihd.com/sarkici/yavuz-bingol/",
    # "zara": "https://www.sarkisozlerihd.com/sarkici/zara/",
    # "zeki": "https://www.sarkisozlerihd.com/sarkici/zeki-muren/",
    # "zerrin": "https://www.sarkisozlerihd.com/sarkici/zerrin-ozer/",
    # "zeynep": "https://www.sarkisozlerihd.com/sarkici/zeynep-bastik/"
  }

  for singer in urls:
    save_urls(find_song_names(urls[singer], singer))


if __name__ == "__main__":
  main()

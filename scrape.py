# pip install requests
# pip install beautifulsoup4
# pip install lxml
# pip install html5lib
import os
os.system('clear')

from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')
csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])
# article = soup.find_all('article')
for article in soup.find_all('article'):
  headline = article.h2.a.text
  summary = article.find('div',class_="entry-content").text

  try:
    youtube_link = article.find('iframe',class_= 'youtube-player')['src']
    vid_id = youtube_link.split('/')[4].split('?')[0]
    yt_link = f'https://youtube.com/watch?v={vid_id}' 
  except Exception as e:
    yt_link = "No Link Available"

  print(f'{headline.strip()}\n{summary.strip()}\n{yt_link.strip() }\n')
  csv_writer.writerow([headline, summary, yt_link])
csv_file.close() 
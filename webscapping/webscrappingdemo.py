import requests
from bs4 import BeautifulSoup

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/88.0.4324.182 Safari/537.36"}
data = requests.get("https://www.imdb.com/find/?s=ep&q=Thriller&ref_=nv_sr_sm",headers=headers)
soup = BeautifulSoup(data.content,
                     "html.parser")  # To get and understand the content of the webpage using html content.
# print(soup.prettify())

# find and findAll method
thriller_tv_table = soup.find('ul',{'class':'ipc-metadata-list ipc-metadata-list--dividers-after sc-e8e4ce7-3 dTEYDP ipc-metadata-list--base'})
# print(thriller_tv_table.prettify())
shows_lists = thriller_tv_table.findAll('li')
for shows in shows_lists:
    show_data = shows.findAll('ul')
    show_url = shows.find('a')
    for show in show_data:
        show_name = show_data[1]
        print(show_name.text)

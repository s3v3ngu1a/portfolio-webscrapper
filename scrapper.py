from bs4 import BeautifulSoup
# import requests

# website = "https://www.cadena3.com/pagina/buscador?q=argentina"
# result = requests.get(website)
# content = result.text

# print(content)

with open("content.html", encoding='utf-8') as fp:
    soup = BeautifulSoup(fp, features="html.parser")

links = soup.find_all('a')

for link in links:
    # print(type(link))
    # print(type(links))
    # print(type(link['href']))
    # print(link.get('href'))
    if "/noticia/" in link.get('href', ''):
        print(link.get('href'))


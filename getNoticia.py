import requests
from bs4 import BeautifulSoup

# url = "https://www.cadena3.com/noticia/futbol/la-historia-de-taty-castellanos-no-jugo-en-argentina-y-la-rompio-en-eeuu_356287"

# response = requests.get(url)

# response.encoding = 'UTF-8'

# print(response.text)

with open("noticia.html", encoding="utf-8") as fp:
    soup = BeautifulSoup(fp, from_encoding="utf-8", features="html.parser")

div_tag = soup.div

nota_elements = div_tag.find_all(id="cuerpo-nota")

print(nota_elements[0])

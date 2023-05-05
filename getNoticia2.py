# Este script extrae ya el contenido de la nota
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
'''
for nota_element in nota_elements:
    embebida_elements = nota_element.find_all(class_="nota-embebida")
    hide_elements = nota_element.find_all(class_="hide")

    for embebida_element in embebida_elements:
        embebida_element.decompose()
    for hide_element in hide_elements:
        hide_element.decompose()
'''
for nota_element in nota_elements:
    for embebida_element in nota_element.select(".nota-embebida"):
        embebida_element.decompose()
    for hide_element in nota_element.select(".hide"):
        hide_element.decompose()

print(nota_elements[0].get_text(strip=True))


import requests

url = "https://www.cadena3.com/noticia/futbol/la-historia-de-taty-castellanos-no-jugo-en-argentina-y-la-rompio-en-eeuu_356287"

response = requests.get(url)

response.encoding = 'UTF-8'

print(response.text)

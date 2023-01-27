import requests
from bs4 import BeautifulSoup

# you can insert the website link here
url = "https://docs.python.org/3/library/index.html"

req = requests.get(url)
soup = BeautifulSoup(req.content, "html.parser")

oth = soup.title
print(oth.get_text())
print(oth.prettify())
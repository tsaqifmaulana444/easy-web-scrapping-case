from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")
# print(doc.prettify())

tag = doc.find("b")
# print(tag)

# nested filter
filter = tag.find("u")
print(filter.string)

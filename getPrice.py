from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.ca/p/0TH-01UG-00044?Item=9SIANTREER3672&cm_sp=Homepage_SS-_-P1_9SIANTREER3672-_-01262023"
url2 = "https://www.newegg.ca/apple-iphone-13-pro-max-6-7-2g-3g-4g-lte-5g-blue/p/23M-0003-02211?Item=9SIBBFCJ745765&cm_sp=Homepage_dailydeals-_-P2_9SIBBFCJ745765-_-01262023"

res = requests.get(url2)
doc = BeautifulSoup(res.text, "html.parser")

price = doc.find_all(text="$")
parent = price[0].parent
strong = parent.find("strong")
print("The price is $" + strong.string)
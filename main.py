from bs4 import BeautifulSoup
import requests
from helper import Helper

url = "https://www.douglas.be/nl/p/3001047702"
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "html.parser")

Helper.getProductByFormat("https://www.douglas.be/nl/p/3001047702", "100 ml")
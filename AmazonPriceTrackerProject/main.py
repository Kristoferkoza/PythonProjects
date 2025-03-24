import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.pl/JBL-przenośny-wodoodporny-bezprzewodowy-Bluetooth/dp/B07HKQ6YGX/ref=sr_1_1_mod_primary_new?__mk_pl_PL=ÅMÅŽÕÑ&keywords=JBL+Charge+4&qid=1704397515&s=electronics&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sr=1-1"
header = {"Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                        "like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0 (Edition "
                        "std-1)"}

response = requests.get(URL, headers=header)
website = response.content

soup = BeautifulSoup(website, "html.parser")
price = soup.find(class_="a-price-whole").get_text()

# from bs4 import BeautifulSoup
#
# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
#
# all_a_tags = soup.find_all(name="a")
# print(all_a_tags)

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup.title)
article_title = soup.find_all(name="span", class_="titleline")
for title in article_title:
    print(title.get_text())
    link = title.find(name="a").get("href")
    print(link)


article_score = soup.find_all(class_="score")
for score in article_score:
    print(score.get_text())
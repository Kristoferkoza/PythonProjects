import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
web = response.text


soup = BeautifulSoup(web, "html.parser")
all_titles = soup.find_all(name="h3", class_="title")

title_names = [title.getText() for title in all_titles]
title_names.reverse()

with open("title.txt", mode="w") as file:
    for title in title_names:
        file.write(f"{title}\n")

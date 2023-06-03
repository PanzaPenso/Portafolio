import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL).text

soup = BeautifulSoup(response, "html.parser")
titles_rank = soup.find_all("h3", class_="title")

title_list = [title.text for title in titles_rank]
title_list = [x for x in title_list[::-1]]
with open(r'./100_movies.txt', 'w') as fp:
    for movie in title_list:
        fp.write("%s\n" % movie)
print('Done')




from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
parent_tag = soup.find_all("tr", class_="athing")
score_tag = soup.find_all("span", class_="score")

score_list = [int(score.text.split()[0]) for score in score_tag]
score_list.insert(11, 0)

rank_list = []
anchor_tags = []
for tag in parent_tag:
    rank_list.append(tag.select(".rank"))
    anchor_tags.append(tag.select("td span a"))

final_list = []
for item in range(0, len(rank_list)):
    final_list.append((rank_list[item][0].text, anchor_tags[item][0].get("href"), anchor_tags[item][0].text, score_list[item]))

print(final_list[score_list.index(max(score_list))])
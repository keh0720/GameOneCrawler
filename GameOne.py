import requests
import json
from bs4 import BeautifulSoup
from GameOneCrawler.Players import Players

team_url = "http://www.gameone.kr/club/info/player?club_idx=13457"
player_url = "http://www.gameone.kr/locker/record/sum"
startYear = 2018
endYear = 2018

players = Players.get_players(team_url)
group_code = '3D6307527DE36B0FF0992CA9C8F9F3B3'
total_records = dict()
for year in range(startYear, endYear + 1):
    records = dict()
    for name, info in players.items():
        url = player_url + "?group_code=" + info['group_code'] + "&season=" + str(year)
        soup = BeautifulSoup(requests.get(url).text, 'html.parser')

        titles_html = soup.select(".score_record > ul li span.title")
        scores_html = soup.select(".score_record > ul li span.score")

        titles = [title.text for title in titles_html]
        scores = [score.text for score in scores_html]

        record = dict(zip(titles[:28], scores[:28]))  # only hitter record
        records[name] = record
    total_records[year] = records

print(total_records)

with open("./ninegunners-" + str(startYear) + "-" + str(endYear) + ".json", "w", encoding='utf-8') as json_file:
    json.dump(total_records, json_file, ensure_ascii=False)

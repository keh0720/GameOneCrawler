import requests
from bs4 import BeautifulSoup

url = "http://www.gameone.kr/locker/record/sum?group_code=D93C03B937A50884CFE8E9DC83109966&season=2019"
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')

titles_html = soup.select(".score_record > ul li span.title")
scores_html = soup.select(".score_record > ul li span.score")
titles = [title.text for title in titles_html]
scores = [record.text for record in scores_html]

records = dict(zip(titles, scores))
print(records)

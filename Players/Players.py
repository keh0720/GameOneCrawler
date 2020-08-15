import requests
from bs4 import BeautifulSoup


def get_players(url):
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    player_group = soup.select(".player_list")
    group_code_html = soup.find_all('input', {'name': 'group_code'})
    name_html = soup.select("div.scon_players._helix > ul > li > dl > form > dt")
    group_codes = [group_code.attrs.get('value') for group_code in group_code_html]
    names = [name.text for name in name_html]

    return dict(zip(names, group_codes))


if __name__ == "__main__":

    print(get_players("http://www.gameone.kr/club/info/player?club_idx=13457"))


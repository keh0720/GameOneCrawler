import requests
from bs4 import BeautifulSoup


def get_players(url):
    bs = BeautifulSoup(requests.get(url).text, 'html.parser')

    group_code_html = bs.find_all('input', {'name': 'group_code'})
    name_html = bs.select("div.scon_players._helix > ul > li > dl > form > dt")
    position_html = bs.select("div.scon_players._helix > ul > li > dl > form > dd:nth-child(4)")

    group_codes = [group_code.attrs.get('value') for group_code in group_code_html]
    names = [name.text for name in name_html]
    positions = [str(position.text).split("|")[0].rstrip() for position in position_html]

    players = dict()
    for i in range(len(names)):
        players[names[i]] = dict(group_code=group_codes[i], position=positions[i])

    return players


if __name__ == "__main__":

    print(get_players("http://www.gameone.kr/club/info/player?club_idx=13457"))


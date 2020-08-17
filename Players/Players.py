import requests
from bs4 import BeautifulSoup


def get_players(url):
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    player_group = soup.select(".player_list")
    group_code_html = soup.find_all('input', {'name': 'group_code'})
    name_html = soup.select("div.scon_players._helix > ul > li > dl > form > dt")
    position_html = soup.select("div.scon_players._helix > ul > li > dl > form > dd:nth-child(4)")
    # sContent > div.s_content > div.scon_players._helix > ul > li:nth-child(21) > dl > form > dd:nth-child(4)
    group_codes = [group_code.attrs.get('value') for group_code in group_code_html]
    names = [name.text for name in name_html]
    positions = [str(position.text).split("|")[0].rstrip() for position in position_html]
    i = 0
    players = dict()
    for name in names:
        info = dict(group_code=group_codes[i], position=positions[i])
        players[name] = info
        i += 1
    return players


if __name__ == "__main__":

    print(get_players("http://www.gameone.kr/club/info/player?club_idx=13457"))


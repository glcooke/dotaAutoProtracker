# from pprint import pprint
from dota2gsi import Server
import json
import webbrowser

DOTA_STATE_HERO_SELECTED = "DOTA_GAMERULES_STATE_STRATEGY_TIME"
DOTA_STATE_DRAFTING = "DOTA_GAMERULES_STATE_HERO_SELECTION"
DOTA_PRO_TRACKER_URL = "https://www.dota2protracker.com/hero/"

with open('heroes.json') as heroes_json:
    dota_heroes = {item["id"]: item for item in json.load(heroes_json)["heroes"]}


def on_draft(past_state, state):
    if "map" in state.keys():
        if state["map"]["game_state"] == DOTA_STATE_HERO_SELECTED:
            hero_name_url = f'{dota_heroes[state["hero"]["id"]]["localized_name"].replace(" ", "%20")}#'
            webbrowser.open(DOTA_PRO_TRACKER_URL + hero_name_url,
                            new=0,
                            autoraise=True)
            draft_stage = False
    else:
        draft_stage = False


if __name__ == "__main__":
    server = Server()
    server.on_state_change(on_draft)
    server.start()

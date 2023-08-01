# from pprint import pprint
import dota2gsi
import json
import webbrowser

DOTA_STATE_HERO_SELECTED = "DOTA_GAMERULES_STATE_STRATEGY_TIME"
DOTA_STATE_DRAFTING = "DOTA_GAMERULES_STATE_HERO_SELECTION"
DOTA_PRO_TRACKER_URL = "https://www.dota2protracker.com/hero/"

draft_stage = False
with open('heroes.json') as heroes_json:
    dota_heroes = {item["id"]: item for item in json.load(heroes_json)["heroes"]}


def handle_state(state):
    # Use nested gets to safely extract data from the state
    global draft_stage
    if "map" in state.keys():
        if not draft_stage and state["map"]["game_state"] == DOTA_STATE_DRAFTING:
            draft_stage = True
        if draft_stage and state["map"]["game_state"] == DOTA_STATE_HERO_SELECTED:
            webbrowser.open(DOTA_PRO_TRACKER_URL +
                            f'{dota_heroes[state["hero"]["id"]]["localized_name"].replace(" ", "%20")}#',
                            new=0,
                            autoraise=True)
            draft_stage = False
    else:
        draft_stage = False


if __name__ == "__main__":
    server = dota2gsi.Server()
    server.on_update(handle_state)
    server.start()

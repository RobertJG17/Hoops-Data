import pandas as pd
import requests
import json

### INITIALIZE START ###

card_data = []

ABBR = ["ATL", "BOS","CHA","CHI","CLE","DAL", "DEN","DET",
        "GSW", "HOU", "IND", "LAC", "LAL", "MEM", "MIA",
        "MIL", "MIN", "NO", "NYK", "BKN", "OKC", "ORL", "PHI",
        "PHO", "POR", "SAC", "TOR", "UTH", "WAS"]

BASE_URL = 'http://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/'


def filter_card_components(info):
    ser = pd.Series(info)
    # WE WANT displayName, color, alternateColor, standingSummary, logo, and record ovr
    raw_ser = ser[["displayName", "logos", "record", "standingSummary", "color", "alternateColor"]]

    logo = raw_ser["logos"][0]["href"]
    record_ovr = raw_ser["record"]["items"][0]["summary"]

    refined_ser = raw_ser
    refined_ser["logos"] = logo
    refined_ser["record"] = record_ovr
    refined_ser.rename({"logos": "logo"}, inplace=True)

    return refined_ser.to_dict()

for team in ABBR:
    request = requests.get(BASE_URL + f'{team}')
    info = json.loads(request.content)['team']
    card_data.append(filter_card_components(info))


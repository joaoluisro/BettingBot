import mwclient
import datetime

# Get all matches in certain DATE from a certain TOURNAMENT
# -------------------------KWARGS-------------------------
# team : get all future matches of a particular team
# URL and PATH : honestly idk

def QueryFutureMatches(tournament,
                      team = None,
                      date = datetime.date.today(),
                      URL = 'lol.gamepedia.com',
                      PATH = '/'):

  site = mwclient.Site(URL, path=PATH)

  response = site.api('cargoquery',
         limit = 'max',
         tables = "MatchSchedule=MS, Tournaments=T",
         fields = "MS.Team1, MS.Team2, MS.DateTime_UTC, T.StandardName",
         where = "MS.DateTime_UTC >= '" + str(date) + " 00:00:00' AND T.StandardName='" + tournament + "'",
         join_on = "MS.ShownName=T.StandardName"
  )

  matches = response['cargoquery']
  requested_matches = []

  for match in matches:
    match_title = match['title']
    team1, team2 = match_title['Team1'], match_title['Team2']
    tournament = match_title['StandardName']
    date_time = match_title['DateTime UTC']
    requested_matches.append((team1, team2, date_time))

  return requested_matches


default_tournaments = [
"LCS 2021 Spring",
"LEC 2021 Spring",
"LPL 2021 Spring",
"LCK 2021 Spring",
"CBLOL 2021 Split 1",
]

QueryFutureMatches(default_tournaments[0])

import discord
from discord.ext import commands
from fetch import QueryFutureMatches
import datetime
import csv
import json

bot = commands.Bot(command_prefix='$')

tracked_tournaments = {
    'lcs':'LCS 2021 Spring',
    'lec':'LEC 2021 Spring',
    'cblol':'CBLOL 2021 Split 1',
    'lpl':'LPL 2021 Spring',
    'lck':'LCK 2021 Spring'
}

def update_csv():
    all_scheduled_tournaments = [QueryFutureMatches(tournament)
                            for tournament in tracked_tournaments.values()]

    with open('buffer.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Team1', 'Team2', 'Date', 'Tournament'])
        for t_matches, tourn in zip(all_scheduled_tournaments, track_tournaments.values()):
            for match in tournament_matches:
                writer.writerow(list(match).append(tourn))
        print('Updated Buffer file')

with open('meta.json') as json_file:
    meta = json.load(json_file)
    last_update = datetime.datetime.strptime(meta['updated'], "%Y-%m-%d %H:%M:%S")
    date_now = datetime.datetime.now()
    diff = date_now - last_update
    if diff.days >= 15:
        update_csv()
        meta['updated'] = date_now
    else:
        print('Buffer already updated - carry on')
print('JSON metadata and CSV buffer updated.')

@bot.command()
async def tournaments(ctx):
    all_tourn = ""
    for t in tracked_tournaments.keys():
        all_tourn += t + '\n'
    await ctx.send('Current tracked tournaments: \n{}'.format(all_tourn))

@bot.command()
async def test(ctx, tournament):
    try:
        curr_tour = tournament_dict[tournament]
        matches = QueryFutureMatches(curr_tour)
        await ctx.send('Scheduled Matches: ')
        for match in matches:
            await ctx.send(str(match))
    except:
        await ctx.send('Error in requesting scheduled matches')

token = 'Nzk4NjUzMjExODU0NjM1MDU4.X_4Jww.9IXxIlLBdBeS1vBGo3uNr2lkoZk'
bot.run(token)

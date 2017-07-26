from urllib.request import urlopen
import json


appid = "252490" #Used to define the steam game to query
apikey = "96E46F5C469B9805C0413E1C6A9E0C60" #Used to hook into steam API
steam64 = "76561198381077399" #Used to define steam user
apilink = ("http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid={}&key={}&steamid={}").format(appid,apikey,steam64)

response = urlopen(apilink) #Getting response from the steam web API
string = response.read().decode('utf-8') #Reading the api json and decoding from bytes
json_obj = json.loads(string) #Loading the json object for parsing



stats = (json_obj['playerstats']['stats'])


deaths = stats[0]['value'] #Getting total ingame deaths
fall_deaths = stats[5]['value'] #Getting deaths by falling ingame
self_deaths = stats[6]['value'] #Getting self-inflicted deaths ingame (fire death, drowning)
wolf_deaths = stats[22]['value'] #Getting deaths from wolf ingame
entity_deaths = stats[21]['value'] #Getting deaths from entities (fire particles, etc.)
bear_deaths = stats[23]['value'] #Getting deaths by bear ingame
suicides = stats[4]['value'] #Getting the amount of times I've killed myself ingame
playerkills = stats[7]['value'] #Getting my player kills ingame
bullethits = stats[8]['value'] #Getting my bullet hits ingame
headshots = stats[15]['value'] #Getting my ingame headshot count

#Getting exact death from player

#Calculations to get percentages and ratios
playerdeaths = (deaths -
                fall_deaths -
                self_deaths - wolf_deaths -
                entity_deaths -
                bear_deaths -
                suicides)#Getting deaths caused by players by removing other deaths 
hspercent = round(headshots / bullethits * 100) #Getting a whole number percent of headshots hit
kdr = round(playerkills / playerdeaths, 2) #Get player Kill / Death ratio rounded to two decimal places

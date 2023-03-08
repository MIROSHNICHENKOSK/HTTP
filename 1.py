import requests
import json

url = 'https://www.superheroapi.com/api.php/2619421814940190/search/'

heroes = ['Hulk', 'Captain america', 'Thanos']
iq_dct = {'Hulk': 0, 'Captain america': 0, 'Thanos': 0}

for hero in heroes:
    hero_dict = json.loads(requests.get(str(url) + str(hero)).content)
    iq_dct[hero] = int(hero_dict['results'][0]['powerstats']['intelligence'])

print(max(iq_dct))
import os
#import json
from youtubesearchpython import VideosSearch

videosSearch = VideosSearch(input("What do you wanna search for? \n"), limit = 15)
rezultate = []
for i in videosSearch.result()["result"]:
    rezultate.append({"title" : i["title"], "link" : i["link"]})
#print(rezultate)
alegere = len(rezultate)+1
counter = 0
for i in rezultate:
    print("["+str(counter+1) +"] " + i["title"])
    counter += 1
while int(alegere) > len(rezultate) or alegere.strip() == '' or int(alegere) > len(rezultate):
    alegere = input("\nChoose a number: \n")
    if alegere.strip() == '':
        alegere = len(rezultate)+1
        continue
    if not alegere.strip().isdigit():
        alegere = len(rezultate)+1
        continue
link = rezultate[counter - 1]["link"]
os.system("youtube-dl --extract-audio --audio-format mp3 " + link)

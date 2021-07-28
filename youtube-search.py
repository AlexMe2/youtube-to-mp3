import os
from youtubesearchpython import VideosSearch

videosSearch = VideosSearch(input("What do you wanna search for? \n"), limit = 15)
results = []
for i in videosSearch.result()["result"]:
    results.append({"title" : i["title"], "link" : i["link"]})
choice = len(results)+1
counter = 0
for i in results:
    print("["+str(counter+1) +"] " + i["title"])
    counter += 1
while int(choice) > len(results) or choice.strip() == '' or int(choice) > len(results):
    choice = input("\nChoose a number: \n")
    if choice.strip() == '':
        choice = len(results)+1
        continue
    if not choice.strip().isdigit():
        choice = len(results)+1
        continue
link = results[counter - 1]["link"]
os.system("youtube-dl --extract-audio --audio-format mp3 " + link)

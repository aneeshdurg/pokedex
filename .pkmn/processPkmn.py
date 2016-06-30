from random import randint
import urllib2
from sys import argv

pkmn = ""
if len(argv)==2:
  pkmn = argv[1]

pkmnTable = open("listPkmn.html", "r").readlines()
listPkmn = []
for entry in pkmnTable:
	if "title" in entry and "width" in entry:
		name = entry.replace("<", ":").replace(">",":").replace(" ","").split("title=")[1].split("::")[0].replace('"', "")
		listPkmn.append(name)
pidx = 0
if pkmn=="":
  pidx = randint(0, 150)
else:
  for i in xrange(len(listPkmn)):
    if listPkmn[i].lower()==pkmn.lower():
      pidx = i
      break
url = "http://archives.bulbagarden.net/wiki/File:"+("0" if pidx+1<100 else "" )+("0" if pidx+1<10 else "" )+str(pidx+1)+listPkmn[pidx]+".png"
#print url
response = urllib2.urlopen(url)
imgUrl = ""
lines = response.read().split(">")
for l in lines:
	if "/"+("0" if pidx+1<100 else "" )+("0" if pidx+1<10 else "" )+str(pidx+1)+listPkmn[pidx]+".png" in l:
		imgUrl = l
		break
open("imgUrl.txt", "w").write(imgUrl.split("=")[1].replace('"', ""))
open("pkmnName.txt", "w").write("["+str(pidx+1)+"] "+listPkmn[pidx])

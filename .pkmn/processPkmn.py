from random import randint
import urllib2
from sys import argv

def distance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]

pkmn = ""
ext = 0
if len(argv)==2:
  pkmn = argv[1]

pkmnTable = open("listPkmn.html", "r").readlines()
listPkmn = []
for entry in pkmnTable:
	if "title" in entry and "width" in entry and "(Pok%C3%A9mon)" in entry :
		name = entry.replace("<", ":").replace(">",":").replace(" ","").split("title=")[1].split("::")[0].replace('"', "")
		if name not in listPkmn:
			listPkmn.append(name)
pidx = -1
dist = -1
minDistPkmn = ""
if pkmn=="":
  pidx = randint(0, len(listPkmn)-1)
else:
  for i in xrange(len(listPkmn)):
    if listPkmn[i].lower()==pkmn.lower():
      pidx = i
      break
    else:
      if dist==-1 or distance(listPkmn[i].lower(), pkmn.lower())<dist:
        dist = distance(listPkmn[i].lower(), pkmn.lower())
        minDistPkmn = listPkmn[i]
  if pidx==-1:
    print pkmn+" not found!"
    print "\t Did you mean '"+minDistPkmn+"' instead?"
    pidx = 0
    exit(1)
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

exit(ext)

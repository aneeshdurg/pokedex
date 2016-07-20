 #!/usr/bin/python
 # -*- coding: utf-8 -*-
import json
from random import randint
from sys import argv
import urllib2

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

pkmn = json.loads(open("pkmnJson", "r").read())
keys = pkmn.keys()

theID = -1
minDistPkmn = [-1, ""]

if len(argv)>1 and argv[1][0]!="-":
	for pkid in keys:
		if pkmn[pkid]["name"] == argv[1]:
			theID = pkid
			break
		else:
			if minDistPkmn[0]==-1 or distance(pkmn[pkid]["name"], argv[1])<minDistPkmn[0]:
				minDistPkmn[0] = distance(pkmn[pkid]["name"], argv[1])
				minDistPkmn[1] = pkmn[pkid]["name"]
else:
	pkid = randint(0, len(keys)-1)
	theID = keys[pkid]

if theID==-1:	
	print argv[1]+" not found!"
	print "\t Did you mean '"+minDistPkmn[1]+"' instead?"
	exit(1)

pkmn = pkmn[theID]
pkmnName = pkmn["name"]
imgURL = pkmn["img"]
pokedexEntries = pkmn["pokedex"]
pkdxKeys = pokedexEntries.keys()
pkdxid = randint(0, len(pkdxKeys)-1)
pkdxsrc = pkdxKeys[pkdxid]
pkdxEntry = pokedexEntries[pkdxsrc]

#print imgURL
response = urllib2.urlopen(imgURL)
imgURL = ""
lines = response.read().split(">")
searchStr = "/"+("0" if int(theID)<100 else "" )+("0" if int(theID)<10 else "" )+str(int(theID))+str(pkmnName)+".png"
#print searchStr
for l in lines:
	#print l
	if searchStr in l:
		imgURL = l
		break

if "-p" in argv:
	print pkmnName
	print imgURL
	print pkdxsrc
	print pkdxEntry
else:
	open("imgUrl.txt", "w").write(imgURL.split("=")[1].replace('"', ""))
	open("pkmnName.txt", "w").write("["+str(int(theID))+"] "+pkmnName)
	open("pkdesource.txt", "w").write(pkdxsrc.encode('utf8'))
	open("pkdex.txt", "w").write(pkdxEntry.encode('utf8'))
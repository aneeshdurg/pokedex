import urllib2
from sys import argv
from random import randint
if len(argv)<2:
  print "Usage: python getPokedex.py [pokemon name] {-p}"
  exit()
if " " in argv[1]:
 argv[1] = argv[1].split(" ")[1].replace('"', "")
url = "http://bulbapedia.bulbagarden.net/wiki/"+argv[1]+"_%28Pok%C3%A9mon%29"
#print "URL: ", url
response = urllib2.urlopen(url)
lines = response.read()
#print lines
lines = lines.split("\n")
pdex = {}
source = ""
start = -1
title = ""
skip = False
for i in xrange(len(lines)):
  l = lines[i]
  if start==3:
    if len(l)<11:
      continue
    if "Game locations" in l:
      break
    if "title=" in l:
      #print "TITLE"
      #print l
      title = l.split("title=")[1]
      title = title.split('"')[1]#.replace('"', '')
      if title in pdex:
        title=""
    elif not skip and title!="":
      skip = True
    elif skip and title!="":
      if "/" in l:
        title = ""
        skip = False
      else:
        skip = False
        #print l
        pdex[title] = l.split("> ")[1]
        title = ""
  else:
    if 'id="Pok.C3.A9dex_entries_3"' in l:
       #print l
       start+=1
    elif start>=0 and "table" in l:
      start+=1
if start == -1:
  for i in xrange(len(lines)):
    l = lines[i]
    if start==3:
      if len(l)<11:
        continue
      if "Game locations" in l:
        break
      if "title=" in l:
        #print "TITLE"
        #print l
        title = l.split("title=")[1]
        title = title.split('"')[1]#.replace('"', '')
        if title in pdex:
          title=""
      elif not skip and title!="":
        skip = True
      elif skip and title!="":
        if "/" in l:
          title = ""
          skip = False
        else:
          skip = False
          #print l
          pdex[title] = l.split("> ")[1]
          title = ""
    else:
      if 'id="Pok.C3.A9dex_entries_2"' in l:
         #print l
         start+=1
      elif start>=0 and "table" in l:
        start+=1
if start==-1:
  for i in xrange(len(lines)):
    l = lines[i]
    if start==3:
      if len(l)<11:
        continue
      if "Game locations" in l:
        break
      if "title=" in l:
        #print "TITLE"
        #print l
        title = l.split("title=")[1]
        title = title.split('"')[1]#.replace('"', '')
        if title in pdex:
          title=""
      elif not skip and title!="":
        skip = True
      elif skip and title!="":
        if "/" in l:
          title = ""
          skip = False
        else:
          skip = False
          #print l
          pdex[title] = l.split("> ")[1]
          title = ""
    else:
      if 'id="Pok.C3.A9dex_entries"' in l:
         #print l
         start+=1
      elif start>=0 and "table" in l:
        start+=1
klen = len(pdex.keys())
#print klen
k = randint(0, klen-1)
#print k
source = pdex.keys()[k]
entry = pdex[pdex.keys()[k]]
if "-p" in argv:
  print source
  print entry
else:
  open("pkdesource.txt", "w").write(source)
  open("pkdex.txt", "w").write(entry) 

 

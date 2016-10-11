import Names, WikipediaParser
##name,type,imageurl,wikipediaIDfi,WikipediaIDen

names = Names.getplantnames()
namesbirds =Names.getspeciesnames("species-names.txt")
#names.extend(namesbirds)

csv = open("species.CSV", 'w')

for name in names:
    pic = WikipediaParser.getpicture(name[0])
    enid = WikipediaParser.getIDen(name[0])
    finid = WikipediaParser.getIDfi(name[0])

    csv.write(name[0]+","+name[1]+","+pic+","+finid+","+enid+"\n")
for name in namesbirds:
    pic = WikipediaParser.getpicture(name[0])
    enid = WikipediaParser.getIDen(name[0])
    finid = WikipediaParser.getIDfi(name[0])

    csv.write(name[0]+","+name[1]+","+pic+","+finid+","+enid+"\n")


csv.close()

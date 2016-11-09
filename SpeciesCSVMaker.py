import Names, WikipediaParser,codecs
##name,type,imageurl,wikipediaIDfi,WikipediaIDen

names = Names.getplantnames()
namesbirds =Names.getspeciesnames("species-names.txt")
#names.extend(namesbirds)
#print(len(names))


"""
sf = codecs.open("species.CSV", 'r', 'utf-8')
nameslist= []
s = sf.readline()

while len(s) > 0:
    s = s.split(',')
    name = s[0]
    nameslist.append(name)
    s = sf.readline()
"""
#print(nameslist)

csv = codecs.open("species.CSV", 'w', 'utf-8')


#asd = [y[1] for y in names].index("Suokorte")
#print(asd)
#name = names[1933]
#print(name)
#print(WikipediaParser.getpicture(name[0]))

#enid = WikipediaParser.getIDen(name[0])
#finid = str(WikipediaParser.getIDfi(name[0]))
#typespec = "2"

for name in names:
    pic = WikipediaParser.getpicture(name[0])
    if pic != "-1":

        enid = WikipediaParser.getIDen(name[0])
        finid = str(WikipediaParser.getIDfi(name[0]))
        typespec = "1"
        csv.write(name[0]+","+name[1]+","+typespec+","+pic+","+finid+","+enid+"\n")
        print(name)
    else:
        csv.write("###ERROR###"+name[0]+"\n")
for name in namesbirds:
    pic = WikipediaParser.getpicture(name[0])
    if pic != "-1":
        enid = WikipediaParser.getIDen(name[0])
        finid = str(WikipediaParser.getIDfi(name[0]))
        typespec = "2"
        csv.write(name[0]+","+name[1]+","+typespec+","+pic+","+finid+","+enid+"\n")
        print(name)
    else:
        csv.write("###ERROR###" + name[0]+"\n")


csv.close()
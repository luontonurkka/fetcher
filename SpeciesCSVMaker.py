import Names, WikipediaParser,codecs

names = Names.getplantnames()
namesbirds =Names.getspeciesnames("species-names.txt")

csv = codecs.open("species.CSV", 'w', 'utf-8')


for name in names:
    pic = WikipediaParser.getpictureSoup(name[0])
    if pic != "-1":

        enid = WikipediaParser.getIDen(name[0])
        finid = str(WikipediaParser.getIDfi(name[0]))
        if finid=="-1":
            finid=str(WikipediaParser.getIDfi(name[1]))

        typespec = "1"
        csv.write(name[0]+","+name[1]+","+typespec+","+pic+","+finid+","+enid+"\n")
        print(name)
    else:
        pic = WikipediaParser.getpicture(name[0])
        if pic != "-1":
            enid = WikipediaParser.getIDen(name[0])
            finid = str(WikipediaParser.getIDfi(name[0]))
            if finid == "-1":
                finid = str(WikipediaParser.getIDfi(name[1]))
            typespec = "1"
            csv.write(name[0] + "," + name[1] + "," + typespec + "," + pic + "," + finid + "," + enid + "\n")
            print(name)
        else:
            csv.write("###ERROR###"+name[0]+","+name[1]+"\n")

for name in namesbirds:
    if name[0] == "Corvus corone cornix":
        name[0] == "Corvus cornix"
    if name[0]  == "Luscinia cyanura":
        name[0] = "Tarsiger cyanurus"
    pic = WikipediaParser.getpictureSoup(name[0])#getpicture(name[0])
    if pic != "-1":

        enid = WikipediaParser.getIDen(name[0])
        finid = str(WikipediaParser.getIDfi(name[0]))
        if finid=="-1":
            finid=str(WikipediaParser.getIDfi(name[1]))

        typespec = "2"
        csv.write(name[0]+","+name[1]+","+typespec+","+pic+","+finid+","+enid+"\n")
        print(name)
    else:
        pic = WikipediaParser.getpicture(name[0])
        if pic != "-1":
            enid = WikipediaParser.getIDen(name[0])
            finid = str(WikipediaParser.getIDfi(name[0]))
            if finid == "-1":
                finid = str(WikipediaParser.getIDfi(name[1]))
            typespec = "2"
            csv.write(name[0] + "," + name[1] + "," + typespec + "," + pic + "," + finid + "," + enid + "\n")
            print(name)
        else:
            csv.write("###ERROR###"+name[0]+","+name[1]+"\n")


csv.close()
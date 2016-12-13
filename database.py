# -*- coding: utf-8 -*-
import dataset,codecs, Names, sqlite3

"""
Under MIT-Licence, 2016 Perttu Rautaniemi
"""


def createtables():
    """
    Opening the database and tables, create tables if they dont exist
    """
    conn = sqlite3.connect('LuontonurkkaDB.db')

    conn.execute('''CREATE TABLE `grid` (
    	`id`	INTEGER NOT NULL,
    	`N`	INTEGER NOT NULL,
    	`E`	INTEGER NOT NULL,
    	`sqrname`	VARCHAR,
    	PRIMARY KEY(id)
    );''')
    conn.execute('''CREATE TABLE `species` (
    	`id`	INTEGER NOT NULL,
    	`namelatin`	VARCHAR NOT NULL,
    	`namefin`	VARCHAR,
    	`type`	INTEGER NOT NULL,
    	`picture`	VARCHAR,
    	`idEN`	VARCHAR,
    	`idFI`	VARCHAR,
    	PRIMARY KEY(id)
    );''')
    conn.execute('''CREATE TABLE "species_in_square" (
    	`id`	INTEGER NOT NULL,
    	`sid`	INTEGER NOT NULL,
    	`gid`	INTEGER NOT NULL,
    	`freq`	INTEGER,
    	PRIMARY KEY(id)
    )''')

    ##
    ## Sql for indexes
    ##
    conn.execute('''CREATE INDEX gridIndex
    on grid (N, E);''')
    conn.execute('''CREATE INDEX sqrID
    on species_in_square (gid);''')
    conn.close()


"""filling both species in square and square tables using id data from speciestable and gridcsv for"""
def data_fillfromCSV():
    db = dataset.connect('sqlite:///LuontonurkkaDB.db')
    tableSquare = db.get_table("grid")
    tableSpecies = db.get_table("species")
    tableSpeSqr = db.get_table("species_in_square")

    csv = codecs.open("species.CSV", "r", "UTF-8")
    asdi = csv.readlines()
    datablob = {}
    specieslist = []
    counter = 1
    for line in asdi:
        if not line.__contains__("###ERROR###"):
            specdata = line.split(',')
            specdata[5] = specdata[5].strip("\n")
            data = dict(id=counter, namelatin=specdata[0], namefin=specdata[1], type=specdata[2], picture=specdata[3],
                        idEN=specdata[4], idFI=specdata[5])
            counter += 1
            specieslist.append(data)
            datablob[specdata[0]] = data

    gridcsv = codecs.open("grid_sorted.csv", "r", "UTF-8")

    gridnames = Names.getgridnames()
    listItems = []
    listCoords = []
    stackItems = gridcsv.readlines()
    for line in stackItems:
        blo = []
        blo = line.split(',')
        bla = blo[0].split(':')
        namn =""
        for i, dic in enumerate(gridnames):
            if dic['N'] == bla[0] and dic['E'] == bla[1]:
                namn = dic['name']
        acab = dict(N=bla[0], E=bla[1], sqrname=namn)
        listCoords.append(acab)
        del blo[0]
        for item in blo:
            species = item.split(':')
            spec = datablob.get(species[0])  # replace the name with id from speciestable
            if spec is not None:
                specgrid = len(listCoords)  # replace coords with ID from squaretable
                info = dict(sid=spec['id'], gid=specgrid, freq=species[2].strip("\r\n"))
                listItems.append(info)
    #finally, the inserts
    tableSpecies.insert_many(specieslist)
    tableSquare.insert_many(listCoords)
    tableSpeSqr.insert_many(listItems)






#createtables()
data_fillfromCSV()
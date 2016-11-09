# -*- coding: utf-8 -*-
import dataset, sqlalchemy, codecs, re, Names, time

def createtables():
    """
    Opening the database and tables, create tables if they dont exist
    """
    db= dataset.connect('sqlite:///LuontonurkkaDB.db')
    tableSquare = db.get_table("grid",)
    tableSpecies = db.get_table("species")
    tableSpeSqr = db.get_table("species_in_square")

    """
    Create table columns, check if these are what we wanted.
    """
    tableSquare.create_column("N", sqlalchemy.types.INTEGER)
    tableSquare.create_column("E", sqlalchemy.types.Integer)

    tableSpeSqr.create_column("sid", sqlalchemy.types.Integer)
    tableSpeSqr.create_column("gid", sqlalchemy.types.Integer)
    tableSpeSqr.create_column("freq", sqlalchemy.types.Integer)


    tableSpecies.create_column("namelatin",sqlalchemy.types.String)
    tableSpecies.create_column("namefin",sqlalchemy.types.String)
    tableSpecies.create_column("type",sqlalchemy.types.Integer)
    tableSpecies.create_column("picture",sqlalchemy.types.String)
    tableSpecies.create_column("idEN",sqlalchemy.types.Integer)
    tableSpecies.create_column("idFI",sqlalchemy.types.Integer)



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

    listItems = []
    listCoords = []
    stackItems = gridcsv.readlines()
    for line in stackItems:
        blo = []
        blo = line.split(',')
        bla = blo[0].split(':')
        acab = dict(N=bla[0], E=bla[1])
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

def fillspeciesproperly():
    """Add names and types to speciestable"""
    db = dataset.connect('sqlite:///LuontonurkkaDB.db')
    tableSpecies = db.get_table("species")

    asd = Names.getspeciesnames("species-names.txt")
    wasd = Names.getplantnames()
    line = asd[0]
    data = dict([('namelatin',line[0]),('namefin', line[1]),('type', 2)])



data_fillfromCSV()
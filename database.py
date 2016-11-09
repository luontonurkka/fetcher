# -*- coding: utf-8 -*-
import dataset, sqlalchemy, codecs, re, Names, time

def createtables():
    """
    Opening the database and tables, create tables if they dont exist
    """
    db= dataset.connect('sqlite:///LuontonurkkaDB')
    tableSquare = db.get_table("square",)
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
def squaresdata_fillfromCSV():
    db = dataset.connect('sqlite:///LuontonurkkaDB')
    tableSquare = db.get_table("square", )
    tableSpecies = db.get_table("species")
    tableSpeSqr = db.get_table("species_in_square")
    gridcsv = codecs.open("grid_sorted.csv", "r" , "UTF-8")

    stack = gridcsv.readlines()
    for asd in stack:
        blo = asd.split(',')        #split lines to form 'name:type:id lists'

        acab ={}
        for item in blo:
            if re.match("[0-9]{3}:[0-9]{3}", item):    #if is grid, save to grid table for ID in later use
                a,b = item.split(':')
                acab = dict(N =a, E = b)
                tableSquare.insert(acab)
            else:
                species = item.split(':')
                spec= tableSpecies.find_one(namelatin = species[0])     #replace the name with id from speciestable
                if spec is not None:
                    specgrid = tableSquare.find_one(N=acab['N'], E=acab['E'])      #replace coords with ID from squaretable
                    info = dict(sid=spec['id'], gid=specgrid['id'], freq=species[2])
                    tableSpeSqr.insert(info)                               #insert data into table

def fillspeciestable():

    db = dataset.connect('sqlite:///LuontonurkkaDB')
    tableSpecies = db.get_table("species")


    csv = codecs.open("species.csv", "r" , "UTF-8")
    asd = csv.readlines()
    datablob = []
    for line in asd:
        if not line.__contains__("###ERROR###"):
            specdata = line.split(',')
            specdata[5] = specdata[5].strip("\n")
            data = dict(namelatin = specdata[0],namefin = specdata[1],type = specdata[2],picture = specdata[3], idEN = specdata[4], idFI = specdata[5])
            datablob.append(data)
    tableSpecies.insert_many(datablob)


def fillspeciesproperly():
    """Add names and types to speciestable"""
    db = dataset.connect('sqlite:///LuontonurkkaDB')
    tableSpecies = db.get_table("species")

    asd = Names.getspeciesnames("species-names.txt")
    wasd = Names.getplantnames()
    line = asd[0]
    data = dict([('namelatin',line[0]),('namefin', line[1]),('type', 2)])




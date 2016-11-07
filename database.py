import dataset, sqlalchemy

"""
Opening the database and tables, create tables if they dont exist
"""
db= dataset.connect('sqlite:///LuontonurkkaDB')
tableSquare = db.get_table("square", "N" )
tableSpecies = db.get_table("species")
#tableSpeSqr = db.get_table("spesqr")  #if we use arrays in squares-table, not necessary.
"""
Create table columns, check if these are what we wanted.
"""
tableSquare.create_column("E", sqlalchemy.types.Integer)
tableSquare.create_column("speciesList", sqlalchemy.types.String)

tableSpecies.create_column("namelatin",sqlalchemy.types.String)
tableSpecies.create_column("namefin",sqlalchemy.types.String)
tableSpecies.create_column("picture",sqlalchemy.types.String)
tableSpecies.create_column("idEN",sqlalchemy.types.String)
tableSpecies.create_column("idFI",sqlalchemy.types.String)


"""
testing
"""
data = dict([('namelatin','koiran'),('namefin','karvoja'),('picture','suussani'),('idEN','on'),('idFI','miljoona')])
tableSpecies.insert(data)
rows = tableSpecies.all()
for n in rows:
    print n

data2 = dict()
tableSquare.insert(data2)


import json, urllib2

def getgrid():
    response = urllib2.urlopen('http://koivu.luomus.fi/kasviatlas/ruudut-json.php')
    data = response.read()
    posgrid = data.split(',')
    posgrid[0] = posgrid[0][1:]
    posgrid[-1] = posgrid[-1][0:-1]
    for i in range(len(posgrid)):
        posgrid[i] = posgrid[i][1:-1]
    return posgrid

def getgridpos(ne, year):
    url = "http://www.luomus.fi/kasviatlas/grid.php?key=" + ne + "&year=" + str(year) + "&format=json"
    response = urllib2.urlopen(url)
    data = response.read()
    return json.loads(data)

def makecsvline(gridjson):
    line = ""
    lajit = gridjson['lajit']
    comma = ""
    for laji in lajit:
        line = line + comma + laji + ":" + lajit[laji]['frekvenssi']
        comma = ","
    return line

posgrid = getgrid()

print(makecsvline(getgridpos(posgrid[100], 2015)))


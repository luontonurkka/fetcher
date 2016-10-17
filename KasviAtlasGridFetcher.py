# -*- coding: utf-8 -*-
import json, urllib2, codecs

def getgrid():
    # get list of the grid squares
    response = urllib2.urlopen('http://koivu.luomus.fi/kasviatlas/ruudut-json.php')
    data = response.read()
    # remove square brackets
    posgrid[0] = posgrid[0][1:]
    posgrid[-1] = posgrid[-1][0:-1]
    # remove "
    for i in range(len(posgrid)):
        posgrid[i] = posgrid[i][1:-1] 
    return posgrid

def getgridpos(ne, year):
    # get single square json
    url = "http://www.luomus.fi/kasviatlas/grid.php?key=" + ne + "&year=" + str(year) + "&format=json"
    print(url)
    response = urllib2.urlopen(url)
    data = response.read()
    # parse json to python object and return
    return json.loads(data)

def makecsvline(gridjson):
    # make a csv line out of square json
    line = ""
    # check if json has lajit attr
    try:
        lajit = gridjson['lajit']
    except KeyError:
        return ""
    # make comma seperated string out of the species info
    comma = ""
    for laji in lajit:
        line = line + comma + laji + ":" + lajit[laji]['frekvenssi']
        comma = ","
    return line

def makecsvdict(grid, year):
    # get all of the squares
    posgrid = getgrid()
    # check all squares and add to dictionary
    for pos in posgrid:
        line = makecsvline(getgridpos(pos, year))
        # check if square exists in the grid
        try:
            old = grid[pos]
            grid[pos] = old + "," + line
        except KeyError:
            grid[pos] = line

    return grid


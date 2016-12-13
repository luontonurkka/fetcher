import requests, bs4

"""
Under MIT-Licence, 2016 Perttu Rautaniemi
"""

def getplantnames():
    """ This method gets all the scientific and finnish names from url and returns them"""
    names = []
    site = requests.get("http://koivu.luomus.fi/kasviatlas/all.php")
    soup = bs4.BeautifulSoup(site.text)
    lista = soup.find("div", {"id": "main"})
    das = lista.get_text().splitlines()
    del das[0:2]
    del das[len(das) - 3:]
    for line in das:
        latin, finnish = line.split(' - ', 1)
        print(finnish)
        latin = latin.strip()
        finnish = finnish.strip()
        finn = finnish.split(' ')
        del finn[len(finn) - 1]
        finnish = " ".join(finn)
        finnish = finnish.replace('(', '')
        finnish = finnish.replace(')', '')
        finnish = finnish.replace(',', '')
        finnish = finnish.capitalize()
        o = latin.split(' ')
        if len(o) == 1 or finnish.__contains__("Ryhmä") or finnish.__contains__("ryhmä") or len(finnish)<2:
            continue
        else:
            names.append([latin, finnish])
    return names

###I brazenly took this from jarno's code and modified it for my needs, thanks###

def getspeciesnames(speciesfilename):
    # open the file
    sf = open(speciesfilename, 'r')
    # init empty dict
    names = []
    # first line is skipped
    s = sf.readline()
    s = sf.readline()
    # read to end of the file
    while len(s) > 0:
        # data is split with tabs
        # first colums in the code and second full name
        parts = s.split("\t")
        # add dict
        names.append([parts[1], parts[2]])
        # read next line
        s = sf.readline()
    return names

def getgridnames():
    names = []
    site = requests.get("http://atlas3.lintuatlas.fi/tulokset/ruudut")
    soup = bs4.BeautifulSoup(site.text)
    lista = soup.find("div", {"id": "d-main"})
    das=  lista.get_text().splitlines()
    for item in das:
        try:
            a,b = item.split(",")
            N,E = b.strip().split(":")
            names.append(dict(N=N,E=E,name=a))
        except:
            continue
    return names

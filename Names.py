import requests, bs4


def getplantnames():
    """ This method gets all the scientific and finnish names from url and returns them"""
    # open the html file
    site = requests.get("http://koivu.luomus.fi/kasviatlas/all.php")
    # make an empty list
    names = []
    # start reading the html document by splitting into lines
    a = site.text.splitlines()
    for line in a:
        # lets grab all links, counting out the first one wich does not suit our needs
        if line.startswith("<a href=") and not line.__contains__("vaxtatlas"):
            # splitting the line until we get "scientific - finnish"
            b, a, = line.split('>', 1)
            a, b = a.split('<', 1)
            # print(a)
            a, b = a.split('(', 1)
            latin, finnish = a.split('-', 1)
            latin = latin.strip()
            finnish = finnish.strip()
            # capitals for uniformity, then appending our friendly list.
            finnish = finnish.capitalize()
            # print(finnish)
            names.append((latin, finnish))
            #   return names
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
        names.append((parts[1], parts[2]))
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

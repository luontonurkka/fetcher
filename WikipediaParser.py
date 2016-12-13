import wikipedia, requests, bs4

"""
Under MIT-Licence, 2016 Perttu Rautaniemi
"""

def getpicture(name):
    if name == "Apera":
        return "-1"
    try:
        page = wikipedia.page(name)
        asd = page.images

        for imga in asd:
            if not (imga.__contains__("svg") or imga.__contains__("ogg") or imga.__contains__("ogv") or imga.__contains__("map") or imga.__contains__("range") or imga.__contains__("Bronze-Oak-Leaf-Cluster")or imga.__contains__("Bronze-Oak-Leaf-Cluster")):
                pic = imga
                break
            else:
                pic = "-1"
        return pic
    except:
        pic = "-1"
        return pic

def getpictureSoup(name):
    try:
        asd = requests.get("https://en.wikipedia.org/wiki/%s" % name)
        site = asd.text
        soup = bs4.BeautifulSoup(site)
        kuva = soup.find('table', {"class": "infobox biota"})
        pra = kuva.find('img')
        pre = pra['src']
        pri = pre.replace("/thumb", "")
        pra, b = pri.split("/220")
        pic = "https:" + pra
        return pic
    except:
        return "-1"

def getIDen(name):
    try:
        page = wikipedia.page(name)
        enid = page.pageid
        return enid
    except:
        enid = "-1"
        return enid

def getIDfi(name):
    wikipedia.set_lang("fi")
    try:
        page = wikipedia.page(name)
        finid = page.pageid
        wikipedia.set_lang("en")
        return finid
    except:
        finid = "-1"
        return finid

def getdescriptionfin(name):
    wikipedia.set_lang("fi")
    page = wikipedia.page(name)
    text = page.summary
    wikipedia.set_lang("en")
    return text

def getdescriptionen(name):
    page = wikipedia.page(name)
    text = page.summary
    return text

""""
kuva = page.url
site = requests.get(kuva)
a = site.text.splitlines()
for i in range(len(a)):
   if a[i].__contains__("infobox biota"):
       image = a[i + 6]
   lista = image.split('src', )
   a = lista[2].split('1.5x,')
   a = a[1].split(" 2x")
   a = a[0].lstrip()
   a = "https:" + a
return a
"""""

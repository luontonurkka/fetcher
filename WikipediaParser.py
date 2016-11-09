import wikipedia, requests

def getpicture(name):
    if name == "Apera":
        return "-1"
    try:
        page = wikipedia.page(name)

        pic = page.images[0]
        return pic
    except:
        pic = "-1"
        return pic

def getIDen(name):
    page = wikipedia.page(name)
    enid = page.pageid
    return enid

def getIDfi(name):
    wikipedia.set_lang("fi")
    try:
        page = wikipedia.page(name)
        finid = page.pageid
        wikipedia.set_lang("en")
        return finid
    except:
        finid = -1
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
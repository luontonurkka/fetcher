import wikipedia

def getpicture(name):
    page = wikipedia.page(name)
    pic = page.images[0]
    return pic

def getIDen(name):
    page = wikipedia.page(name)
    enid = page.pageid
    return enid

def getIDfi(name):
    wikipedia.set_lang("fi")
    page = wikipedia.page(name)
    finid = page.pageid
    wikipedia.set_lang("en")
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
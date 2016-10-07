speciesnamesfile = "species-names.txt"

def getspeciesnames():
    sf = open(speciesnamesfile, 'r')
    names = {}
    s = sf.readline()
    s = sf.readline()
    while len(s) > 0:
        parts = s.split("\t")
        names[parts[0]] = parts[1]
        s = sf.readline()
    return names

def getgrid(names):
    breedingfile = "atlas3-breeding-data.txt"
    bf = open(breedingfile, 'r')

    grid = {}

    s = bf.readline()
    s = bf.readline()

    while len(s) > 0:
        parts = s.split("\t")
        print(parts)
        spec = names[parts[1]] + ":" + parts[5]
        pos = parts[2] + ":" + parts[3]
        try:
            old = grid[pos]
            grid[pos] = old + "," + spec
        except KeyError:
            grid[pos] = spec
        s = bf.readline()

    print grid

if __name__ == "__main__":

    names = getspeciesnames()
    grid = getgrid(names)
















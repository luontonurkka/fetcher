speciesnamesfile = "species-names.txt"

def getspeciesnames(speciesfilename):
    sf = open(speciesfilename, 'r')
    names = {}
    s = sf.readline()
    s = sf.readline()
    while len(s) > 0:
        parts = s.split("\t")
        names[parts[0]] = parts[1]
        s = sf.readline()
    return names

def getgrid(breedfilename, names):
    bf = open(breedfilename, 'r')

    grid = {}

    s = bf.readline()
    s = bf.readline()

    while len(s) > 0:
        parts = s.split("\t")
        code, n, e, freq = parts[1], parts[2], parts[3], parts[5].strip()
        if code not in names:
            print("skipped " + code)
            s = bf.readline()
            continue
        spec = names[code] + ":" + freq
        pos = n + ":" + e
        try:
            old = grid[pos]
            grid[pos] = old + "," + spec
        except KeyError:
            grid[pos] = spec
        s = bf.readline()

    return grid

if __name__ == "__main__":
    specfile, breedfile, outfile = "species-names.txt", "atlas3-breeding-data.txt", "grid.csv"
    names = getspeciesnames(specfile)
    grid = getgrid(breedfile, names)
    f = open(outfile, 'w')
    for pos, line in grid.iteritems():
        f.write(pos + "," + line + "\n")
    f.close()


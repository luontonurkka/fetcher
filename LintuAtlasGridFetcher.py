def getspeciesnames(speciesfilename):
    # open the file
    sf = open(speciesfilename, 'r')
    # init empty dict
    names = {}
    #first line is skipped
    s = sf.readline()
    s = sf.readline()
    # read to end of the file
    while len(s) > 0:
        # data is split with tabs
        # first colums in the code and second full name
        parts = s.split("\t")
        # add dict
        names[parts[0]] = parts[1]
        # read next line
        s = sf.readline()
  
    return names

def getgrid(breedfilename, names):
    # open the file
    bf = open(breedfilename, 'r')
    # empty dict
    grid = {}
    # skip first line
    s = bf.readline()
    s = bf.readline()
    # read to end of the file
    while len(s) > 0:
        # columns are seperated with tabs
        parts = s.split("\t")
        # copy values to variables
        code, n, e, freq = parts[1], parts[2], parts[3], parts[5].strip()
        # normalize frequensy to 0-100 scale
        freq = str(int(freq)*25)
        # if full name is not in the dict skip
        if code not in names:
            print("skipped " + code)
            # but remember to read next line or
            # infinite loop
            s = bf.readline()
            continue
        # get full name and combine it with freq
        spec = names[code] + ":" + freq
        # combine north and east pos
        pos = n + ":" + e
        try:
            # try to append to the grid pos
            # will raise KeyError if grid pos is not in the dict
            old = grid[pos]
            grid[pos] = old + "," + spec
        except KeyError:
            # grid pos wasn't in the dict
            # so add it
            grid[pos] = spec
        # read next line
        s = bf.readline()
    # grid should now be filled with breeding info
    return grid

if __name__ == "__main__":
    # species code to full name file,
    # breeding grid data file,
    # output csv file
    specfile, breedfile, outfile = "species-names.txt", "atlas3-breeding-data.txt", "grid.csv"
    # make dictionary wich combines code and name
    # with code as key value
    names = getspeciesnames(specfile)
    # make a dictionary where
    # key values are the grid coordinates
    # and values the breeding info
    grid = getgrid(breedfile, names)
    # write grid dictonary to outfile
    f = open(outfile, 'w')
    for pos, line in grid.iteritems():
        f.write(pos + "," + line + "\n")
    f.close()


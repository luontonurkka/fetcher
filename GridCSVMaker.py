import KasviAtlasGridFetcher
import LintuAtlasGridFetcher
import codecs, time

# to check total time
t = time.time()

# get bird data first
print("fetchin bird data")
specfile, breedfile, outfile = "species-names.txt", "atlas3-breeding-data.txt", "grid.csv"
names = LintuAtlasGridFetcher.getspeciesnames(specfile)
grid = LintuAtlasGridFetcher.getgrid(breedfile, names)

# plants
print("fetching plant data")
grid = KasviAtlasGridFetcher.makecsvdict(grid, 2015)

# make the csv
print("writing to 'grid.csv'")
f = codecs.open("grid.csv", 'w', 'utf-8')
for pos, line in grid.iteritems():
    f.write(pos + "," + line + "\n")
f.close()

# done
print("total time: " + str(time.time() - t))


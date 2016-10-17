import KasviAtlasGridFetcher
import LintuAtlasGridFetcher
import codecs, time
import coordinates

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
  # get YKJ coordinates and converse them to WGS84
  coordYKJ = pos.split(':')
  WGS = coordinates.KKJxy_to_WGS84lalo({'P':int(coordYKJ[0])*10000, 'I':int(coordYKJ[1])*10000}, 3)
  f.write(str(WGS["La"]) + ":" + str(WGS["Lo"])  + "," + line + "\n")
f.close()

# done
print("total time: " + str(time.time() - t))


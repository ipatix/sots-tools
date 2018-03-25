import agb

STDPROJ = "../../source_of_the_sovereign/sots-private/map/sots.json"
MAPOUTPUT = "../../source_of_the_sovereign/sots-private/map/maps/%b/%m/map_%b_%m.pmh" #%b will be replaced with bank and %m with map
MAPSYM = "map_%b_%m"
TSOUTPUT = "../../source_of_the_sovereign/sots-private/map/tileset/tileset%n/maptileset%n" #%s will be replaced with the offset and %n with the number relative to TSTABLE
TSGRAPHIC = "../../source_of_the_sovereign/sots-private/map/tileset/tileset%n/gfx_maptileset%n.png" #Can be None as well - no graphic will be exported then
TSGFXSYM = "gfx_maptileset%nTiles"
TSSYM = "maptileset%n"
STDROM = "../../source_of_the_sovereign/base/bpre0.gba"
MAPTABLEPTR = 0x5524C
TSTABLE = 0x4A32D0
STDPREAMBLE = "pymap_constants.h"
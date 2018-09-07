
import os
import sys
import getopt
from pymap import config
from pymap import path as rpath
STDLIB = "./lib/macros.py"
INCLUDE = "../include"
STDPREAMBLE = config.STDPREAMBLE

""" Table of certain constants """

# ------------------------------------------------------------------------------------------------------------------------------------------
# Musik & Anderes
# ------------------------------------------------------------------------------------------------------------------------------------------
music = {
	267: "SEQ_BGM_TOWN_HESPERIA",
	272: "SEQ_BGM_CITY_CARUN",
	273: "SEQ_BGM_CITY_URBANIA",
	302: "SEQ_BGM_ROUTE_1",
	303: "SEQ_BGM_ROUTE_2",
	347: "SEQ_BGM_PC",
	382: "SEQ_BGM_LAB",
	352: "SEQ_BGM_P_FOY",
	390: "SEQ_BGM_CAVE_GUARDIAN",
	436: "SEQ_BGM_P_TOL",
	437: "SEQ_BGM_P_DFOY",
	482: "SEQ_BGM_EYE_TT",
	483: "SEQ_BGM_EYE_TT_BOSS",
	486: "SEQ_BGM_EYE_GUARDIAN",
	500: "SEQ_BGM_EVENT_TT_RAID",
	501: "SEQ_BGM_INTRO",
	504: "SEQ_BGM_EVENT_DEOXYS",
	505: "SEQ_BGM_EVENT_TT_DANCE",
	506: "SEQ_BGM_SURF", }

map_namespaces = {
    88: 'MAP_HESPERIA',
    89: 'MAP_CARUN_CITY',
    90: 'MAP_URBANIA_CITY',
	91: 'MAP_HESPERIAPFAD',
	92: 'MAP_HESPERIAZWEIG',
	93: 'MAP_CARUNPFAD',
	94: 'MAP_YELNIAPFAD',
	95: 'MAP_WALD_VON_YELNIA',
	96: 'MAP_HESPERIAGRABEN',
	97: 'MAP_REBERATUNNEL',
	98: 'MAP_BAUM_DES_LEBENS',
	99: 'MAP_REBERA_GEBIRGE_OST',
	100: 'MAP_RUINE_DER_WAECHTER',
	101: 'MAP_TRAINERSCHULE',
	102: 'MAP_WALDHAIN', }

item_table = {
	  0 : "ITEM_NONE", }

# ------------------------------------------------------------------------------------------------------------------------------------------
# Flags
# ------------------------------------------------------------------------------------------------------------------------------------------
important_flag_table = {
	0x820 : "FLAG_ORDEN_1",
	0x821 : "FLAG_ORDEN_2",
	0x822 : "FLAG_ORDEN_3",
	0x823 : "FLAG_ORDEN_4",
	0x824 : "FLAG_ORDEN_5",
	0x825 : "FLAG_ORDEN_6",
	0x826 : "FLAG_ORDEN_7",
	0x827 : "FLAG_ORDEN_8",
	0x828 : "FLAG_PKMN_MENU",
	0x829 : "FLAG_POKEDEX",
	0x830 : "FLAG_TURBOTRETER", }

worldmap_flag_table = {
	0x6FF : "WORLDMAP_FLAG_HESPERIA",
	0x6FE : "WORLDMAP_FLAG_CARUN_CITY",
	0x6FD : "WORLDMAP_FLAG_URBANIA_CITY", }

sidequest_flag_table = {
	0x700: "VERSTECKTES_ITEM_X", }

story_flag_table = {
	0x500 : "FLAG_HIDDENALL",						# Versteckt NPCs beim Gamestart. Diese Flags ist gesetzt!
	0x501 : "FLAG_SCHOOL_MOVESPRITE",				# Schüler sind verstreut auf der Map, statt auf den Stühle.
	0x502 : "FLAG_HIDE_RIVAL_SCHOOL",				# Versteckt den Rivalen in der Trainerschule.
	0x503 : "FLAG_HIDE_RIVAL_SCHOOL_OUT",			# Versteckt den Rivalen am Eingang der Trainerschule.
	}

# ------------------------------------------------------------------------------------------------------------------------------------------
# Vars
# ------------------------------------------------------------------------------------------------------------------------------------------
important_var_table = {
	0x800F : "VAR_LASTTALKED",
	0x800D : "VAR_LASTRESULT",
	0x800C : "VAR_PLAYERFACING",
	0x4050 : "VAR_NOTSET",								# Diese Var benutze ich für Scripts, die immer ausgeführt werden.
	}

game_mod_var_table = {
	0x5050 : "VAR_MODI",								# Schwierigkeitsgrad
		0x0 : "MODI_LEICHT",
		0x1 : "MODI_MITTEL",
		0x2 : "MODI_SCHWER",
	}
	
story_var_table = {
	0x5051 : "VAR_STORYVERLAUF",						# Spielverlauf Variable, die Values bestimmen wo man ist.
		0x0 : "VALUE_UNTERRICHT_SCHULE",				# Spielstart in der Trainerschule Senseis Unterricht.
		0x1 : "VALUE_RIVALE_SCHULE_INDOOR",				# Das Gespräch mit dem Rivalen am Spint.
		0x2 : "VALUE_RIVALE_SCHULE_OUTDOOR",			# Das Gespräch draußen vor dem Eingang der Trainerschule mit dem Rivalen.
		0x3 : "VALUE_ZUM_LABOR",						# Spieler versucht Carn City zu verlassen. & Achim kommt den Spielern vor dem Labor entgegen
		0x4 : "VALUE_ERSTES_MAL_LABOR",					# Man betritt mit dem Rivalen das erste mal das Labor.
		0x5 : "VALUE_OHNE_POKE_LABOR",					# Man verlässt den hinterraum, ohne Pokémon.
		0x6 : "VALUE_MIT_POKE_LABOR",					# Man kommt mit einem Pokémon vom Hinterraum.
		0x7 : "VALUE_RIVALKAMPF_HESPERIAPFAD",			# Der erste Kampf gegen den Rivalen im Hesperiapfad.
	}	
	
# ------------------------------------------------------------------------------------------------------------------------------------------
# Banks & Maps
# ------------------------------------------------------------------------------------------------------------------------------------------
bank_list_table = {
	  0 : "BANKID_OUTDOOR",
	  1 : "BAMKID_ROUTE",
	  2 : "BANKID_UNTERWASSER",
	  3 : "BANKID_WAELDER_SUEMPFE",
	  4 : "BANKID_HOEHLE_GEBIRGE",
	  5 : "BANKID_LEGENDAERE",
	  6 : "BANKID_HEILIGE_ORTE",
	  7 : "BANKID_WICHTIGE_INDOOR",
	  8 : "BANKID_HESSPERIA_INDOOR",
	  9 : "BANKID_CARUN_CITY_INDOOR",
	  10 : "BANKID_URBANIA_CITY_INDOOR",
	  120 : "BANKID_DEBUG_TEST_START", }

map_outdoor = {
	  0 : "MAPID_HESPERIA_NORD",
	  1 : "MAPID_HESPERIA_SUED",
	  2 : "MAPID_CARUN_CITY",
	  3 : "MAPID_URBANIA_CITY_OST",
	  4 : "MAPID_URBANIA_CITY_WEST", }

map_route = {
	  0 : "MAPID_HESPERIAPFAD",
	  1 : "MAPID_HESPERIAZWEIG",
	  2 : "MAPID_CARUNPFAD",
	  3 : "MAPID_YELNIAPFAD", }

map_wald_suempfe = {
	  0 : "MAPID_LEBENDERWALD_YELNIA_1",
	  1 : "MAPID_LEBENDERWALD_YELNIA_2",
	  2 : "MAPID_LEBENDERWALD_YELNIA_3",
	  3 : "MAPID_LEBENDERWALD_YELNIA_4",
	  4 : "MAPID_LEBENDERWALD_YELNIA_5",
	  5 : "MAPID_LEBENDERWALD_YELNIA_6",
	  6 : "MAPID_LEBENDERWALD_YELNIA_7",
	  7 : "MAPID_LEBENDERWALD_YELNIA_8",
	  8 : "MAPID_LEBENDERWALD_YELNIA_9",
	  9 : "MAPID_LEBENDERWALD_YELNIA_RAETSEL_1",
	 10 : "MAPID_LEBENDERWALD_YELNIA_RAETSEL_2",
	 11 : "MAPID_LEBENDERWALD_YELNIA_RAETSEL_3",
	 12 : "MAPID_LEBENDERWALD_YELNIA_RAETSEL_4",
	 13 : "MAPID_LEBENDERWALD_YELNIA_RAETSEL_5",
	 14 : "MAPID_LEBENDERWALD_YELNIA_RAETSEL_6",
	 15 : "MAPID_LEBENDERWALD_YELNIA_RAETSEL_7",
	 16 : "MAPID_LEBENDERWALD_YELNIA_RAETSEL_8",
	 17 : "MAPID_LEBENDERWALD_YELNIA_RAETSEL_9",
	 18 : "MAPID_LEBENDERWALD_YELNIA_RAETSEL_10",
	 19 : "MAPID_LEBENDERWALD_YELNIA_RAETSEL_11",
	 20 : "MAPID_LEBENDERWALD_YELNIA_EINGANG_BAUM_DES_LEBENS",
	 21 : "MAPID_LEBENDERWALD_YELNIA_EINGANG_BAUM_DES_LEBENS_ERWACHT",
	 22 : "MAPID_TOTERWALD_YELNIA_1",
	 23 : "MAPID_TOTERWALD_YELNIA_2",
	 24 : "MAPID_TOTERWALD_YELNIA_AUSGANG",
	 25 : "MAPID_YELNIA_WALDHUETTE_EG",
	 26 : "MAPID_YELNIA_WALDHUETTE_SZ", }

map_hoehle_gebirge = {
	  0 : "MAPID_HESPERIAGRABEN_1",
	  1 : "MAPID_HESPERIAGRABEN_2",
	  2 : "MAPID_HESPERIAGRABEN_3",
	  3 : "MAPID_HESPERIAGRABEN_4",
	  4 : "MAPID_HESPERIAGRABEN_5",
	  5 : "MAPID_REBERATUNNEL", }

map_heilige_orte = {
	  0 : "MAPID_BAUM_DES_LEBENS_EINGANG",
	  1 : "MAPID_BAUM_DES_LEBENS_EBENE_1",
	  2 : "MAPID_BAUM_DES_LEBENS_EBENE_2",
	  3 : "MAPID_BAUM_DES_LEBENS_EBENE_3",
	  4 : "MAPID_BAUM_DES_LEBENS_EBENE_4",
	  5 : "MAPID_BAUM_DES_LEBENS_EBENE_5",
	  6 : "MAPID_BAUM_DES_LEBENS_EBENE_6",
	  7 : "MAPID_BAUM_DES_LEBENS_EBENE_7",
	  8 : "MAPID_BAUM_DES_LEBENS_EBENE_8",
	  9 : "MAPID_REBERA_GEBIRGE_OST_1",
	 10 : "MAPID_REBERA_GEBIRGE_OST_2",
	 11 : "MAPID_REBERA_GEBIRGE_OST_3",
	 12 : "MAPID_RUINE_DER_WAECHTER_1",
	 13 : "MAPID_RUINE_DER_WAECHTER_2",
	 14 : "MAPID_RUINE_DER_WAECHTER_3",
	 15 : "MAPID_RUINE_DER_WAECHTER_4",
	 16 : "MAPID_RUINE_DER_WAECHTER_5",
	 17 : "MAPID_RUINE_DER_WAECHTER_6",
	 18 : "MAPID_RUINE_DER_WAECHTER_7",
	 19 : "MAPID_RUINE_DER_WAECHTER_8", }

map_hesperia_maps = {
	  0 : "MAPID_SPIELERHAUS_EG",
	  1 : "MAPID_SPIELERHAUS_OG",
	  2 : "MAPID_HES_HAUS_1_EG",
	  3 : "MAPID_HES_HAUS_1_UG",
	  4 : "MAPID_HES_HAUS_2_EG",
	  5 : "MAPID_HES_HAUS_2_UG",
	  6 : "MAPID_HES_HAUS_3_EG",
	  7 : "MAPID_HES_HAUS_3_UG",
	  8 : "MAPID_HES_HAUS_4_EG",
	  9 : "MAPID_HES_HAUS_4_UG",
	 10 : "MAPID_HES_HAUS_5_EG",
	 11 : "MAPID_HES_HAUS_5_UG",
	 12 : "MAPID_HES_CENTER", }

map_carun_city_maps = {
	  0 : "MAPID_CAR_TRAINERSCHULE_OD",
	  1 : "MAPID_CAR_LABOR_VORDERRAUM",
	  2 : "MAPID_CAR_LABOR_HINTERRAUM",
	  3 : "MAPID_CAR_HAUS_1_EG",
	  4 : "MAPID_CAR_HAUS_1_UG",
	  5 : "MAPID_CAR_HAUS_2_EG",
	  6 : "MAPID_CAR_HAUS_2_UG",
	  7 : "MAPID_CAR_HAUS_3_EG",
	  8 : "MAPID_CAR_HAUS_3_UG",
	  9 : "MAPID_CAR_HAUS_4_EG",
	 10 : "MAPID_CAR_HAUS_4_UG",
	 11 : "MAPID_CAR_CENTER",
	 12 : "MAPID_CAR_TRAINERSCHULE_ID",
	 13 : "MAPID_CAR_VERBINDUNGSHAUS_CARUNPFAD",
	 14 : "MAPID_CAR_VERBINDUNGSHAUS_YELNIAPFAD", }

map_urbania_city_maps = {
	  0 : "MAPID_URBANI_CENTER",
	  1 : "MAPID_VERBINDUNGSHAUS_URBANIA_CITY",
	  2 : "MAPID_HAUS_1_EG",
	  3 : "MAPID_HAUS_1_OG_1",
	  4 : "MAPID_HAUS_1_OG_2",
	  5 : "MAPID_HAUS_1_OG_3",
	  6 : "MAPID_HAUS_2_EG",
	  7 : "MAPID_HAUS_2_OG",
	  8 : "MAPID_HAUS_3_EG",
	  9 : "MAPID_HAUS_3_OG",
	 10 : "MAPID_HAUS_4_EG",
	 11 : "MAPID_HAUS_4_OG",
	 12 : "MAPID_HAUS_5_EG",
	 13 : "MAPID_HAUS_5_OG_1",
	 14 : "MAPID_HAUS_5_OG_2",
	 15 : "MAPID_HAUS_6_EG",
	 16 : "MAPID_HAUS_6_OG",
	 17 : "MAPID_HAUS_7_EG",
	 18 : "MAPID_HAUS_7_OG_1",
	 19 : "MAPID_HAUS_7_OG_2",
	 20 : "MAPID_HAUS_7_OG_3",
	 21 : "MAPID_HAUS_7_OG_4",
	 22 : "MAPID_URBANIA_BIB_EG",
	 23 : "MAPID_URBANIA_BIB_OG",
	 24 : "MAPID_URBANIA_CAFE",
	 25 : "MAPID_URBANIA_RESTERAUNT",
	 26 : "MAPID_URBANIA_ARENA_1",
	 27 : "MAPID_URBANIA_ARENA_2",
	 28 : "MAPID_URBANIA_ARENA_3", }

map_debug_test_startmap = {
	  0 : "MAPID_STARTMAP_INTRO", }

# ------------------------------------------------------------------------------------------------------------------------------------------
# NPC Table & Sprite
# ------------------------------------------------------------------------------------------------------------------------------------------
npc_sprite_table1 = {
	0: 'NPC_SPIELER',
	1: 'NPC_SPIELER_RAD',
	2: 'NPC_SPIELER_SITZT',
	3: 'NPC_SPIELER_NUTZT',
	4: 'NPC_SPIELER_ANGEL',
	5: 'NPC_SPIELER_NUTZT_2',
	6: 'NPC_SPIELER_NUTZT_RAD',
	7: 'NPC_SPIELERIN',
	8: 'NPC_SPIELERIN_RAD',
	9: 'NPC_SPIELERIN_SITZT',
	10: 'NPC_SPIELERIN_NUTZT',
	11: 'NPC_SPIELERIN_ANGEL',
	12: 'NPC_SPIELERIN_NUTZT_2',
	13: 'NPC_SPIELERIN_NUTZT_RAD',
	14: 'NPC_PSYCHO_M',
	15: 'NPC_PSYCHO_W',
	16: 'NPC_ASS_TRAINER_M',
	17: 'NPC_ASS_TRAINER_W',
	18: 'NPC_CAMPER',
	19: 'NPC_PICKNICKER',
	20: 'NPC_VOGELFAENGER_M',
	21: 'NPC_VOGELFAENGER_W',
	22: 'NPC_EXPERTE_M',
	23: 'NPC_EXPERTE_W',
	24: 'NPC_SCHNOESEL',
	25: 'NPC_LADY',
	26: 'NPC_SCHWARZGURT',
	27: 'NPC_KAEMPFERIN',
	28: 'NPC_GITARRIST_M',
	29: 'NPC_GITARRIST_W',
	30: 'NPC_BIKER_M',
	31: 'NPC_BIKER_W',
	32: 'NPC_GENTLEMAN',
	33: 'NPC_DAME',
	34: 'NPC_PKMN_ZUECHTER_M',
	35: 'NPC_PKMN_ZUECHTER_W',
	36: 'NPC_PKMN_RANGER_M',
	37: 'NPC_PKMN_RANGER_W',
	38: 'NPC_SCHUELER_M',
	39: 'NPC_SCHUELER_W',
	40: 'NPC_TEENAGER',
	41: 'NPC_GOERE',
	42: 'NPC_SCHIRMDAME',
	43: 'NPC_MODEL',
	44: 'NPC_SCHOENHEIT',
	45: 'NPC_HEXE',
	46: 'NPC_FARMER',
	47: 'NPC_COWGIRL',
	48: 'NPC_SKIFAHRER_M',
	49: 'NPC_JOGGER_W',
	50: 'NPC_FORSCHER_M',
	51: 'NPC_FORSCHER_W',
	52: 'NPC_POKEFAN_M',
	53: 'NPC_POKEFAN_W',
	54: 'NPC_VETERAN_M',
	55: 'NPC_VETERAN_W',
	56: 'NPC_ANGESTELLTER_W',
	57: 'NPC_ANGESTELLTER_M',
	58: 'NPC_BACKPACKER_M',
	59: 'NPC_BACKPACKER_W',
	60: 'NPC_PFLEGER_M',
	61: 'NPC_PFLEGER_W',
	62: 'NPC_VORSCHULKIND_M',
	63: 'NPC_VORSCHULKIND_W',
	64: 'NPC_INTERVIEWER_M',
	65: 'NPC_INTERVIEWER_W',
	66: 'NPC_SCHWIMMER_M',
	67: 'NPC_SCHWIMMER_W',
	68: 'NPC_SCHWIMMER_M_WASSER',
	69: 'NPC_SCHWIMMER_W_WASSER',
	70: 'NPC_KIND1',
	71: 'NPC_ZWILLING',
	72: 'NPC_PLANSCHER_M_WASSER',
	73: 'NPC_PLANSCHER_W_WASSER',
	74: 'NPC_SNOWBOARDER',
	75: 'NPC_SKIFAHRER_W',
	76: 'NPC_RAUFBOLD',
	77: 'NPC_ROWDY',
	78: 'NPC_HITZKOPF',
	79: 'NPC_FEUERSPUCKER',
	80: 'NPC_JUNGES_GLUECK_M',
	81: 'NPC_JUNGES_GLUECK_W',
	82: 'NPC_KAEFERSAMMLER',
	83: 'NPC_AROMALADY',
	84: 'NPC_NINJAJUNGE',
	85: 'NPC_PLANSCHER_M',
	86: 'NPC_PLANSCHER_W',
	87: 'NPC_WANDERER',
	88: 'NPC_ANGLER',
	89: 'NPC_ARBEITER1',
	90: 'NPC_ARBEITER2',
	91: 'NPC_POLIZIST',
	92: 'NPC_WACHE',
	93: 'NPC_ELEKTRIKER',
	94: 'NPC_MATROSE',
	95: 'NPC_DRACHENPROFI',
	96: 'NPC_POKEMANIAC',
	97: 'NPC_SAMMLER',
	98: 'NPC_JONGLEUR',
	99: 'NPC_DIEB',
	100: 'NPC_INFORMATIKER',
	101: 'NPC_JOGGER_M',
	102: 'NPC_ZOFFE',
	103: 'NPC_SERVIERER_W',
	104: 'NPC_SERVIERER_M',
	105: 'NPC_MALER',
	106: 'NPC_BAECKER',
	107: 'NPC_ERZIEHERIN',
	108: 'NPC_TAENZER',
	109: 'NPC_LOCKFUEHRER',
	110: 'NPC_PILOT',
	111: 'NPC_HAUSMEISTER',
	112: 'NPC_CLOWN',
	113: 'NPC_GITARRIST2',
	114: 'NPC_ANHAENGER_M',
	115: 'NPC_ANHAENGER_W',
	116: 'NPC_BASEBALLER',
	117: 'NPC_KORBLEGER',
	118: 'NPC_FOOTBALLER',
	119: 'NPC_FUSSBALLER',
	120: 'NPC_TENNIS_ASS',
	121: 'NPC_RUINENMANIAC',
	122: 'NPC_TEENEGER2',
	123: 'NPC_MAEDCHEN1',
	124: 'NPC_MAEDCHEN2',
	125: 'NPC_VATER1',
	126: 'NPC_MUTTER1',
	127: 'NPC_OMA1',
	128: 'NPC_AGENT',
	129: 'NPC_MUTTER2',
	130: 'NPC_MUTTER3',
	131: 'NPC_AFRO_GELBE_HAARE',
	132: 'NPC_FORSCHER2',
	133: 'NPC_VATER2',
	134: 'NPC_OPA1',
	135: 'NPC_OPA2',
	136: 'NPC_OPA3',
	137: 'NPC_VATER3',
	138: 'NPC_TEENAGER3',
	139: 'NPC_TEENAGER4',
	140: 'NPC_MAEDCHEN3',
	141: 'NPC_TEENAGER5',
	142: 'NPC_VATER3',
	143: 'NPC_KLEINES_MAEDCHEN',
	144: 'NPC_TEENAGER6',
	145: 'NPC_MANN1',
	146: 'NPC_MANN2',
	147: 'NPC_MANN3',
	148: 'NPC_CAPITAN_SCHWARZ',
	149: 'NPC_KOCH',
	150: 'NPC_TEENAGER7',
	151: 'NPC_TEENAGER2',
	152: 'NPC_OMA4',
	153: 'NPC_OPA_GELBE_HAARE',
	154: 'NPC_CAPITAN_WEISS',
	155: 'NPC_FORSCHER3',
	156: 'NPC_VERBINDUNGSHAUS_M',
	157: 'NPC_VERBINDUNGSHAUS_W',
	158: 'NPC_HEADSET1_W',
	159: 'NPC_HEADSET1_M',
	160: 'NPC_EMPFANGSDAME_GRUEN',
	161: 'NPC_EMPFANGSDAME_ROT',
	162: 'NPC_HEADSET2_W',
	163: 'NPC_HEADSET3_W',
	164: 'NPC_PACKETBOTE',
	165: 'NPC_WAECHTER2',
	166: 'NPC_VERKAEUFER',
	167: 'NPC_SCHWESTER_JOY',
	168: 'NPC_GAMER',
	169: 'NPC_SACHSOFON',
	170: 'NPC_FLOETIST_W',
	171: 'NPC_FLOETIST_M',
	172: 'NPC_GEIGE',
	173: 'NPC_GITARRIST3',
	174: 'NPC_IDAN',
	175: 'NPC_LINDA',
	176: 'NPC_ACHIM',
	177: 'NPC_TUNDRA_RUEPEL_M',
	178: 'NPC_TUNDRA_RUEPEL_W',
	179: 'NPC_MARKUS',
	180: 'NPC_NADINE',
	181: 'NPC_JANA',
	182: 'NPC_NORMAN',
	183: 'NPC_LEVIN',
	184: 'NPC_DIANA',
	185: 'NPC_FLORIAN',
	186: 'NPC_DAMIAN',
	187: 'NPC_JASMINE',
	188: 'NPC_LENA',
	189: 'NPC_PAUL',
	190: 'NPC_HEILO',
	191: 'NPC_FABIOLA',
	192: 'NPC_AARON',
	193: 'NPC_PROFESSOR1_M',
	194: 'NPC_PROFESSOR2_M',
	195: 'NPC_TUNDRA_SPION',
	196: 'NPC_PROFESSOR1_W',
	238: 'NPC_RIVALE', }

npc_sprite_table2 = {
	0: 'NPC_LAPRAS',
	1: 'NPC_GENGAR',
	2: 'NPC_STALOBOR',
	3: 'NPC_LUCARIO',
	4: 'NPC_GUARDEVOIR',
	5: 'NPC_ABSOL',
	6: 'NPC_GLURAK',
	7: 'NPC_PINSIR',
	8: 'NPC_AERODACTYL',
	9: 'NPC_NAGELLOTZ',
	10: 'NPC_YORKLEFF',
	11: 'NPC_OHRDOCH',
	12: 'NPC_GRILLMARK',
	13: 'NPC_SODAMARK',
	14: 'NPC_VEGIMARK',
	15: 'NPC_FELILOU',
	16: 'NPC_KLEOPARDA',
	17: 'NPC_MILZA',
	18: 'NPC_ZORUA',
	19: 'NPC_BISASAM',
	20: 'NPC_GLUMANDA',
	21: 'NPC_SCHIGGY',
	22: 'NPC_RATTFRATZ',
	23: 'NPC_TAUBSI',
	24: 'NPC_HABITAK',
	25: 'NPC_PIKACHU',
	26: 'NPC_RAICHU',
	27: 'NPC_NIDORAN_W',
	28: 'NPC_NIDORAN_M',
	29: 'NPC_PUMMELLUF',
	30: 'NPC_PIEPI',
	31: 'NPC_VULPIX',
	32: 'NPC_MAUZI',
	33: 'NPC_ENTON',
	34: 'NPC_FURKANO',
	35: 'NPC_QUAPSEL',
	36: 'NPC_MACHOLO',
	37: 'NPC_FLEGMON',
	38: 'NPC_PORENTA',
	39: 'NPC_MAGNETILO',
	40: 'NPC_CHANEIRA',
	41: 'NPC_TRAGOSSO',
	42: 'NPC_EVOLI',
	43: 'NPC_AQUANA',
	44: 'NPC_BLITZA',
	45: 'NPC_FLAMARA',
	46: 'NPC_PSIANA',
	47: 'NPC_NACHTARA',
	48: 'NPC_FOLIPURBA',
	49: 'NPC_GLAZIOLA',
	50: 'NPC_ISSO',
	51: 'NPC_MAMPFAXO',
	52: 'NPC_DRATINI',
	53: 'NPC_HOOTHOOT',
	54: 'NPC_PICHU',
	55: 'NPC_TOGEPI',
	56: 'NPC_NATU',
	57: 'NPC_VOLTILAMM',
	58: 'NPC_WAATY',
	59: 'NPC_AMPHAROS',
	60: 'NPC_AZURILL',
	61: 'NPC_MARIL',
	62: 'NPC_AZUMARILL',
	63: 'NPC_QUAXO',
	64: 'NPC_GRIFFEL',
	65: 'NPC_FELINO',
	66: 'NPC_HUNDUSTER',
	67: 'NPC_HUNDEMON',
	68: 'NPC_FIFFYEN',
	69: 'NPC_MAGNAYEN',
	70: 'NPC_ZIGZACHS',
	71: 'NPC_GERADACHS',
	72: 'NPC_LARVITAR',
	73: 'NPC_GECKARBOR',
	74: 'NPC_FLEMMLI',
	75: 'NPC_HYDROPI',
	76: 'NPC_LOTURZEL',
	77: 'NPC_SAMURZEL',
	78: 'NPC_SCHWALBINI',
	79: 'NPC_WINGULL',
	80: 'NPC_PELIPPER',
	81: 'NPC_BUMMELZ',
	82: 'NPC_ENECO',
	83: 'NPC_ENECORO',
	84: 'NPC_PLUSLE',
	85: 'NPC_MINUN',
	86: 'NPC_WATTZAPF',
	87: 'NPC_VOLTULA',
	88: 'NPC_RAUPY',
	89: 'NPC_SMETTPO',
	90: 'NPC_HORNLIU',
	91: 'NPC_BIBOR',
	92: 'NPC_WEBARAK',
	93: 'NPC_ARIADOS',
	94: 'NPC_WAUMPEL',
	95: 'NPC_PAPINELLA',
	96: 'NPC_PUDOX',
	97: 'NPC_GEHWEIEHER',
	98: 'NPC_MASKEREGEN',
	99: 'NPC_SANDAN',
	100: 'NPC_SANAMER',
	101: 'NPC_DIGDA',
	102: 'NPC_DIGDRI',
	103: 'NPC_SMOGON',
	104: 'NPC_SMOGMOG',
	105: 'NPC_NEBULAK',
	106: 'NPC_ALPOLLO',
	107: 'NPC_KRABBY',
	108: 'NPC_KREBSCOURPS',
	109: 'NPC_RIHORN',
	110: 'NPC_ELEKTEK',
	111: 'NPC_MAGMAR',
	112: 'NPC_TAUROS',
	113: 'NPC_SCHEROX',
	114: 'NPC_TUSKA',
	115: 'NPC_WABLU',
	116: 'NPC_SENGO',
	117: 'NPC_TRASLA',
	118: 'NPC_KNILZ',
	119: 'NPC_KAPILZ',
	120: 'NPC_KNACKRACK',
	121: 'NPC_CAMAUB',
	122: 'NPC_CAMERUPT',
	123: 'NPC_KINDWURM',
	124: 'NPC_DRACHSEL',
	125: 'NPC_BRUTALANDA',
	126: 'NPC_TANHEL',
	127: 'NPC_METANG',
	128: 'NPC_METAGROSS',
	129: 'NPC_STARALILI',
	130: 'NPC_STARAVIA',
	131: 'NPC_BIDIZA',
	132: 'NPC_BIDIFAS',
	133: 'NPC_SHEINUX',
	134: 'NPC_LUXIO',
	135: 'NPC_LUXTRA',
	136: 'NPC_KOKNODON',
	137: 'NPC_SCHILTERUS',
	138: 'NPC_WADRIBE',
	139: 'NPC_HONWEISEL',
	140: 'NPC_PACHIRUSU',
	141: 'NPC_BAMELIN',
	142: 'NPC_AMBIDIFFEL',
	143: 'NPC_HASPIROR',
	144: 'NPC_CHARMIAN',
	145: 'NPC_SCHNURRGAST',
	146: 'NPC_WONNEIRA',
	147: 'NPC_PLAUDAGEI',
	148: 'NPC_RIOLU',
	149: 'NPC_HIPPOTAS_W',
	150: 'NPC_HIPPOTAS_M',
	151: 'NPC_HIPPOTERUS_W',
	152: 'NPC_HIPPOTERUS_M',
	153: 'NPC_GLIBUNKEL',
	154: 'NPC_STOLLUNUIOR',
	155: 'NPC_FIRTZELBLITZ',
	156: 'NPC_ZUBAT',
	157: 'NPC_GOLBAT',
	158: 'NPC_IKSBAT',
	159: 'NPC_QUICKEL',
	160: 'NPC_KEIFEL',
	161: 'NPC_MAMUTEL',
	162: 'NPC_SEEMOPS',
	163: 'NPC_SEEJONG',
	164: 'NPC_WALRAISA',
	165: 'NPC_SCHNEPKE',
	166: 'NPC_FIRNONTOR',
	167: 'NPC_FROSDEDJE',
	168: 'NPC_SHNEBEDECK',
	169: 'NPC_RESBILSAR',
	170: 'NPC_SNIEBEL',
	171: 'NPC_SNIBUNNA',
	172: 'NPC_SEEJONG',
	173: 'NPC_AUSTOSS',
	174: 'NPC_KIRLIA',
	175: 'NPC_GALAGLADI',
	176: 'NPC_GANOVIL',
	177: 'NPC_ROKKAIMAN',
	178: 'NPC_RABIGATOR',
	179: 'NPC_LATAERNCO',
	180: 'NPC_GARAOS',
	181: 'NPC_SNUBULL',
	182: 'NPC_TEDIURSA',
	183: 'NPC_PHANPY',
	184: 'NPC_MILTANK', }

npc_sprite_table3 = {
	0: 'NPC_ARKTOS',
	1: 'NPC_ZAPDOS',
	2: 'NPC_LAVADOS',
	3: 'NPC_MEWTU',
	4: 'NPC_MEW',
	5: 'NPC_RAIKOU',
	6: 'NPC_ENTEI',
	7: 'NPC_SUICUNE',
	8: 'NPC_LUGIA',
	9: 'NPC_HO_OH',
	10: 'NPC_CELEBIE',
	11: 'NPC_REGIROCK',
	12: 'NPC_REGICE',
	13: 'NPC_REGISTEEL',
	14: 'NPC_LATIAS',
	15: 'NPC_LATIOS',
	16: 'NPC_KYOGRE',
	17: 'NPC_GROUDON',
	18: 'NPC_RAYQUAZA',
	19: 'NPC_JIRACHI',
	20: 'NPC_DEOXYS_NORMALFORM',
	21: 'NPC_SELFE',
	22: 'NPC_VESPRIT',
	23: 'NPC_TOBUTZ',
	24: 'NPC_DIALGA',
	25: 'NPC_PALKIA',
	26: 'NPC_HEATARAN',
	27: 'NPC_REGIGIGAS',
	28: 'NPC_GIRATINA',
	29: 'NPC_CRESSELIA',
	30: 'NPC_PHIONE',
	31: 'NPC_MANAPHY',
	32: 'NPC_DARKAI',
	33: 'NPC_SHAYMIN',
	34: 'NPC_ARCEUS',
	35: 'NPC_VICTINI',
	36: 'NPC_KOBALIUM',
	37: 'NPC_TERRAKIUM',
	38: 'NPC_VIRIDIUM',
	39: 'NPC_BOREOS',
	40: 'NPC_VOLTOLOS',
	41: 'NPC_DEMETREOS',
	42: 'NPC_RESHIRAM',
	43: 'NPC_ZEKROM',
	44: 'NPC_KYUREM',
	45: 'NPC_KELDEO',
	46: 'NPC_MELOETTA',
	47: 'NPC_GENESECT',
	48: 'NPC_XERENEAS',
	49: 'NPC_YVETEL',
	50: 'NPC_ZYGARDE',
	51: 'NPC_DIANCIE',
	52: 'NPC_HOOPA',
	53: 'NPC_VOLCANION', }
	
npc_sprite_table4 = {
	0: 'NPC_ZERSCHNEIDERBAUM_ARENA',
	1: 'NPC_ZERTRUEMMERERSTEIN',
	2: 'NPC_ZERTRUEMMERERWAND',
	3: 'NPC_STAERKESTEIN',
	4: 'NPC_STAERKESTAHLSTEIN',
	5: 'NPC_METEORIT',
	6: 'NPC_POKEDEX',
	7: 'NPC_MEGASTEINFUNKEL',
	8: 'NPC_SEELENTAU_GANZ',
	9: 'NPC_POKEBALL',
	10: 'NPC_POKEBALL_FUER_TM',
	11: 'NPC_SEGELBOOT',
	12: 'NPC_SCHIFF',
	13: 'NPC_WIBELWIND',
	14: 'NPC_BLITZ',
	15: 'NPC_FEUEREXPLOSION',
	16: 'NPC_FEUERANGRIFF',
	17: 'NPC_RACKETE_UNTEN',
	18: 'NPC_RACKETE_OBEN',
	19: 'NPC_XERENEAS_VERSTEINERT',
	20: 'NPC_LATIOS_IM_KRISTALL',
	21: 'NPC_LATIAS_IM_KRISTALL',
	22: 'NPC_ZERSCHNEIDERBAUM',
	23: 'NPC_GROSSER_ZERSCHNEIDERBAUM',
	24: 'NPC_ZERSCHNEIDER_ANIMATION', }

# ------------------------------------------------------------------------------------------------------------------------------------------
# Pymap Konstanten
# ------------------------------------------------------------------------------------------------------------------------------------------
map_connections = [
	"ANB_KEINS",
	"ANB_UNTEN",
	"ANB_OBEN",
	"ANB_LINKS",
	"ANB_RECHTS",
	"ANB_ABTAUCHEN",
	"ANB_AUFTAUCHEN"]

behaviours = [
    'BEH_KEINE_BEWEGUNG',
    'BEH_UMHERBLICKEN',
    'BEH_HERUMGEHEN',
    'BEH_GEHE_AUF_AB',
    'BEH_GEHE_AUF_AB2',
    'BEH_GEHE_HIN_HER',
    'BEH_GEHE_HIN_HER2',
    'BEH_BLICKE_OBEN',
    'BEH_BLICKE_UNTEN',
    'BEH_BLICKE_LINKS',
    'BEH_BLICKE_RECHTS',
    'BEH_ERROR',
    'BEH_VERSTECKT',
    'BEH_BLICKE_OBEN_UNTEN',
    'BEH_BLICKE_LINKS_RECHTS',
    'BEH_BLICKE_OBEN_LINKS',
    'BEH_BLICKE_OBEN_RECHTS',
    'BEH_BLICKE_UNTEN_LINKS',
    'BEH_BLICKE_UNTEN_RECHTS',
    'BEH_BLICKE_OBEN_UNTEN_LINKS',
    'BEH_BLICKE_OBEN_UNTEN_RECHTS',
    'BEH_BLICKE_OBEN_LINKS_RECHTS',
    'BEH_BLICKE_UNTEN_LINKS_RECHTS',
    'BEH_BLICKE_GEGEN_UHRZEIGERSINN',
    'BEH_BLICKE_IM_UHRZEIGERSINN',
    'BEH_LAUFE_AUF_AB',
    'BEH_LAUFE_AUF_AB2',
    'BEH_LAUFE_HIN_HER',
    'BEH_LAUFE_HIN_HER2',
    'BEH_LAUFE_HOCH_RECHTS_LINKS_RUNTER',
    'BEH_LAUFE_RECHTS_LINKS_HOCH_RUNTER',
    'BEH_LAUFE_RUNTER_HOCH_RECHTS_LINKS',
    'BEH_LAUFE_LINKS_RUNTER_HOCH_RECHTS',
    'BEH_LAUFE_HOCH_LINKS_RECHTS_RUNTER',
    'BEH_LAUFE_LINKS_RECHTS_RUNTER_HOCH',
    'BEH_LAUFE_RUNTER_HOCH_LINKS_RECHTS',
    'BEH_LAUFE_RECHTS_RUNTER_HOCH_LINKS',
    'BEH_LAUFE_LINKS_HOCH_RUNTER_RECHTS',
    'BEH_LAUFE_HOCH_RUNTER_RECHTS_LINKS',
    'BEH_LAUFE_RECHTS_LINKS_HOCH_RUNTER2',
    'BEH_LAUFE_RUNTER_RECHTS_LINKS_HOCH',
    'BEH_LAUFE_RECHTS_HOCH_RUNTER_LINKS',
    'BEH_LAUFE_HOCH_RUNTER_LINKS_RECHTS',
    'BEH_LAUFE_LINKS_RECHTS_HOCH_RUNTER',
    'BEH_LAUFE_RUNTER_LINKS_RECHTS_HOCH',
    'BEH_LAUFE_GEGEN_UHRZEIGERSINN',
    'BEH_LAUFE_GEGEN_UHRZEIGERSINN2',
    'BEH_LAUFE_GEGEN_UHRZEIGERSINN3',
    'BEH_LAUFE_GEGEN_UHRZEIGERSINN4',
    'BEH_LAUFE_GEGEN_UHRZEIGERSINN5',
    'BEH_LAUFE_UHRZEIGERSINN',
    'BEH_LAUFE_UHRZEIGERSINN2',
    'BEH_LAUFE_UHRZEIGERSINN3',
    'BEH_SPIELER_KOPIEREN',
    'BEH_SPIELER_SPIEGELN',
    'BEH_SPIELER_SPIEGELN2',
    'BEH_SPIELER_SPIEGELN3',
    'BEH_BAUM_WAND_VERKLEIDUNG',
    'BEH_FELS_WAND_VERKLEIDUNG',
    'BEH_SPIELER_SPIEGELN_STAND',
    'BEH_SPIELER_KOPIEREN_STAND2',
    'BEH_SPIELER_SPIEGELN_STAND3',
    'BEH_SPIELER_SPIEGELN_STAND4',
    'BEH_VERSTECKT2',
    'BEH_STELLE_GEHEN_UNTEN',
    'BEH_STELLE_GEHEN_OBEN',
    'BEH_STELLE_GEHEN_LINKS',
    'BEH_STELLE_GEHEN_RECHTS',
    'BEH_STELLE_JOGGEN_UNTEN',
    'BEH_STELLE_JOGGEN_OBEN',
    'BEH_STELLE_JOGGEN_LINKS',
    'BEH_STELLE_JOGGEN_RECHTS',
    'BEH_STELLE_LAUFEN_UNTEN',
    'BEH_STELLE_LAUFEN_OBEN',
    'BEH_STELLE_LAUFEN_LINKS',
    'BEH_STELLE_LAUFEN_RECHTS',
    'BEH_VERSTECKT_THREE',
    'BEH_STELLE_GEHEN_UNTEN2',
    'BEH_STELLE_GEHEN_OBEN2',
    'BEH_STELLE_GEHEN_LINKS2',
    'BEH_STELLE_GEHEN_RECHTS2' ]

map_show_name = {
	0 : "NAMEN_NICHT_ANZEIGEN",
	1 : "NAMEN_ANZEIGEN",
	6 : "NAMEN_DORF_ANZEIGEN",
	7 : "NAMEN_ORT_ANZEIGEN",
	0xD : "NAMEN_STADT_ANZEIGEN" }

flash_types = [
	"BLITZ_NEIN", "BLITZ_EINSETZBAR", "BLITZ_NICHT_EINSETZBAR" ]

map_weather = [
	"WEATHER_INNEN",
	"WEATHER_SONNIG_MIT_WOLKEN_IM_WASSER",
	"WEATHER_DRAUSSEN",
	"WEATHER_REGEN",
	"WEATHER_DREI_SCHNEEFLOCKEN",
	"WEATHER_GEWITTER",
	"WEATHER_NEBEL",
	"WEATHER_SCHNEE",
	"WEATHER_SANDSTURM",
	"WEATHER_NEBEL_RECHTS",
	"WEATHER_HELLER_NEBEL",
	"WEATHER_DUNKEL",
	"WEATHER_UNTERGRUND_BINKT",
	"WEATHER_STARKES_GEWITTER",
	"WEATHER_UNTWERWASSER",
	"WEATHER_0F"]

map_types = [
	"MAP_TYPE_NORMAL",
	"MAP_TYPE_DORF",
	"MAP_TYPE_STADT",
	"MAP_TYPE_ROUTE",
	"MAP_TYPE_HOEHLE",
	"MAP_TYPE_UNTERWASSER",
	"MAP_TYPE_TYPE_06",
	"MAP_TYPE_TYPE_07",
	"MAP_TYPE_INNEN",
	"MAP_TYPE_GEHEIMBASIS" ]

battle_types = [
	"BATTLE_TYPE_ZUFALL",
	"BATTLE_TYPE_ARENA",
	"BATTLE_TYPE_TEAM_ROCKET",
	"BATTLE_TYPE_03",
	"BATTLE_TYPE_TOP_VIER1",
	"BATTLE_TYPE_TOP_VIER2",
	"BATTLE_TYPE_TOP_VIER3",
	"BATTLE_TYPE_TOP_VIER4",
	"BATTLE_TYPE_GROSSER_POKEBALL" ]

ebene_type_table = {
	0: "EBENE_IMMER",
	1: "EBENE_SUFER",
	3: "EBENE_NORMAL",
	4: "EBENE_BRUECKE" }

signpost_type_table = {
	0: "SIGN_IMMER",
	1: "SIGN_OBEN",
	2: "SIGN_UNTEN",
	3: "SIGN_RECHTS",
	4: "SIGN_LINKS",
	7: "SIGN_VERSTECKTES_ITEM" }

pchar_dict = {
	"PCHAR_SPACE":0x0,
	"PCHAR_0":0xA1,
	"PCHAR_1":0xA2,
	"PCHAR_2":0xA3,
	"PCHAR_3":0xA4,
	"PCHAR_5":0xA6,
	"PCHAR_6":0xA7,
	"PCHAR_7":0xA8,
	"PCHAR_8":0xA9,
	"PCHAR_9":0xAA,
	"PCHAR_EXCLAM":0xAB,
	"PCHAR_QUESTION":0xAC,
	"PCHAR_DOT":0xAD,
	"PCHAR_DOTS":0xAF,
	"PCHAR_MINUS":0xAE,
	"PCHAR_COMMA":0xB8,
	"PCHAR_PLUS":0x2E,
	"PCHAR_SLASH":0xBA,
	"PCHAR_A":0xBB,
	"PCHAR_B":0xBC,
	"PCHAR_C":0xBD,
	"PCHAR_D":0xBE,
	"PCHAR_E":0xBF,
	"PCHAR_F":0xC0,
	"PCHAR_G":0xC1,
	"PCHAR_H":0xC2,
	"PCHAR_I":0xC3,
	"PCHAR_J":0xC4,
	"PCHAR_K":0xC5,
	"PCHAR_L":0xC6,
	"PCHAR_M":0xC7,
	"PCHAR_N":0xC8,
	"PCHAR_O":0xC9,
	"PCHAR_P":0xCA,
	"PCHAR_Q":0xCB,
	"PCHAR_R":0xCC,
	"PCHAR_S":0xCD,
	"PCHAR_T":0xCE,
	"PCHAR_U":0xCF,
	"PCHAR_V":0xD0,
	"PCHAR_W":0xD1,
	"PCHAR_X":0xD2,
	"PCHAR_Y":0xD3,
	"PCHAR_Z":0xD4,
	"PCHAR_a":0xD5,
	"PCHAR_b":0xD6,
	"PCHAR_c":0xD7,
	"PCHAR_d":0xD8,
	"PCHAR_e":0xD9,
	"PCHAR_f":0xDA,
	"PCHAR_g":0xDB,
	"PCHAR_h":0xDC,
	"PCHAR_i":0xDD,
	"PCHAR_j":0xDE,
	"PCHAR_k":0xDF,
	"PCHAR_l":0xE0,
	"PCHAR_m":0xE1,
	"PCHAR_n":0xE2,
	"PCHAR_o":0xE3,
	"PCHAR_p":0xE4,
	"PCHAR_q":0xE5,
	"PCHAR_r":0xE6,
	"PCHAR_s":0xE7,
	"PCHAR_t":0xE8,
	"PCHAR_u":0xE9,
	"PCHAR_v":0xEA,
	"PCHAR_w":0xEB,
	"PCHAR_x":0xEC,
	"PCHAR_y":0xED,
	"PCHAR_z":0xEE,
	"PCHAR_SHARP":0x7F,
	"PCHAR_AE":0xF1,
	"PCHAR_OE":0xF2,
	"PCHAR_UE":0xF3,
	"PCHAR_ae":0xF4,
	"PCHAR_oe":0xF5,
	"PCHAR_ue":0xF6,
	"PCHAR_WAIT":0xFC,
	"PCHAR_BUFFER":0xFD,
	"PCHAR_LINE_SCROLL":0xFA,
	"PCHAR_PARAGRAPH":0xFB,
	"PCHAR_NEW_LINE":0xFE,
	"PCHAR_POKE_E":0x1B,
	"PCHAR_PARANTHESIS_START":0x5C,
	"PCHAR_PARANTHESIS_END":0x5D,
	"PCHAR_COLON":0xF0 }

# ------------------------------------------------------------------------------------------------------------------------------------------
# Codegerüst
# ------------------------------------------------------------------------------------------------------------------------------------------
def item(id):
	try: return item_table[id]
	except: return hex(id)

def ebene_type(id):
	try: return ebene_type_table[id]
	except: return hex(id)

def signpost_type(id):
	try: return signpost_type_table[id]
	except: return hex(id)

def bank_table(id):
	try: return bank_list_table[id]
	except: return hex(id)

def important_flag(id):
	try: return important_flag_table[id]
	except: return hex(id)

def worldmap_flag(id):
	try: return worldmap_flag_table[id]
	except: return hex(id)

def sidequest_flag(id):
	try: return sidequest_flag_table[id]
	except: return hex(id)

def story_flag(id):
	try: return story_flag_table[id]
	except: return hex(id)

def important_var(id):
	try: return important_var_table[id]
	except: return hex(id)

def game_mod_var(id):
	try: return game_mod_var_table[id]
	except: return hex(id)

def story_var(id):
	try: return story_var_table[id]
	except: return hex(id)

def npc1(id):
	try: return npc_sprite_table1[id]
	except: return hex(id)

def npc2(id):
	try: return npc_sprite_table2[id]
	except: return hex(id)

def npc3(id):
	try: return npc_sprite_table3[id]
	except: return hex(id)

def npc4(id):
	try: return npc_sprite_table4[id]
	except: return hex(id)

def bank0(id):
	try: return map_outdoor[id]
	except: return hex(id)

def bank1(id):
	try: return map_route[id]
	except: return hex(id)

def bank3(id):
	try: return map_wald_suempfe[id]
	except: return hex(id)

def bank4(id):
	try: return map_hoehle_gebirge[id]
	except: return hex(id)

def bank6(id):
	try: return map_heilige_orte[id]
	except: return hex(id)

def bank8(id):
	try: return map_hesperia_maps[id]
	except: return hex(id)

def bank9(id):
	try: return map_carun_city_maps[id]
	except: return hex(id)

def bank10(id):
	try: return map_urbania_city_maps[id]
	except: return hex(id)

def bank120(id):
	try: return map_debug_test_startmap[id]
	except: return hex(id)

def values(_d):
	if isinstance(_d, dict): return _d.values()
	return _d

def _dict_get(_d, key, hexstr=True, _str=True):
	""" Returns a string from a dict in this module if a key is present else simply the key """
	if key in _d: return _d[key]
	if hexstr: return hex(key)
	if _str: return str(key)
	return key

def byte_to_pchar(byte):
	for pchar in pchar_dict:
		if pchar_dict[pchar] == byte: return pchar
	return hex(byte)

def _mkdirs(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

def export_macros(lib, dir):
	""" Exports several macros into a directory """
	_mkdirs(dir)
	macros = [
		_export_generic_macros_from_dict(lib, dir, "important_flag", important_flag_table),
		_export_generic_macros_from_dict(lib, dir, "worldmap_flag", worldmap_flag_table),
		_export_generic_macros_from_dict(lib, dir, "sidequest_flag", sidequest_flag_table),
		_export_generic_macros_from_dict(lib, dir, "story_flag", story_flag_table),
		_export_generic_macros_from_dict(lib, dir, "important_var", important_var_table),
		_export_generic_macros_from_dict(lib, dir, "game_mod_var", game_mod_var_table),
		_export_generic_macros_from_dict(lib, dir, "story_var", story_var_table),
		_export_generic_macros_from_dict(lib, dir, "npc1", npc_sprite_table1),
		_export_generic_macros_from_dict(lib, dir, "npc2", npc_sprite_table2),
		_export_generic_macros_from_dict(lib, dir, "npc3", npc_sprite_table3),
		_export_generic_macros_from_dict(lib, dir, "npc4", npc_sprite_table4),
		_export_generic_macros_from_dict(lib, dir, "bank_table", bank_list_table),
		_export_generic_macros_from_dict(lib, dir, "bank1", map_outdoor),
		_export_generic_macros_from_dict(lib, dir, "bank2", map_route),
		_export_generic_macros_from_dict(lib, dir, "bank3", map_wald_suempfe),
		_export_generic_macros_from_dict(lib, dir, "bank4", map_hoehle_gebirge),
		_export_generic_macros_from_dict(lib, dir, "bank6", map_heilige_orte),
		_export_generic_macros_from_dict(lib, dir, "bank8", map_hesperia_maps),
		_export_generic_macros_from_dict(lib, dir, "bank9", map_carun_city_maps),
		_export_generic_macros_from_dict(lib, dir, "bank10", map_urbania_city_maps),
		_export_generic_macros_from_dict(lib, dir, "bank120", map_debug_test_startmap),
		_export_generic_macros_from_dict(lib, dir, "ebene_type", ebene_type_table),
		_export_generic_macros_from_dict(lib, dir, "signpost_type", signpost_type_table),
		_export_generic_macros(lib, dir, "map_connections", map_connections),
		_export_generic_macros_from_dict(lib, dir, "music", music),
		_export_generic_macros(lib, dir, "behaviours", behaviours),
		_export_generic_macros_from_dict(lib, dir, "map_namespaces", map_namespaces),
		_export_generic_macros_from_dict(lib, dir, "map_showname", map_show_name),
		_export_generic_macros(lib, dir, "flash_types", flash_types),
		_export_generic_macros(lib, dir, "map_weather", map_weather),
		_export_generic_macros(lib, dir, "map_type", map_types),
		_export_generic_macros(lib, dir, "battle_types", battle_types)
	]
	fd = open(dir + STDPREAMBLE, "w+")
	fd.write("\n\n\n".join(macros))
	fd.close()

def _export_generic_macros(lib, dir, _generic_name, _generic_table):
	""" Export generic macros """
	_mkdirs(dir)
	macro = "@ARM Assembly macro definitions for " + _generic_name + "\n\n\n"
	macro += "\n".join([(".equ " + _generic_table[i] + ", " + hex(i)) for i in range(len(_generic_table))]) + "\n"
	path = dir + _generic_name +".s"
	return macro
	"""fd = open(path, "w+")
	fd.write(macro)
	fd.close()
	lib_update(lib, _generic_name, path)"""

def _export_generic_macros_from_dict(lib, dir, _generic_name, _generic_dict):
	""" Export generic macros """
	_mkdirs(dir)
	macro = "@ARM Assembly macro definitions for " + _generic_name + "\n\n\n"
	macro += "\n".join([(".equ " + _generic_dict[k] + ", " + hex(k)) for k in _generic_dict]) + "\n"
	path = dir + _generic_name +".s"
	return macro
	"""fd = open(path, "w+")
	fd.write(macro)
	fd.close()
	lib_update(lib, _generic_name, path)"""

def lib_update(libf, type, file):
	""" Updates a macro link in the lib for a certain type """
	fd = open(libf, "r+")
	lib = eval(fd.read())
	fd.close()
	lib[type] = os.path.relpath(file, INCLUDE)
	fd = open(libf, "w+")
	fd.write(str(lib))
	fd.close()

def get_macro_header():
	""" Returns a macro header """
	"""fd = open(rpath.path(STDLIB, from_root=from_root), "r+")
	lib = eval(fd.read())
	fd.close()"""
	#return "\n".join(('.include "' + lib[k].replace("\\", "/") + '"') for k in lib) + "\n"
	return "#include <" + STDPREAMBLE + ">"

if __name__ == "__main__":
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hl:", ["help"])
	except getopt.GetoptError:
		sys.exit(2)
	lib = STDLIB
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			print("Usage: constants.py outdir (e.g.'foo/bar/')")
			sys.exit(0)
		elif opt in ("-l"): lib = arg
	dir = args[0]
	export_macros(lib, dir)
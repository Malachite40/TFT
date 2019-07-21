from enum import Enum
from itertools import combinations

class Origin(Enum):
    DEMON = 1
    DRAGON = 2
    EXILE = 3
    GLACIAL = 4
    ROBOT = 5
    IMPERIAL = 6
    NOBLE = 7
    NINJA = 8
    PIRATE = 9
    PHANTOM = 10
    WILD = 11
    VOID = 12
    YORDLE = 13
    ASSASSIN = 14
    BLADEMASTER = 15
    BRAWLER = 16
    ELEMENTALIST = 17
    GAURDIAN = 18
    GUNSLINGER = 19
    KNIGHT = 20
    RANGER = 21
    SHAPESHIFTER = 22
    SORCERER = 23

class tf:
    def __init__(self, pawns=None):
        self._pawns = pawns

    def print_all_pawns(self, tier=None, origins=None):

        if origins is not None:
            for x in range(0, len(pawns)):
                pawn = pawns[x]
                if all(elem in pawn._origins for elem in origins):
                    print(pawn._name)

            return

        if tier is not None:
            for x in range(0,len(pawns)):
                pawn = pawns[x]
                if pawn._tier == tier:
                    print(pawn._name)
            return


        for x in range(0,len(pawns)):
            print(pawns[x]._name)

    def get_all_pawns(self, tier=None, origins=None):
        plist = []

        if origins is not None:
            for x in range(0, len(pawns)):
                pawn = pawns[x]
                if all(elem in pawn._origins for elem in origins):
                    plist.append(pawn)

            return plist

        if tier is not None:
            for x in range(0,len(pawns)):
                pawn = pawns[x]
                if pawn._tier == tier:
                    plist.append(pawn)

            return plist

        return None

    def find_origins(self, pawns):

        buffs = []

        if self.has_assassin_6(pawns) or self.has_assassins_3(pawns):
            buffs.append(Origin.ASSASSIN)

        if self.has_blademaster_3(pawns) or self.has_blademaster_6(pawns):
            buffs.append(Origin.BLADEMASTER)

        if self.has_brawler_2(pawns) or self.has_brawler_4(pawns):
            buffs.append(Origin.BRAWLER)

        if self.has_elementalist(pawns):
            buffs.append(Origin.ELEMENTALIST)

        if self.has_gardian(pawns):
            buffs.append(Origin.GAURDIAN)

        if self.has_gunslinger_2(pawns) or self.has_gunslinger_4(pawns):
            buffs.append(Origin.GUNSLINGER)

        if self.has_knight_2(pawns) or self.has_knight_4(pawns) or self.has_knight_6(pawns):
            buffs.append(Origin.KNIGHT)

        if self.has_ranger_2(pawns) or self.has_ranger_4(pawns):
            buffs.append(Origin.RANGER)
        
        if self.has_shapeshifter(pawns):
            buffs.append(Origin.SHAPESHIFTER)
        
        if self.has_sorcerer_3(pawns) or self.has_sorcerer_6(pawns):
            buffs.append(Origin.SORCERER)

        if self.has_demonds_2(pawns) or self.has_demonds_4(pawns) or self.has_demonds_6(pawns):
            buffs.append(Origin.DEMON)

        if self.has_dragons(pawns):
            buffs.append(Origin.DRAGON)

        if self.has_exile(pawns):
            buffs.append(Origin.EXILE)

        if self.has_glacial_2(pawns) or self.has_glacial_4(pawns) or self.has_glacial_6(pawns):
            buffs.append(Origin.GLACIAL)

        if self.has_imperials_2(pawns) or self.has_imperials_4(pawns):
            buffs.append(Origin.IMPERIAL)
            
        if self.has_nobles_3(pawns) or self.has_nobles_6(pawns):
            buffs.append(Origin.NOBLE)

        if self.has_ninja_1(pawns) or self.has_ninja_4(pawns):
            buffs.append(Origin.NINJA)

        if self.has_phantom(pawns):
            buffs.append(Origin.PHANTOM)

        if self.has_pirates(pawns):
            buffs.append(Origin.PIRATE)

        if self.has_robot(pawns):
            buffs.append(Origin.ROBOT)

        if self.has_voids(pawns):
            buffs.append(Origin.VOID)

        if self.has_wild_2(pawns) or self.has_wild_4(pawns):
            buffs.append(Origin.WILD)

        if self.has_yordles_3(pawns) or self.has_yordles_6(pawns):
            buffs.append(Origin.YORDLE)

        return buffs 

    # Has buff functions

    def has_assassins_3(self, pawns):
        count = 0
        used_pawns =[]
        for x in range(0, len(pawns)):
            pawn = pawns[x]
            if Origin.ASSASSIN in pawn._origins and pawn not in used_pawns:
                count += 1
                used_pawns.append(pawn)
                if count >= 3:
                    return True
        return False

    def has_assassin_6(self, pawns):
        count = 0
        used_pawns =[]
        for x in range(0, len(pawns)):
            pawn = pawns[x]
            if Origin.ASSASSIN in pawn._origins and pawn not in used_pawns:
                count += 1
                used_pawns.append(pawn)
                if count >= 6:
                    return True
        return False

    def has_blademaster_3(self, pawns):
        count = 0
        used_pawns =[]
        for x in range(0, len(pawns)):
            pawn = pawns[x]
            if Origin.BLADEMASTER in pawn._origins and pawn not in used_pawns:
                count += 1
                used_pawns.append(pawn)
                if count >= 3:
                    return True
        return False

    def has_blademaster_6(self, pawns):
        count = 0
        used_pawns =[]
        for x in range(0, len(pawns)):
            pawn = pawns[x]
            if Origin.BLADEMASTER in pawn._origins and pawn not in used_pawns:
                count += 1
                used_pawns.append(pawn)
                if count >= 6:
                    return True
        return False

    def has_brawler_2(self, pawns):
        count = 0
        used_pawns =[]
        for x in range(0, len(pawns)):
            pawn = pawns[x]
            if Origin.BRAWLER in pawn._origins and pawn not in used_pawns:
                count += 1
                used_pawns.append(pawn)
                if count >= 2:
                    return True
        return False

    def has_brawler_4(self, pawns):
        count = 0
        used_pawns =[]
        for x in range(0, len(pawns)):
            pawn = pawns[x]
            if Origin.BRAWLER in pawn._origins and pawn not in used_pawns:
                count += 1
                if count >= 4:
                    used_pawns.append(pawn)
                    return True
        return False

    def has_elementalist(self, pawns):
        count = 0
        used_pawns =[]
        for x in range(0, len(pawns)):
            pawn = pawns[x]
            if Origin.ELEMENTALIST in pawn._origins and pawn not in used_pawns:
                count += 1
                used_pawns.append(pawn)
                if count >= 3:
                    return True
        return False

    def has_gardian(self, pawns):
        count = 0
        used_pawns =[]
        for x in range(0, len(pawns)):
            pawn = pawns[x]
            if Origin.GAURDIAN in pawn._origins and pawn not in used_pawns:
                count += 1
                used_pawns.append(pawn)
                if count >= 2:
                    return True
        return False

    def has_gunslinger_2(self, pawns):
        count = 0
        used_pawns =[]
        for x in range(0, len(pawns)):
            pawn = pawns[x]
            if Origin.GUNSLINGER in pawn._origins and pawn not in used_pawns:
                count += 1
                used_pawns.append(pawn)
                if count >= 2:
                    return True
        return False

    def has_gunslinger_4(self, pawns):
        count = 0
        used_pawns =[]
        for x in range(0, len(pawns)):
            pawn = pawns[x]
            if Origin.GUNSLINGER in pawn._origins and pawn not in used_pawns:
                count += 1
                used_pawns.append(pawn)
                if count >= 4:
                    return True
        return False

    def has_knight_2(self, pawns):
        count = 0
        used_pawns =[]
        for x in range(0, len(pawns)):
            pawn = pawns[x]
            if Origin.KNIGHT in pawn._origins and pawn not in used_pawns:
                count += 1
                used_pawns.append(pawn)
                if count >= 2:
                    return True
        return False

    def has_knight_4(self, pawns):
        count = 0
        used_pawns =[]
        for x in range(0, len(pawns)):
            pawn = pawns[x]
            if Origin.KNIGHT in pawn._origins and pawn not in used_pawns:
                count += 1
                used_pawns.append(pawn)
                if count >= 4:
                    return True
        return False

    def has_knight_6(self, pawns):
        count = 0
        used_pawns =[]
        for x in range(0, len(pawns)):
            pawn = pawns[x]
            if Origin.KNIGHT in pawn._origins and pawn not in used_pawns:
                count += 1
                used_pawns.append(pawn)
                if count >= 6:
                    return True
        return False

    def has_ranger_2(self, pawns):
        count = 0
        used_pawns =[]
        for x in range(0, len(pawns)):
            pawn = pawns[x]
            if Origin.RANGER in pawn._origins and pawn not in used_pawns:
                count += 1
                used_pawns.append(pawn)
                if count >= 2:
                    return True
        return False

    def has_ranger_4(self, pawns):
        count = 0
        used_pawns =[]
        for x in range(0, len(pawns)):
            pawn = pawns[x]
            if Origin.RANGER in pawn._origins and pawn not in used_pawns:
                count += 1
                used_pawns.append(pawn)
                if count >= 4:
                    return True
        return False

    def has_shapeshifter(self, pawns):
        count = 0
        used_pawns =[]
        for x in range(0, len(pawns)):
            pawn = pawns[x]
            if Origin.SHAPESHIFTER in pawn._origins and pawn not in used_pawns:
                count += 1
                used_pawns.append(pawn)
                if count >= 3:
                    return True
        return False

    def has_sorcerer_3(self, pawns):
        count = 0
        used_pawns =[]
        for x in range(0, len(pawns)):
            pawn = pawns[x]
            if Origin.SORCERER in pawn._origins and pawn not in used_pawns:
                count += 1
                used_pawns.append(pawn)
                if count >= 3:
                    return True
        return False

    def has_sorcerer_6(self, pawns):
        count = 0
        used_pawns =[]
        for x in range(0, len(pawns)):
            pawn = pawns[x]
            if Origin.SORCERER in pawn._origins and pawn not in used_pawns:
                count += 1
                used_pawns.append(pawn)
                if count >= 6:
                    return True
        return False

    def has_demonds_2(self, pawns):
        count = 0
        used_pawns =[]
        for x in range(0, len(pawns)):
            pawn = pawns[x]
            if Origin.DEMON in pawn._origins and pawn not in used_pawns:
                count += 1
                used_pawns.append(pawn)
                if count >= 2:
                    return True
        return False

    def has_demonds_4(self, pawns):
        count = 0
        used_pawns =[]
        for x in range(0, len(pawns)):
            pawn = pawns[x]
            if Origin.DEMON in pawn._origins and pawn not in used_pawns:
                count += 1
                used_pawns.append(pawn)
                if count >= 4:
                    return True
        return False

    def has_demonds_6(self, pawns):
        count = 0
        used_pawns =[]
        for x in range(0, len(pawns)):
            pawn = pawns[x]
            if Origin.DEMON in pawn._origins and pawn not in used_pawns:
                count += 1
                used_pawns.append(pawn)
                if count >= 6:
                    return True
        return False

    def has_dragons(self, pawns):
        count = 0
        used_pawns =[]
        for x in range(0, len(pawns)):
            pawn = pawns[x]
            if Origin.DRAGON in pawn._origins and pawn not in used_pawns:
                count += 1
                used_pawns.append(pawn)
                if count >= 2:
                    return True
        return False

    def has_exile(self, pawns):
        count = 0
        used_pawns =[]
        for x in range(0, len(pawns)):
            pawn = pawns[x]
            if Origin.EXILE in pawn._origins and pawn not in used_pawns:
                count += 1
                used_pawns.append(pawn)
                if count >= 1:
                    return True
        return False

    def has_glacial_2(self, pawns):
        count = 0
        used_pawns =[]
        for x in range(0, len(pawns)):
            pawn = pawns[x]
            if Origin.GLACIAL in pawn._origins and pawn not in used_pawns:
                count += 1
                used_pawns.append(pawn)
                if count >= 2:
                    return True
        return False

    def has_glacial_4(self, pawns):
        count = 0
        used_pawns =[]
        for x in range(0, len(pawns)):
            pawn = pawns[x]
            if Origin.GLACIAL in pawn._origins and pawn not in used_pawns:
                count += 1
                used_pawns.append(pawn)
                if count >= 4:
                    return True
        return False

    def has_glacial_6(self, pawns):
        count = 0
        used_pawns =[]
        for x in range(0, len(pawns)):
            pawn = pawns[x]
            if Origin.GLACIAL in pawn._origins and pawn not in used_pawns:
                count += 1
                used_pawns.append(pawn)
                if count >= 6:
                    return True
        return False

    def has_imperials_2(self, pawns):
        count = 0
        used_pawns =[]
        for x in range(0, len(pawns)):
            pawn = pawns[x]
            if Origin.IMPERIAL in pawn._origins and pawn not in used_pawns:
                count += 1
                used_pawns.append(pawn)
                if count >= 2:
                    return True
        return False

    def has_imperials_4(self, pawns):
        count = 0
        used_pawns =[]
        for x in range(0, len(pawns)):
            pawn = pawns[x]
            if Origin.IMPERIAL in pawn._origins and pawn not in used_pawns:
                count += 1
                used_pawns.append(pawn)
                if count >= 4:
                    return True
        return False

    def has_nobles_3(self, pawns):
        count = 0
        used_pawns =[]
        for x in range(0, len(pawns)):
            pawn = pawns[x]
            if Origin.NOBLE in pawn._origins and pawn not in used_pawns:
                count += 1
                used_pawns.append(pawn)
                if count >= 3:
                    return True
        return False

    def has_nobles_6(self, pawns):
        count = 0
        used_pawns =[]
        for x in range(0, len(pawns)):
            pawn = pawns[x]
            if Origin.NOBLE in pawn._origins and pawn not in used_pawns:
                count += 1
                used_pawns.append(pawn)
                if count >= 6:
                    return True
        return False

    def has_ninja_1(self, pawns):
        count = 0
        for x in range(0, len(pawns)):
            pawn = pawns[x]
            if Origin.NINJA in pawn._origins:
                count += 1
        
        if count == 1:
            return True
        return False

    def has_ninja_4(self, pawns):
        count = 0
        used_pawns =[]
        for x in range(0, len(pawns)):
            pawn = pawns[x]
            if Origin.NINJA in pawn._origins and pawn not in used_pawns:
                count += 1
                used_pawns.append(pawn)
                if count >= 4:
                    return True
        return False

    def has_phantom(self, pawns):
        count = 0
        used_pawns =[]
        for x in range(0, len(pawns)):
            pawn = pawns[x]
            if Origin.PHANTOM in pawn._origins and pawn not in used_pawns:
                count += 1
                used_pawns.append(pawn)
                if count >= 2:
                    return True
        return False

    def has_pirates(self, pawns):
        count = 0
        used_pawns =[]
        for x in range(0, len(pawns)):
            pawn = pawns[x]
            if Origin.PIRATE in pawn._origins and pawn not in used_pawns:
                count += 1
                used_pawns.append(pawn)
                if count >= 3:
                    return True
        return False

    def has_robot(self, pawns):
        count = 0
        used_pawns =[]
        for x in range(0, len(pawns)):
            pawn = pawns[x]
            if Origin.ROBOT in pawn._origins and pawn not in used_pawns:
                count += 1
                used_pawns.append(pawn)
                if count >= 1:
                    return True
        return False

    def has_voids(self, pawns):
        count = 0
        used_pawns =[]
        for x in range(0, len(pawns)):
            pawn = pawns[x]
            if Origin.VOID in pawn._origins and pawn not in used_pawns:
                count += 1
                used_pawns.append(pawn)
                if count >= 3:
                    return True
        return False

    def has_wild_2(self, pawns):
        count = 0
        used_pawns =[]
        for x in range(0, len(pawns)):
            pawn = pawns[x]
            if Origin.WILD in pawn._origins and pawn not in used_pawns:
                count += 1
                used_pawns.append(pawn)
                if count >= 2:
                    return True
        return False

    def has_wild_4(self, pawns):
        count = 0
        used_pawns =[]
        for x in range(0, len(pawns)):
            pawn = pawns[x]
            if Origin.WILD in pawn._origins and pawn not in used_pawns:
                count += 1
                used_pawns.append(pawn)
                if count >= 4:
                    return True
        return False

    def has_yordles_3(self, pawns):
        count = 0
        used_pawns =[]
        for x in range(0, len(pawns)):
            pawn = pawns[x]
            if Origin.YORDLE in pawn._origins and pawn not in used_pawns:
                count += 1
                used_pawns.append(pawn)
                if count >= 3:
                    return True
        return False

    def has_yordles_6(self, pawns):
        count = 0
        used_pawns =[]
        for x in range(0, len(pawns)):
            pawn = pawns[x]
            if Origin.YORDLE in pawn._origins and pawn not in used_pawns:
                count += 1
                used_pawns.append(pawn)
                if count >= 6:
                    return True
        return False


    # asdf

    def find_combos(self, pawns=None, combos=3, team_size=7):
        combos = []

        pawns = self._pawns.copy()

        unique_combos = list(combinations(pawns, team_size))

        for x in range(0, len(unique_combos)):
            print(unique_combos[x][1]._name)

        return combos

class Pawn:
    def __init__(
        self,
        name=None,
        origins=None,
        tier=None,
        ):
        self._name = name
        self._origins = origins
        self._tier = tier

ashe = Pawn(name="ashe", origins=[Origin.RANGER, Origin.GLACIAL], tier=3)
sejuani = Pawn(name="sejuani", origins=[Origin.KNIGHT, Origin.GLACIAL], tier=4)
gnar = Pawn(name="gnar", origins=[Origin.WILD, Origin.SHAPESHIFTER, Origin.YORDLE], tier=4)
chogath = Pawn(name="chogath", origins=[Origin.BRAWLER, Origin.VOID], tier=4)
garen = Pawn(name="garen", origins=[Origin.KNIGHT, Origin.NOBLE], tier=1)
aurelion_sol = Pawn(name="aurelion_sol", origins=[Origin.SORCERER, Origin.DRAGON], tier=4)
kayle = Pawn(name="kayle", origins=[Origin.KNIGHT, Origin.NOBLE], tier=5)
draven = Pawn(name="draven", origins=[Origin.BLADEMASTER, Origin.IMPERIAL], tier=4)
kassadin = Pawn(name="kassadin", origins=[Origin.VOID, Origin.SORCERER], tier=1)
brand = Pawn(name="brand", origins=[Origin.DEMON, Origin.ELEMENTALIST], tier=4)
vayne = Pawn(name="vayne", origins=[Origin.NOBLE, Origin.RANGER], tier=1)
anivia = Pawn(name="anivia", origins=[Origin.GLACIAL, Origin.ELEMENTALIST], tier=5)
kindred = Pawn(name="kindred", origins=[Origin.PHANTOM, Origin.RANGER], tier=4)
nidalee = Pawn(name="nidalee", origins=[Origin.SHAPESHIFTER, Origin.WILD], tier=1)
darius = Pawn(name="darius", origins=[Origin.IMPERIAL, Origin.KNIGHT], tier=1)
pyke = Pawn(name="pyke", origins=[Origin.ASSASSIN, Origin.PIRATE], tier=2)
veigar = Pawn(name="veigar", origins=[Origin.SORCERER, Origin.YORDLE], tier=3)
kha_zix = Pawn(name="kha_zix", origins=[Origin.VOID, Origin.ASSASSIN], tier=1)
morgana = Pawn(name="morgana", origins=[Origin.DEMON, Origin.SORCERER], tier=3)
yasuo = Pawn(name="yasuo", origins=[Origin.EXILE, Origin.BLADEMASTER], tier=5)
karthus = Pawn(name="karthus", origins=[Origin.SORCERER, Origin.PHANTOM], tier=5)
lulu = Pawn(name="lulu", origins=[Origin.SORCERER, Origin.YORDLE], tier=2)
elise = Pawn(name="elise", origins=[Origin.DEMON, Origin.SHAPESHIFTER], tier=1)
lissandra = Pawn(name="lissandra", origins=[Origin.ELEMENTALIST, Origin.GLACIAL], tier=2)
swain = Pawn(name="swain", origins=[Origin.DEMON, Origin.IMPERIAL, Origin.SHAPESHIFTER], tier=5)
zed = Pawn(name="zed", origins=[Origin.ASSASSIN, Origin.NINJA], tier=2)
miss_fortune = Pawn(name="miss_fortune", origins=[Origin.PIRATE, Origin.GUNSLINGER], tier=5)
kennen = Pawn(name="kennen", origins=[Origin.ELEMENTALIST, Origin.YORDLE, Origin.NINJA], tier=3)
lucian = Pawn(name="lucian", origins=[Origin.NOBLE, Origin.GUNSLINGER], tier=2)
shyvana = Pawn(name="shyvana", origins=[Origin.SHAPESHIFTER, Origin.DRAGON], tier=3)
leona = Pawn(name="leona", origins=[Origin.NOBLE, Origin.GAURDIAN], tier=4)
volibear = Pawn(name="volibear", origins=[Origin.BRAWLER, Origin.GLACIAL], tier=3)
graves = Pawn(name="graves", origins=[Origin.PIRATE, Origin.GUNSLINGER], tier=1)
blitzcrank = Pawn(name="blitzcrank", origins=[Origin.ROBOT, Origin.BRAWLER], tier=2)
shen = Pawn(name="shen", origins=[Origin.NINJA, Origin.BLADEMASTER], tier=2)
ahri = Pawn(name="ahri", origins=[Origin.SORCERER, Origin.WILD], tier=2)
akali = Pawn(name="akali", origins=[Origin.NINJA, Origin.ASSASSIN], tier=4)
varus = Pawn(name="varus", origins=[Origin.DEMON, Origin.RANGER], tier=2)
aatrox = Pawn(name="aatrox", origins=[Origin.DEMON, Origin.BLADEMASTER], tier=3)
warwick = Pawn(name="warwick", origins=[Origin.WILD, Origin.BRAWLER], tier=1)
braum = Pawn(name="braum", origins=[Origin.GAURDIAN, Origin.GLACIAL], tier=2)
rengar = Pawn(name="rengar", origins=[Origin.WILD, Origin.ASSASSIN], tier=3)
poppy = Pawn(name="poppy", origins=[Origin.KNIGHT, Origin.YORDLE], tier=3)
mordekaiser = Pawn(name="mordekaiser", origins=[Origin.PHANTOM, Origin.IMPERIAL], tier=1)
evelynn = Pawn(name="evelynn", origins=[Origin.ASSASSIN, Origin.DEMON], tier=3)
rek_sai = Pawn(name="rek_sai", origins=[Origin.VOID, Origin.BRAWLER], tier=2)
katarina = Pawn(name="katarina", origins=[Origin.IMPERIAL, Origin.ASSASSIN], tier=3)
fiora = Pawn(name="fiora", origins=[Origin.NOBLE, Origin.BLADEMASTER], tier=1)
gangplank = Pawn(name="gangplank", origins=[Origin.BLADEMASTER, Origin.GUNSLINGER, Origin.PIRATE], tier=3)
tristrana = Pawn(name="tristrana", origins=[Origin.GUNSLINGER, Origin.YORDLE], tier=1)

pawns = [ashe,sejuani,gnar,chogath,garen,aurelion_sol,kayle,draven,kassadin,brand,vayne,anivia,kindred,nidalee,darius,pyke,veigar,kha_zix,morgana,yasuo,karthus,lulu,elise,lissandra,swain,zed,miss_fortune,kennen,lucian,shyvana,leona,volibear,graves,blitzcrank,shen,ahri,akali,varus,aatrox,warwick,braum,rengar,poppy,mordekaiser,evelynn,rek_sai,katarina,fiora,gangplank,tristrana]

tfm = tf(pawns=pawns)

# `temp_pawn = [sejuani, ashe, kassadin, rek_sai, warwick, chogath, shen, zed, kennen, akali]

# buffs = tfm.find_origins(temp_pawn)
# for x in range(0, len(buffs)):
#     print(buffs[x].name)

tfm.find_combos(pawns=tfm._pawns, combos=4, team_size=4)

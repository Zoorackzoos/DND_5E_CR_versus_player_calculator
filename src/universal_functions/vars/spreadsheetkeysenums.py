from enum import Enum, auto

class SpreadsheetKeysEnums(Enum):
    """
    These are if you want to call a dictionary's key.
    they're here in order to make sure you don't get a type error because you put
    "size" instead of "Size" or something.
    this makes more sense in a java context but having to go to the spreadsheet to confirm
    the right spelling is dumb asf.
    """
    NAME = "Name"
    SIZE = "Size"
    TYPE = "Type"
    CR = "CR"
    URL = "URL"
    FONT = "Font"
    AUTHOR = "Author"
    AC = "AC"
    HP = "HP"
    SPEEDS = "Speeds"
    ALIGN = "Align."
    STR = "STR"
    DEX = "DEX"
    CON = "CON"
    INT = "INT"
    WIS = "WIS"
    CHA = "CHA"
    SAVING_THROWS = "Sav. Throws"
    SKILLS = "Skills"
    WEAKNESSES_RESISTANCES_AND_IMMUNITIES = "WRI"
    SENSES = "Senses"
    LANGUAGES = "Languages"
    ADDITIONAL = "Additional"

class SizeEnums(Enum):
    TINY = "Tiny"
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"
    HUGE = "Huge"
    GARGANTUAN = "Gargantuan"

class CreatureTypesEnums(Enum):
    """
    Enums which you can call on to get the DND 5e types.  \n

    this comes from the spreadsheet of course. \n

    if for some reason you wanted to add a type you would have to add it to the ENUM list.
    """
    ABERRATION = "Aberration"
    BEAST = "Beast"
    CELESTIAL = "Celestial"
    CONSTRUCT = "Construct"
    DRAGON = "Dragon"
    ELEMENTAL = "Elemental"
    FEY = "Fey"
    FIEND = "Fiend"
    FIEND_DEMON = "Fiend (Demon)"
    FIEND_DEVIL = "Fiend (Devil)"
    FIEND_DEMON_ORC = "Fiend (Demon,Orc)"
    FIEND_SHAPECHANGER = "Fiend (Shapechanger)"
    FIEND_YUGOLOTH = "Fiend (Yugoloth)"
    GIANT = "Giant"
    GIANT_GIANT_CLOUD = "Giant (Giant, Cloud)"
    GIANT_GIANT_FIRE = "Giant (Giant, Fire)"
    GIANT_GIANT_FROST = "Giant (Giant, Frost)"
    GIANT_GIANT_HILL = "Giant (Giant, Hill)"
    GIANT_GIANT_STONE = "Giant (Giant, Stone)"
    GIANT_GIANT_STORM = "Giant (Giant, Storm)"
    HUMANOID = "Humanoid"
    HUMANOID_ANY_RACE = "Humanoid (Any Race)"
    HUMANOID_DERO = "Humanoid (Derro)"
    HUMANOID_DWARF = "Humanoid (Dwarf)"
    HUMANOID_ELF = "Humanoid (Elf)"
    HUMANOID_FIRENEWT = "Humanoid (Firenewt)"
    HUMANOID_GIF = "Humanoid (Gith)"
    HUMANOID_GNOLL = "Humanoid (Gnoll)"
    HUMANOID_GOBLINOID = "Humanoid (Goblinoid)"
    HUMANOID_GRUNG = "Humanoid (Grung)"
    HUMANOID_HUMAN = "Humanoid (Human)"
    HUMANOID_KOBALD = "Humanoid (Kobold)"
    HUMANOID_MONGRELFOLK = "Humanoid (Mongrelfolk)"
    HUMANOID_NAGGA = "Humanoid (Nagpa)"
    HUMANOID_ORC = "Humanoid (Orc)"
    HUMANOID_TABAXI = "Humanoid (Tabaxi)"
    HUMANOID_TORTLE = "Humanoid (Tortle)"
    HUMANOID_TROGLODYTE = "Humanoid (Troglodyte)"
    HUMANOID_XVART = "Humanoid (Xvart)"
    HUMANOID_YUAN_TI = "Humanoid (Yuan-Ti)"
    MONSTROSITY = "Monstrosity"
    MONSTROSITY_YUAN_TI = "Monstrosity (Yuan-Ti)"
    OOZE = "Ooze"
    PLANT = "Plant"
    UNDEAD = "Undead"
    UNDEAD_TITAN = "Undead (Titan)"

class CRTypeEnums(Enum):
    """
    i've added verbal words to these. \n
    if you find these annoying you can delete them
    """
    CR_zero_no_challenge = 0
    CR_one_eight_very_weak = 1/8
    CR_one_forth_weak = 1/4
    CR_one_half_minor = 1/2
    CR_one = 1
    CR_two = 2
    CR_three = 3
    CR_four = 4
    CR_five = 5
    CR_six = 6
    CR_seven = 7
    CR_ten = 10
    CR_twenty = 20

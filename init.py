#import pickle as serial #serialization library
import pathlib
import random as rand

mods = [] #list of 3rd party mods; datatype file object

settings = {
"shipNames" : eval(open("settings/shipNames.cfg", "r")),
"nations" : eval(open("settings/nations.cfg", "r"))
}

def selNation(): #let user select a nation; overwrites local settings["nations"] to selected - thus, it may only run once
    global settings
    if not settings["nations"] == eval(open("settings/nations.cfg", "r")):
        raise Exception("NATION already set; immutable.\nDid you try to run selNation more than once?")
    print("AVAILABLE NATIONS\n")
    for val in settings["nations"]:
        print("\t" + val)
    print("\nSELECT A NATION")
    natSEL = input(" > ")
    if not settings["nations"][natSEL]:
        print("INVALID NATION")
        selNation()
    else:
        settings["nations"] = settings["nations"][natSEL]
def selShipName(): #randomly select a ship name
    global settings
    if not settings["shipNames"] == eval(open("settings/shipNames.cfg", "r")):
        raise Exception("SHIPNAME already set; immutable.\nDid you try to run selShipName more than once?")
    settings["shipNames"] = settings["shipNames"][rand.randint(0, len(settings["shipNames"]) - 1)]

for module in pathlib.Path("mods"):
    mods.append(module) #temp kludge, breakpoint
    eval(module) #run mod
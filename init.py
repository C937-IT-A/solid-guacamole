#import pickle as serial #serialization library
import pathlib

mods = [] #3rd party mods

for module in pathlib.Path("mods"):
    mods.append(module) #temp kludge, breakpoint

settingsFiles = {eval(open("settings/shipNames.cfg", "r"))}
import pathlib

i = 0

for module in pathlib.Path("../"):
    if module.is_file() and not module == __file__:
        print("LOADED 3PM " + str(module))
        i = i + 1

print("STOCK CONFIG LOADED")
print("LOADED " + str(i) + "3PMs")
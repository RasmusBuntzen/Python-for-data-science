dict = {"store":[("a","b","c")]}
try:
    dict["små"].append(("d","e"))
except:
    dict["små"] = ("d","e")
print(dict)
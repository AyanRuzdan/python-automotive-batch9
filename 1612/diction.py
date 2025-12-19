# sample dictionary
tracks = {
    "Italy": "Autodromo Monza",
    "United Kingdom": "Silverstone Circuit",
    "Monaco": "Circuit Monaco",
    "Japan": "Suzuka International",
}

# accessing full dict
print(tracks, "\n")

# access using square brackets
print(tracks['Italy'], "\n")

# access using get function
print(tracks.get("Japan"), "\n")

# getting all keys
print(tracks.keys(), "\n")

# getting all values
print(tracks.values(), "\n")

# getting all items i.e. both keys and values
print(tracks.items(), "\n")

# updating an existing item
tracks.update({"Japan": "Suzuka International Circuit"})
print("After update: \n", tracks, "\n")

# popping key:value using key
tracks.pop("United Kingdom")
print("After popping UK: \n", tracks, "\n")

# using items to unpack tuples for loop access
for k, v in tracks.items():
    print("%s:%s" % (k, v))

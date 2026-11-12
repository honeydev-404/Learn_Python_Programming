#Dictionary -> it is a used to store data in key-value pair separated with comma (,) and are enclosed with curly braces {}. Suppose key is like a variable that tells what is the value about (like "name":"Honey").
dict1 = {
    "name": "Honey",
    "server": "Asia_East",
    "level": 18
}
print(f"Dictionary 1: {dict1}")

#Rules -> There are certain rules that you must not create duplicate keys, if you do that the second key will overwrite the value of first key.
dict2 = {
    "port":80,
    "port":443 #This overwrites the value 80 completely.
}
print(f"Dictionary 2: {dict2}")

#Accessing Values -> You can access the value from the dictionaries through there keys, with syntax dict["name"].
player_name = dict1["name"]
print(f"Active Player: {player_name}")
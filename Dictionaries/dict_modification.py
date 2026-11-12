#Dictionaries are mutable, means you can add a new key or overwrite it using assignment operator (=).
system_user = {
    "admin":"Bobby",
    "active":False
}

#overwriting the existing value of the key.
system_user["active"] = True

#Adding new key-value pair.
system_user["role"] = "Backend Engineer"
print(f"Modified Dictionary {system_user}")

#Deleting something via del keyword, it removes a key from a dictionary remember removing key from the dictionary also removes the value from the memory.
#Critical: Attempting to delete a key that doesn't exist with throw a KeyError crash. 
security_log = {
    "ip": "192.168.1.1",
    "temp_session_token": "XYZ987",
    "port": 22
}

del security_log["temp_session_token"]
print(f"With temp_session_token removed: {security_log}")

#You can find the total length of the dict with key-value combined with the len() method.
total_length = len(security_log)
print(f"Total Length of dictionary: {total_length}")

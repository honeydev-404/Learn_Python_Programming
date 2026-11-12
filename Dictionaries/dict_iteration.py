#The use of "in" keyword -> You can check if something exist in the dictionary by using the in keyword on the key in the dictionary.
user_profile = {
    "username": "Honey",
    "role": "Backend Engineer",
    "level": 18
}

has_email = "email" in user_profile
print(f"Does email key exist in dictionary: {has_email}")

#We can add using email field using "if-else" statement. (This is extra for my practise can be yours too...)
if has_email == False:
    user_profile["email"] = "bobthebuilder@gmail.com"

print(f"Added email key: {user_profile}")

#Looping directly over a dictionary gives you the key of the dictionary in sequence.
for key in user_profile:
    value = user_profile[key]
    print(f"{key} -> {value}")

#Merging Dictionaries -> You can merge the dictionaries with the pipe (|) symbol. Remember duplicate keys get overwritten.
default_settings = {"theme": "light", "notifications": True}
custom_settings = {"theme": "dark", "ssh_timeout": 30}

final_settings = default_settings | custom_settings
print(final_settings)

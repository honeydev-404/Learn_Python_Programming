# Sometime checking one condition is not enough, we can glue them together with logical operator.

#and -> Returns True if both the conditions are True, otherwise False.
#or -> Return True if one of the conditons are True, otherwise False.
#not -> Returns the opposite of the expected result, can be recognized as (!).

has_key = False
door_locked = True

if has_key and door_locked:
    print("Admin...")
elif has_key or door_locked:
    print("Thief...")

print(not has_key)
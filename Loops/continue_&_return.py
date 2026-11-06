#The Continue Statement -> It helps in skipping some part of the code by writing the continue statement with the condition from where it should skip. Whatever sits underneath it also gets skipped.

print("--- For Continue Statement ---")
for num in range(0,6):
    if num == 3: #This condition will skip the 3 iteration.
        continue 
    
    print(f"Active Numbers are {num}") 

#The Break Statement -> Think of it like a kill-switch if continue statement skips something. By adding this statement you can terminate the full loop.

print("\n--- For Break Statement ---")
for number in range(0,6):
    if number == 4:
        break
    print(f"Active Numbers are {number}")



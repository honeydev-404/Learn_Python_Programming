#The For Loop -> It is loop that is used when you know the exact number or sequences to iterate over the values. It automatically steps through each item from starting to finish.

print("--- The For Loop Understanding ---")
for animal_name in ["Horse"]:
    print(f"The Animal's name is {animal_name}")

#The Range Engine -> The range() is used to generate a sequence of numbers for us. Like we can use it to print numbers and it has various use cases.
#How to use it -> Define the range() func and then it take three inputs (start, end, step).
    #Start -> It tells where to start.
    #Stop -> It tells where to stop.
    #Step -> It tells at which exactly step to skip, think of it for writing the tables.

print("--- The Range Engine Understanding ---")
for num in range(0, 6):
    print(f"The Number is : {num}")
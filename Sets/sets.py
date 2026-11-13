#Sets -> It is a data-type that is just like list and it is created using curly braces ({}), but it is unordered and prefers unique items (like if you convert list to sets then the duplicate values will be striped out).
empty_set = set() #You can create an empty set using set(), remember we are using parenthesis here not curly braces (that will create a dictionary).
my_set = {"nmap", "ssh", "git", "ssh"}
print(f"Unique items: {my_set}")

my_set.add("python") #You can add something in the set using .add method.
print(f"Added 'python': {my_set}")

my_set.remove("git") #You can remove something using .remove method.
print(f"Removed 'git': {my_set}")

#You can also subtract some sets
set1 = {"apple", "banana", "grape"}
set2 = {"apple", "banana"}
total = set1 - set2
print(f"With Subtraction: {total}")
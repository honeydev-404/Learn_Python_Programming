#Suppose you want to access some part of the list so you can do that by list slicing concept.
#The syntax goes like (list_name[start:stop:step]), if you will keep the parameter nothing in start and stop then it will assume it as 0.
system_ports = [21, 22, 80, 443, 8080]

part1 = system_ports[0:2] #This will print items from index 0 to 2.
print(f"From 0 to 2: {part1}")

part2 = system_ports[::] #It will set it to from start to end.
print(f"From starting to last: {part2}")

part3 = system_ports[::-1] #It will print it from last to first (reverse order).
print(f"In reverse order: {part3}")

part4 = system_ports[::2] #It will start from the 0 to last and it will skip the 2 index of each iteration.
print(f"This will print whole list with each 2 iteration skipped: {part4}")

#List Concatenation -> You can join two or more list also.
frontend = ["HTML", "CSS"]
backend = ["Python", "Go"]
total = frontend + backend
print(f"Two List joined Togther: {total}")

#The 'IN' Keyword: It have different use cases but here it tells if something is inside the list or not in True/False.
has_port = 22 in system_ports
print(f"Do system ports have 22nd port available?: {has_port}")

#Delete -> You can delete something from the list with del() keyword.
hardware = ["CPU", "GPU", "Broken_Fan", "Broken_RAM"]
del hardware[2]
print(f"Remove the broken fan: {hardware}")

#Remove -> You can remove something inside the list with its actual value also not by its index number.
hardware.remove("Broken_RAM")
print(f"This will remove the Broken RAM by its name: {hardware}")

#Split -> You can split the items if they are seperated by comma in the list.
message = "hello there sam"
words = message.split()
print(f"The message splited into the list: {words}")

#Join -> it is used to join some splited words like a list of words 
" ".join(words)
print(f"The words joined again with the use of join keyword: {words}")
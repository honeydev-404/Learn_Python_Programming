# Now we will study about one more overhead reducer that is f-string(formatted string), which helps us solve the problem of printing various variables. Again and Again we cannot add + or , to parse the result with the string. Here comes f-string it lets us add things in the string itself by adding the f mark in the starting of the string and {} enclosing the variables in the curly brackets.

name = "Honey"
age = 16

print("My Name is", name, "and My Age is", age) #The traditional and hardworker's way.
print(f"My name is {name} and My Age is {age}") #In the starting of the string I added (f) and now was able to concatenate the string and integers inside the string only.
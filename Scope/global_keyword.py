#Ques -> What is scope?
#Ans -> It refers to where the variable or function name is available to be used.

#So you must be thinking that you can access anything from anywhere, let me prove you wrong.
name1 = "Aman"

def my_name_with_local():
    name2 = "Honey"
    

print(f"With Local Scope: {name1}, -")
#print(name2) #Now you notice an NameError that will tell us that the thing you are trying to access is not defined but it is defined not as a global keyword as it is inside the function.

#Solution -> If you want to push something to the global scope doesn't matter how much nested it is, you can put a "global" keyword behind the variable and then you will be able to access it from anywhere.
 
name1 = "Aman"

def my_name_with_global():
    global name2
    name2 = "Honey"

my_name_with_global()

print(f"With Global Scope: {name1}, {name2}") 


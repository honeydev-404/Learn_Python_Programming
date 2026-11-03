#Parameter -> These are the temprory placeholder variable, created inside [my_function(name, age)]. These are important as if we pass some values inside the parenthesis when we are calling it then we can enter somevalues and they will get alligned in the function.
#In the above the name and age are parameters.

def my_function(name, age):
    print(f"My name is {name} and I am {age} yrs old")

#Arguments -> These are the values or string that are passed while calling the function, like [my_function("Honey", 16)].

my_function("Honey", 16) #Calling the function with the arguements.
# Now we will study about the functions.
# Ques- what are functions and what are the used for and what major problem do they solve?
# Ans- So functions are the mechanism that also reduces overhead of repeatedly writing some lines of code again-and-again for the single logic.
# So once you write a function for some functionalities you can call it from anywhere and get you code executed rather than writing same code for multiple places.


# Defining a function -> The "def" keyword is used to define a function, it tells python that we are making a reusable command block.
msg = "hello world!!!"
def my_function(): # here if there will be inside the parenthesis then it will be considered as parameter. if you keep it empty it can take the global scope variable.
    print(msg)

# Note -> Defining a function doesn't means it will be called automatically, it just saves it in memory.

# Calling a function -> It is called by writing the name of the function (in our case it is 'my_function') and then if arguements remember arguements not parameters will be inside the parenthesis().
my_function() # Arguements can be empty if no parameter is defined in the function.


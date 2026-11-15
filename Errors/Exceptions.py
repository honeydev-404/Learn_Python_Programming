#SyntaxError vs. Exceptions -> Syntax error are typos caught by python before the code even runs, exceptions are the error that occurs in the runtime (like ZeroDivisionError). One crashes when the code runs and crashes in between on crashes when the code didn't start to be executed.

#What are try/except :-
    #Try -> In this we pass the risky code like dividing 0 with 10.
    #Except -> In this we pass the solution for what to do when the try fails and the code crashes.

#Specific Exception First -> You can catch the specific error first before the exception as e because there can be more than 1 error so you can make the solution for them separately.
try:
    num = int("abc")
except ValueError:
    print("Invalid user input...")
except Exception as e:
    print(f"General Fallback: {e}")

#All possible errors -> We use it so we can get all possible errors but it comes with a drawback that we can't give the separate solution for the errors.
try:
    10 / 0
except Exception as e: #We use [except Exception as e:] so, that we can get all the errors that will occur if the try conditions fails.
    print(f"Error Occured: {e}")


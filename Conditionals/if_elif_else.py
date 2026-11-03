#Now we have to get some work done with some conditions, like checking the marks of the student with grading method. We will use if, elif or else statement for that.

marks = 50
if marks >= 90: #If marks are greater than 90.
    print("Grade A")
elif marks >= 70: #If marks are greater than 70. Runs if first condition is not met.
    print("Grade B")
else: # Last condition if all starting conditions are not met.
    print("Fail ;)")

#if -> There can be various if statement (nested) and it is the starting most conditional statement, elif and else cannot start it.
#elif -> There can be numerous elif statement and have no limit (not nested also), it also requires if statement to start.
#else -> It is the last condition if none of the above conditions are met, and it is important to include else in the last.
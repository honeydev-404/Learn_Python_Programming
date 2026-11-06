#The While Loop acts as a repeating "if" statement. It keeps repeating the code block until it evalutes True and if it doesn't there might be some chances that it is a infinite loop.
#It is used when you don't know how many times a condition will run.

num = 0
while num < 100:
    num += 1
    print(num) 

#State mutation is mandatory because it directly alter the variable to be False, smashing the infinite loop. That will tell that it is a infinite loop and that will also evalute the condition to be False.
#The infinite loops are very dangerous, they are the programmes that doesn't stop until we want to.

#Return -> It returns the output and exits the function, and also stored the data in the variable that can be reused later. 
def with_print_sum(num1, num2):
    total = num1 + num2
    print(total)

#Print -> It is used to pass the data to the console and no other logics can be implemented on it, and its value doesn't get stored for future needs.
def with_return_sum(num1, num2):
    total = num1 + num2
    return total

with_print_sum(5,5)
saved_total = with_return_sum(6,6)
print(saved_total)
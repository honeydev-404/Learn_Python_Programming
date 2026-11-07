#What is List -> List is one of the most widely used data storage mechanism because of its data integrity.
#List Syntax and Creation -> The list are created using square brackets [], it is used most of the time because of its features and capabilities.

laptop_names = ["Thinkpad", "xps", "Macbook"] #The data is stored as a string and separated with comma (,).
print(f"The List of Laptop contains:- {laptop_names}")

#Indexing and Accessing Elements -> Computer uses Zero-Indexed Counting means the counting will start from 0, and then second item will be the first one according to the rule. You can access the elements from there name or index.

first_index = laptop_names[0] #Note -> Here I have named the variable as first_index according to us (human understanding) but it is written zero because it starts from there as I have told you about that in the above line.
print(f"The First Index of the list have:- {first_index}")

#Now, If you want to find the length of the list (items inside it) then there is a Built-in len() function that we can use to find the length of the list.

total_length = len(laptop_names)
print(f"The total_length fo list:- {total_length}")


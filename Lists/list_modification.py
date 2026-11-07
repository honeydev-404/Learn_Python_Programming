#Updating An Element-In place -> You can overwrite something on a specific slot. Like you want to add different animal name on index[1] then the previous one will be overwritten.
print("--- For Updation An Element-In place ---")
total_names = ["Aman", "Honey"] 
total_names[1] = "Amit" #Remember it is working on the second one according to us but it is working in 1st one.
print(f"Final Output with Amit added:- {total_names}")

#Appending items -> The .append() method dynamically attaches the new item to the very end of the list.
print("\n--- For Appending the Items ---")
total_names.append("Babu")
print(total_names)

#Popping Element -> This helps us remove a specific item from the list. If you keep the parenthesis empty then it will remove the very last item of the list and if you give a index number it will remove according to it.
print("\n--- For Popping Element ---")
removed_names = total_names.pop(1) #Here I have defined the index if you want to remove the very last item of the list then you can keep it empty.
print(f" Removed Name:- {removed_names}")
print(f"Total Names Left:- {total_names}")
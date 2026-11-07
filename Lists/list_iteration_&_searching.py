#No-Index for Loop Iteration -> The easiest way to show up all the items of the list is to use for loop so that it will show the data sequentially.
laptop_inventory = ["Thinkpad", "XPS", "Macbook"]
for lap in laptop_inventory:
    print(f"The Names of the Laptop are {lap}")

#Accumulator Finding or Searching -> It is used when we want to find some exact metric from the large dataset.
#For this we can use some sort of methods like min() or max().
player_scores = [45, 82, 94, 67, 12]
max_score = max(player_scores)
print(max_score)

#And if you want it to be sorted in ascending order then :-
player_scores.sort()
print(player_scores) 
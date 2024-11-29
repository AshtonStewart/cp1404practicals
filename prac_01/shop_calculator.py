#Gets the total number of items the person is buying.
items = int(input("How many items are you purchasing?"))
totalcost = 0
#sets up a loop based on the previous input that occurs (input) times, collecting costs each time
for i in range(0,items, 1):
    #Gets the new items cost and adds it to the total before displaying said total
    itemcost = int(input("How much does the item cost?"))
    totalcost = totalcost + itemcost
    print(f"the new total is {totalcost}$")
#checks if the final total cost is above 100 and if so, applies a 10% discount.
if totalcost >= 100:
    totalcost = totalcost * 0.9
    print("Your total is over 100$ so you get a 10% discount!")
#says the final cost
print(f"The cost of all your items is {totalcost}$")
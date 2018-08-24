equipmentCheckout = [["Megaphone", 6, 3, 3],
["SM generator", 4, 6, 2],
["LG generator", 2, 0, 0],
["Gas mask - SM", 4, 2, 1],
["Tent - 2 person", 6, 4, 4],
["Gas mask - MD", 4, 0, 0],
["Blankets", 30, 12, 12],
["Gas mask - LG", 4, 3, 3],
["Gas mask - XL", 4, 6, 4]]

# Count # of items you still need
totalNeeded = 0
surplusAvailable = 0
notCheckedOut = 0
for record in equipmentCheckout:
    item = record[0]
    numNeeded = record[1]
    numOwned = record[2]
    numCheckedOut = record[3]

    if numNeeded > numOwned:
        itemsNeeded = numNeeded - numOwned
        totalNeeded = totalNeeded + itemsNeeded
# Count # of surplus items we have that are not checked out
    else:
        surplus = (numOwned - numNeeded) - numCheckedOut
        surplusAvailable = surplusAvailable + surplus

# Count # of gas masks you own that are not checked out
    if item[:3] == "Gas" and item[4:8] == "mask":
        notCheckedOut = notCheckedOut + (numOwned - numCheckedOut)

# Print the results of the three counts
print(str(totalNeeded) + " total items needed.")
if surplusAvailable > 0:
    print(str(surplusAvailable) + " total items available to give to activists.")
else:
    print("No surplus items available to give to activists.")
print(str(notCheckedOut) + " gas masks owned and not checked out.")
import pyinputplus as pyip

ingrediants = {
    "bread" : ["Wheat", "White", "Sourdough"],
    "protein" : ["Chicken", "Turkey", "Ham", "Tofu"],
    "cheese" : ["Chedder", "Swiss", "Mozzarella"],
    "other" : ["Mayo", "Mustard", "Lettuce", "Tomato"]}

cost = {
    "bread" : {"Wheat" : 1, "White" : 2, "Sourdough" : 3},
    "protein" : {"Chicken" : 1, "Turkey" : 2, "Ham" : 3, "Tofu" : 4},
    "cheese" : {"Chedder" : 1, "Swiss" : 2, "Mozzarella" : 3},
    "other" : {"Mayo" : 1, "Mustard" : 2, "Lettuce" : 3, "Tomato" : 4}
    }

order = {"bread" : None,
         "protein" : None,
         "cheese" : None,
         "other" : None}
total = 0

for i in order:
    print(i)
    # print(pyip.inputYesNo("test"))
    if pyip.inputYesNo(f"Do you want {i}?").lower() in ["yes", "y"]:
        order[i] = pyip.inputMenu(ingrediants[i])
    order[i]

for i in order:
    if order[i] == None:
        print("No order")
        continue
    print(i)
    print(cost[i][order[i]])
    print(f"{total} + {cost[i][order[i]]}")
    total += cost[i][order[i]]
print(total)

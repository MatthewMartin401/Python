
#order.append(input("Your Order: "))
order = "Cheese, Burger"
for i in [","]:
    order = order.replace(i, " ")

order = order.split(" ")
print(order)

menu = {
    "Cheese" : 3,
    "Burger" : 5,
    "Cola" : 7
    }

cost = 0
for i in menu:
    print(i)
    if i in order:
        cost += menu[i]
cost += cost / 100 * 7

print(cost)

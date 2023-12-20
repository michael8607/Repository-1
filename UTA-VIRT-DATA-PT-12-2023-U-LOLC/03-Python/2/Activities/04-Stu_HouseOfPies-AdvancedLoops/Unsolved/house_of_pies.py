pies = {"(1)" : "Pecan",
        "(2)" : "Apple Crisp",
        "(3)" : "Bean",
        "(4)" : "Banoffee",
        "(5)" : "Black Bun",
        "(6)" : "BLueberry",
        "(7)" : "Buko",
        "(8)" : "Burek",
        "(9)" : "Tamale",
        "(10)" : "Steak"}

purchase_list = []
repeat = "y"




purchase_list = purchase_list.append(order)


while repeat == "y":
    order = int(input("please input you pie #")) + 1
    print("Great! We'll have that {pie_name} right out for you!")
    purchase_list = purchase_list.append(pies[order + 1])
    repeat = input("would you like to order another pie? (y/n)")


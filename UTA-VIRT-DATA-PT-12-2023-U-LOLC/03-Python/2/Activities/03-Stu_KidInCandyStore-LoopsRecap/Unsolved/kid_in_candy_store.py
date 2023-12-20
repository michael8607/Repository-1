# The list of candies to print to the screen
candy_list = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish", "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]

for index, value in enumerate(candy_list):
    print(f"{index}, {value}")
# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of
candy_cart = []

# Print out options
for candy in candy_list:
    index = candy_list.index(candy)
    print("[" + str(index) + "]" + candy)


while len(candy_cart) <= allowance:
    userInput = input("Enter an Integer from 0-8:")
    userInput = int(userInput)
    if (0 <= userInput <= len(candy_list)):
        candy_cart.append(candy_list[userInput])
    else:
        print("inelligible input")

print(candy_cart)


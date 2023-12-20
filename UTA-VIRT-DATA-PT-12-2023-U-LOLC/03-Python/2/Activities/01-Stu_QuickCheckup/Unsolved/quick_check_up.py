# Prin't Hello User!
print("Hello User!")

# Take in User Input
user_name = input("what is your name?")

# Respond Back with User Input
print(f"Hello {user_name}")


# Take in the User Favorite Number
favorite_number = input("what is your favorite number?")
favorite_number = int(favorite_number)

# Respond Back with a statement based on your favorite number
if favorite_number < 10:
    print("your faborite number is less than mine")
elif favorite_number > 10:
    print("your favorite number is bigger than mine")
elif favorite_number == 10:
    print("your favorite number is the same as mine!")

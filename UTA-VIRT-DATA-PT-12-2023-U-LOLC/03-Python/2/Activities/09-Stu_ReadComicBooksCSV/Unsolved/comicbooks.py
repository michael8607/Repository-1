# Modules
import os
import csv
# Prompt user for title lookup
title = str(input("What is the title of the book you are looking for?"))
# Set path for file
csvpath = os.path.join("..", "Resources", "comic_books.csv")
# Set variable to check if we found the comic book
found_title = False
# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Loop through looking for the comic book
    for row in csvreader:
        # Check if the current row's title matches the user's input
        if row[0] == title:
            publisher = row[8]
            DOP = row[9]
            # Set variable to confirm we have found the comic book
            found_title = True
            # Print out the details of the comic book
            print(f"{title} was published by {publisher} in {DOP}")
# If the comic book is never found, alert the user
if not found_title:
    print(f"Sorry, the book '{title}' could not be found.")
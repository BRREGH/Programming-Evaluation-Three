-
import random

#Generates Random Number
randomNumber = random.uniform(1, 100)

#Asks user how many decimal places they want the number rounded to
decimalPlaces = int(input("Enter the number of decimal places to round to: "))

#Rounds the Random Number
roundedNumber = round(randomNumber, decimalPlaces)
#Prints the number
print(roundedNumber)



#--------------------------------------Question # 2 -----------------------------------------
print("--------------------------------QUESTION # 2--------------------------------------------")
#Asks user for first and last name
fName = input("What is your first name?")
fNameCount = 0
for letter in fName:
  fNameCount += 1
lName = input("What is your last name?")
lNameCount = 0
for letter in lName:
  lNameCount += 1
#Counting letters in user's first and last name and making a special ID

specialID = str(fNameCount) + str(lNameCount)

#Displaying the user's names, letter counts, and special ID
print("First Name:", fName)
print("Number of letters in First Name:", fNameCount)
print("Last Name:", lNameCount)
print("Number of letters in Last Name:", lNameCount)
print("SpecialID:", specialID)

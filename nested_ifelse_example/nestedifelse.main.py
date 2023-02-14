#
#           Question : Get the user's gender and age,
#           Women aged 60 and over, men aged 65 and over can retire.
#           “You can retire” taking into account gender and age
#           or print “You have to work .. more years to retire”.
#

# this for taking input about what users gender is
gend = input("Please enter your gender with M/W : ")
# this for taking input about what users age is
age = input("Please enter your age : ")
age = int(age) #this will be convert str to int

# nested if else
if gend == "M" or gend == "m":
    if age < 0 or age > 90:
        print("Invalid value for age. Please try again.")
    elif age < 65:
        print("You have to work ", (65 - age), " years more.")
    else:
        print("You can be retired.")
elif gend == "W" or gend == "w":
    if age < 0 or age > 90:
        print("Invalid value for age. Please try again.")
    elif age < 60:
        print("You have to work ", (60 - age), " years more.")
    else:
        print("You can be retired.")
else:
    print("You've entered invalid gender value, please try again.")


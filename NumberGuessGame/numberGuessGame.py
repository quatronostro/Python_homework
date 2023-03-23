import random

rNum = random.randint(0, 100)

print("WELCOME TO NUMBER GUESSING GAME!!!"
      "\nYou have 5 guesses for to find correct number and it must be between 0 and 100, so lets try."
      "\n\nEnter your number : ")

enteredNum = int(input())
flag = 4

while True:
    differance = rNum - enteredNum

    if enteredNum < rNum:

        if differance < 10:
            print("The number you entered is less than the correct number. You're so close. Your remaining trial : ",
                  flag,
                  "\nPlease try again : ")
            enteredNum = int(input())
        elif differance < 20:
            print("The number you entered is less than the correct number. Try some more. Your remaining trial : ",
                  flag,
                  "\nPlease try again : ")
            enteredNum = int(input())
        else:
            print(
                "The number you entered is less than the correct number. You made a long guess. Your remaining trial : ",
                flag,
                "\nPlease try again : ")
            enteredNum = int(input())

    if enteredNum > rNum:

        if differance < 10:
            print("The number you entered is greater than the correct number. You're so close. Your remaining trial : ",
                  flag,
                  "\nPlease try again : ")
            enteredNum = int(input())
        elif differance < 20:
            print("The number you entered is greater than the correct number. Try some more. Your remaining trial : ",
                  flag,
                  "\nPlease try again : ")
            enteredNum = int(input())
        else:
            print(
                "The number you entered is less greater the correct number. You made a long guess. Your remaining trial : ",
                flag,
                "\nPlease try again : ")
            enteredNum = int(input())

    flag -= 1
    if flag == 0:
        print("You have filled your right to guess.")
        break

if enteredNum == rNum:
    print("\nYou got the correct number, Congratulations!!!"
          "\n Correct Num : ", rNum)

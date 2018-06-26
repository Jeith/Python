print("--------------------------")
print("-------CHALLENGE 1--------")
print("--------------------------")
print("")
name = input("What is your name? ")
greeting = "Hello " + name + ", how are you?"
print(greeting)

print("")
print("--------------------------")
print("-------CHALLENGE 2--------")
print("--------------------------")
print("")
name2 = (input("WHAT IS YOUR NAME? ").upper())
name2length = str(len(name2))
greeting2 = "HELLO " + name2 + ", YOUR NAME HAS " + name2length + " LETTERS IN IT"
print(greeting2)

print("")
print("--------------------------")
print("-------CHALLENGE 3--------")
print("--------------------------")
print("")
print("Please fill in the blanks below: ")
madlib = "___(name)___'s favorite food is ___(color)___ ___(food)___."
print(madlib)
name3 = input("Enter name: ")
color3 = input("Enter color: ")
food3 = input("Enter food: ")
print(name3 + "'s favorite food is " + color3 + " " + food3 + ".")

print("")
print("--------------------------")
print("-------CHALLENGE 4--------")
print("--------------------------")
print("")
day = int(input('Day (0-6)? '))
dayOfWeek = ""
if day == 0:
    dayOfWeek = "Sunday"
elif day == 1:
    dayOfWeek = "Monday"
elif day == 2:
    dayOfWeek = "Tuesday"
elif day == 3:
    dayOfWeek = "Wednesday"
elif day == 4:
    dayOfWeek = "Thursday"
elif day == 5:
    dayOfWeek = "Friday"
elif day == 6:
    dayOfWeek = "Saturday"
else:
    dayOfWeek = "Invalid input"
print(dayOfWeek)

print("")
print("--------------------------")
print("-------CHALLENGE 5--------")
print("--------------------------")
print("")
day2 = int(input('Day (0-6)? '))
dayOfWeek2 = ""
if day2 >=1 and day2 <=5:
    dayOfWeek2 = "Go to work!"
elif day2 == 0 or day2 == 6:
    dayOfWeek2 = "Sleep in."
else:
    dayOfWeek2 = "Invalid input"
print(dayOfWeek2)

print("")
print("--------------------------")
print("-------CHALLENGE 6--------")
print("--------------------------")
print("")
cel = int(input("Temperature in C? "))
fahr = (cel * 1.8) + 32
print("It is " + str(fahr) + " F")

print("")
print("--------------------------")
print("-------CHALLENGE 7--------")
print("--------------------------")
print("")
bill = float(input("Enter Total Bill Amount: "))
service = input("Enter level of service(good, fair, bad): ")
tip = ""
if service == "good":
    tip = (bill * .20)
elif service == "fair":
    tip = (bill * .15)
elif service == "bad":
    tip = (bill * .10)
else:
    tip = "invalid"
goodtip = "{:.2f}".format(tip)
full = tip + bill
goodfull = "{:.2f}".format(full)
print("You should tip " + str(goodtip) + ", making your total amount " + str(goodfull) + ".")

print("")
print("--------------------------")
print("-------CHALLENGE 8--------")
print("--------------------------")
print("")
bill = float(input("Enter Total Bill Amount: "))
service = input("Enter level of service(good, fair, bad): ")
split = int(input("Split how many ways? "))
tip = ""
if service == "good":
    tip = (bill * .20)
elif service == "fair":
    tip = (bill * .15)
elif service == "bad":
    tip = (bill * .10)
else:
    tip = "invalid"
goodtip = "{:.2f}".format(tip)
full = tip + bill
goodfull = "{:.2f}".format(full)
amtperperson = (full / split)
goodsplit = "{:.2f}".format(amtperperson)
print("Your tip: " + str(goodtip) + " Your total amount: " + str(goodfull) + " Amount per person: " + str(goodsplit))

print("")
print("--------------------------")
print("-------CHALLENGE 9--------")
print("--------------------------")
print("")
num = 0
while num < 10:
    num += 1
    print(num)


print("")
print("--------------------------")
print("-------CHALLENGE 10-------")
print("--------------------------")
print("")
coins = 0
answer = input("You have " + str(coins) + ", would you like another[yes/no]? ")
while answer == "yes":
    coins += 1
    answer = input("You have " + str(coins) + ", would you like another[yes/no]? ")
    if answer == "no":
        print("Bye!")
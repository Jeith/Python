print("----------------------")
print("-----Challenge 1------")
print("----------------------")
print("")
for x in range(1,11):
    print(x)

print("")
print("----------------------")
print("-----Challenge 2------")
print("----------------------")
print("")
n = input("Start from: ")
m = int(input("End on: "))
m += 1
for x in range(int(n),m):
    print(x)

print("")
print("----------------------")
print("-----Challenge 3------")
print("----------------------")
print("")   
numbers = range(1, 11)
i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
        i += 1
    else:
        print(numbers[i])
        i += 1

print("")
print("----------------------")
print("-----Challenge 4------")
print("----------------------")
print("")
stars = "*****"
i = 0
while i < 5:
    print(stars)
    i += 1
    if i == 5:
        break

print("")
print("----------------------")
print("-----Challenge 5------")
print("----------------------")
print("")
howBig = int(input("How big is the square? "))
i = 0
while i < howBig:
    print("*" * howBig)
    i += 1
    if i == howBig:
        break

print("")
print("----------------------")
print("-----Challenge 6------")
print("----------------------")
print("")
width = int(input("Enter Width: "))
height = int(input("Enter Height: "))
i = 0
while i < height:
    print("*" * width)
    i += 1
    if i == height:
        break

print("")
print("----------------------")
print("-----Challenge 7------")
print("----------------------")
print("")
i = 0
star = "*"
while i < 4:
    print(star)
    star = star + "**"
    i += 1
    if i == 4:
        break

print("")
print("----------------------")
print("-----Challenge 8------")
print("----------------------")
print("")
height = int(input("Enter Height: "))
i = 0
star = "*"
while i < height:
    print(star)
    star = star + "**"
    i += 1
    if i == height:
        break

print("")
print("----------------------")
print("-----Challenge 9------")
print("----------------------")
print("")
i = 1
j = 1
while i < 12 and j < 11:
    if i < 11:
        z = i * j
        print(str(i) + " * " + str(j) + " = " + str(z))
        i += 1
    elif i == 11:
        i = 1
        j += 1

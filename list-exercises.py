
print("----------------------")
print("-----Challenge 1------")
print("----------------------")
print("")
myList = [3, 2, 1]
print(sum(myList))

print("")
print("----------------------")
print("-----Challenge 2------")
print("----------------------")
print("")
myList = [3, 2, 1]
print(max(myList))

print("")
print("----------------------")
print("-----Challenge 3------")
print("----------------------")
print("")
myList = [3, 2, 1]
print(min(myList))

print("")
print("----------------------")
print("-----Challenge 4------")
print("----------------------")
print("")
myList = [5, 2, 6, 1, 3, 8]
i = 0
while i < len(myList):
    if myList[i] % 2 == 0:
        print(myList[i])
        i += 1
    else:
        i += 1

print("")
print("----------------------")
print("-----Challenge 5------")
print("----------------------")
print("")
i = 0
numList = [1, 2, 3, 4, 0, 7, 5, 8, 10, -8, -5, -2]
while i < len(numList):
    if numList[i] > 0:
        print(numList[i])
        i += 1
    else:
        i += 1

print("")
print("----------------------")
print("-----Challenge 6------")
print("----------------------")
print("")
i = 0
numList = [1, 2, 3, 4, 0, 7, 5, 8, 10, -8, -5, -2]
positiveList = []
while i < len(numList):
    if numList[i] > 0:
        positiveList.append(numList[i])
        i += 1
    else:
        i += 1
print(positiveList)

print("")
print("----------------------")
print("-----Challenge 7------")
print("----------------------")
print("")
i = 0
numList = [1, 2, 3, 4, 0, 7, 5, 8, 10, -8, -5, -2]
multList = []
while i < len(numList):
    multNum = numList[i] * 2
    multList.append(multNum)
    i += 1
print(multList)

print("")
print("----------------------")
print("-----Challenge 8------")
print("----------------------")
print("")
i = 0
j = 0
vect1 = [3, 6, 9]
vect2 = [2, 4, 6]
result = []
while i < len(vect1) and j < len(vect2):
    numToAdd = vect1[i] * vect2[j]
    result.append(numToAdd)
    i += 1
    j += 1
print(result)

print("")
print("----------------------")
print("-----Challenge 9------")
print("----------------------")
print("")

print("")
print("----------------------")
print("-----Challenge 10-----")
print("----------------------")
print("")

print("")
print("----------------------")
print("-----Challenge 11-----")
print("----------------------")
print("")
deDup = [1, 2, 5, 2, 3, 1, 6, 6]
i = len(deDup)
j = 0
noDup = []
while j < len(deDup):
    if deDup[i] == deDup[j]:
        deDup.pop()
        j += 1
    elif deDup[i] != deDup[j]:
        j += 1
    elif j == len(deDup):
        j = len(deDup)
        i -= 1
print(deDup)
    
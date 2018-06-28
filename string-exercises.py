print("----------------------")
print("-----Challenge 1------")
print("----------------------")
print("")
answer1 = input("Enter full name: ")
print(answer1.upper())

print("")
print("----------------------")
print("-----Challenge 2------")
print("----------------------")
print("")
answer2 = "keith"
print(answer2.capitalize())

print("")
print("----------------------")
print("-----Challenge 3------")
print("----------------------")
print("") 
myString = "Australopithicus" 
newString = ""
i = len(myString)
i -= 1
while i != 1:
    print(myString[i])
    i -= 1

print("")
print("----------------------")
print("-----Challenge 4------")
print("----------------------")
print("")
myString = "Given a paragraph of text as a string, print the paragraph in leetspeak. To translate a string to leetspeak, you need to replace make the following character replacements"
for char in myString:
	if char == 'a':
		myString = myString.replace('a','4')
	elif char == 'i':
		myString = myString.replace('i','1')
	elif char == 'e':
		myString = myString.replace('e','3')
	elif char == 'g':
		myString = myString.replace('g','9')
	elif char == 'o':
		myString = myString.replace('o','0')
	elif char == 's': 
		myString = myString.replace('s','5')
	elif char == 't':
		myString = myString.replace('t','7')
print(myString)

print("")
print("----------------------")
print("-----Challenge 5------")
print("----------------------")
print("")
myString = "Man Spoon"
myString = myString.replace('ee', 'eeeee')
myString = myString.replace('oo', 'ooooo')
myString = myString.replace("aa", "aaaaa")
print(word)
        

print("")
print("----------------------")
print("-----Challenge 6------")
print("----------------------")
print("")
cipher = "lbh zhfg hayrnea jung lbh unir yrnearq"
alphabet = ["a", "b", "c", "d", "e", "f","g", "h","i","j","k", "l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
position = 0
newPosition = 0
decodedPosition = 0
for cipherLetter in cipher:
    if cipherLetter.isspace() == False :
        position = alphabet.index(cipherLetter)
        newPosition = position - 13
        if newPosition < 0:
            newPosition = 26 + newPosition
        print(alphabet[newPosition])

print("----------------------")
print("-----Challenge 1------")
print("----------------------")
print("")
phonebook_dict = { 'Alice': '703-493-1834', 'Bob': '857-384-1234', 'Elizabeth': '484-584-2923' }
print(phonebook_dict["Elizabeth"])
phonebook_dict["Kareem"] = "938-489-1234"
del phonebook_dict["Alice"]
phonebook_dict["Bob"] = "968-345-2345"
print(phonebook_dict)

print("")
print("----------------------")
print("-----Challenge 2------")
print("----------------------")
print("")
ramit = { 'name': 'Ramit', 'email': 'ramit@gmail.com', 'interests': ['movies', 'tennis'], 'friends': [ { 'name': 'Jasmine', 'email': 'jasmine@yahoo.com', 'interests': ['photography', 'tennis'] }, { 'name': 'Jan', 'email': 'jan@hotmail.com', 'interests': ['movies', 'tv'] } ] }
print(ramit['email'])
print(ramit["interests"][0])
print(ramit['friends'][0]['email'])
print(ramit['friends'][1]['interests'][1])
print("")
print("----------------------")
print("-----Challenge 3------")
print("----------------------")
print("")
myLetters = {}
giveMeWord = input("Enter word: ")
for let in giveMeWord:
    letter = let
    if letter not in myLetters:
        myLetters[letter] = 0
    myLetters[letter] += 1
print(myLetters)

print("")
print("----------------------")
print("-----Challenge 4------")
print("----------------------")
print("")
giveMeSentence = input("Enter Sentence ")
word_dict = {}
word_histogram = giveMeSentence.split()
for word in word_histogram:
    word_dict[word] = giveMeSentence.count(word)
print(word_dict)
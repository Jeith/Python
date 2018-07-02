print("----------------------")
print("-----Challenge 1------")
print("----------------------")
print("")
class Person: 
    def __init__(self, name, email, phone, friends, greeting_count): 
        self.name = name 
        self.email = email 
        self.phone = phone 
        self.friends = []
        self.greeting_count = 0

    def greet(self, other_person): 
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greeting_count += 1

    def print_contact_info(self):
        print(self.name + "'s email: " + self.email + ", " + self.name + "'s phone number: " + self.phone)

    def add_friend(self, other_friend):
        self.friends.append(other_friend)

    def num_friends(self):
        print(len(self.friends))

    def __str__(self): 
        return 'Person: {}, Email: {}, Phone Number: {}'.format(self.name, self.email, self.phone)
    
#1
sonny = Person("Sonny", "sonny@hotmail.com", '483-485-4948', [], 0)
#2
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456", [], 0)
#3
print(sonny.greet(jordan))
#4
print(jordan.greet(sonny))
#5
print(sonny.email, sonny.phone)
#6
print(jordan.email, jordan.phone)

print("")
print("----------------------")
print("-----Challenge 2------")
print("----------------------")
print("")
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def print_info(self):
        print(self.make, self.model, self.year)
car = Vehicle("Jeep", "Wrangler", "2009")
print(car.make, car.model, car.year)
# add a method
car.print_info()
# add a method 2
sonny.print_contact_info()
# add an instance variable
sonny.friends.append(jordan)
print(len(sonny.friends))
# add an add_friend method
jordan.add_friend(sonny)
# add num of friends
jordan.num_friends()
# count num of greetings
jordan.greeting_count
jordan.greet(sonny)
jordan.greeting_count
# __str__
str(jordan)

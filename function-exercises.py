print("----------------------")
print("-----Challenge 1------")
print("----------------------")
print("")
def hello(x):
    print("Hello " + x)
hello("Keith")

print("")
print("----------------------")
print("-----Challenge 2------")
print("----------------------")
print("")
import matplotlib.pyplot as plot
def f(x):
    x += 1
    return x

xs = list(range(-3, 4)) 
ys = [] 

for x in xs: 
     ys.append(f(x)) 

plot.plot(xs, ys) 
plot.show()
pyplot.savefig('myplot2.png')

print("")
print("----------------------")
print("-----Challenge 3------")
print("----------------------")
print("")
import matplotlib.pyplot as plot
def f(x):
    x *= x
    return x
xs = list(range(-100, 100))
ys = []
for x in xs:
    ys.append(f(x))
plot.plot(xs, ys)
plot.show()
pyplot.savefig('myplot3.png')

print("")
print("----------------------")
print("-----Challenge 4------")
print("----------------------")
print("")
import matplotlib.pyplot as plot
def f(x):
    x += 1
    if x % 2 == 0:
        return 1
    else:
        return -1
xs = list(range(-5, 5)) 
ys = []
for x in xs: 
     ys.append(f(x))
plot.bar(xs, ys)
plot.show()
pyplot.savefig('myplot4.png')

print("")
print("----------------------")
print("-----Challenge 5------")
print("----------------------")
print("")
import matplotlib.pyplot as plot
import math
def f(x):
    x = math.sin(x)
    return x
xs = list(range(-5, 5))
ys = []
for x in xs:
    ys.append(f(x))
plot.plot(xs, ys)
plot.show()
pyplot.savefig('myplot5.png')

print("")
print("----------------------")
print("-----Challenge 6------")
print("----------------------")
print("")
from numpy import arange
import matplotlib.pyplot as plot
import math
def f(x):
    x = math.sin(x)
    return x
xs = list(arange(-5, 6, 0.1))
ys = []
for x in xs:
    ys.append(f(x))
plot.plot(xs, ys)
plot.show()
pyplot.savefig('myplot6.png')

print("")
print("----------------------")
print("-----Challenge 7------")
print("----------------------")
print("")
import matplotlib.pyplot as plot
xs = list(range(0, 100))
ys = []
y = 0
def convertcels(cels):
    fahr = (cels * 1.8) + 32
    return fahr
while y != 100:
    y += 1
    ys.append(convertcels(y))
plot.plot(xs, ys)
plot.show()

print("")
print("----------------------")
print("-----Challenge 8------")
print("----------------------")
print("")
def playAgain():
    q = input("Do you want to play again [Y or N]?")
    if q == "Y":
        return True
    if q == "N":
        return False
    else:
        print("Invaild input")
playAgain()

print("")
print("----------------------")
print("-----Challenge 9------")
print("----------------------")
print("")
def playAgain():
    q = ""
    while q != "Y" or q != "N":
        q = input("Do you want to play again [Y or N]?")
        if q == "Y":
            return True
        if q == "N":
            return False
        else:
            print("Invaild input")
playAgain()



import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot
f_output = []
g_output = []
def f(x):
    return x
def g(x):
    return x
x_list = list(range(-3, 5))

for x in x_list:
    f_output.append(f(x))
    g_output.append(g(x))

pyplot.plot(x_list, f_output, x_list, g_output)
pyplot.savefig('myplot.png')
pyplot.close() # start a new plot
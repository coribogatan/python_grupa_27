
# python este un limbaj interpretat.

print ("Hello World!")
print (-7)

# variabile

number1 = 10
number2 = 30

var1 = 'hello'
var2 = 'world'

cat1 = 'Cat'
var3 = 100
print(var3)

var4 = number1 + var3
print(var4)

var4 = 3000
print(var4)

#tipuri de date
# 10, -5, -0 -> int
# 4.5 -> float
# 'hello' -> str
# True sau False -> boolean
var7 = 'hello'

print(var7[2])

var8 = True
print(var8 == True)
# == operator binar de comparare
var9 = True
var10 = 1
print(var9 == var10)

# functii: print, max, min, range, pow
#clase: type - ce tip de date e un obiect

var11 = type(var9)
print(var11)

#liste
print('Liste:')
varlist1 = []
print(varlist1)
varlist2 = [10,30,45,99,-1,0,-99, 46778222,'hello', True,0.7, type(0)]
print(varlist2)

varlist3 = [100, 200, [-1,-3,-10, [-99,-888,0]], [True], var3, var10]
print(varlist3)

varlist4 = [40,50,100,3,-10,0]
#index      0   1  2  3  4  5
#           -6 -5 -4 -3 -2  -1

print(varlist4[-6])

print(varlist4[-2])

list4_length = len(varlist4)
print(list4_length)









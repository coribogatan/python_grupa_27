import random
from functools import reduce
from pprint import pprint

from lib.core import even_numbers, is_even


# print(random.sample(range(0, 1000), 15))

random_numbers = [236, 153, 103, 41, 146, 261, 285, 336, 470, 289, 226, 887, 618, 929, 302, 42, 609, 455]

#lambda functions:

def mult_2(param1):
    return param1 * 2

print(mult_2(10))

square = lambda x: x * 2 # functia e anonima
print(square(10))

#filter(), map(), reduce(), zip()

# filtrati numerele care sunt multiplu de 7

rezultat = list(filter(lambda x: x % 7 == 0, random_numbers ))
print(rezultat)

rezultat2 = list(filter(is_even, random_numbers))
print(rezultat2)

#4 Iunie - map, reduce, zip

print("======= Map function: =======")
random_numbers = [236, 153, 103, 41, 146, 261, 285, 336, 470, 289, 226, 887, 618, 929, 302, 42, 609, 455]

ひらが = list( map(lambda x: x // 2, random_numbers))

print(ひらが)

var2 = list(map(lambda x: x ** 3, random_numbers))
print(var2)


print("======= Reduce =======")
var3 = reduce(lambda a,b: a+b, random_numbers, 10000) # aduna numerele din lista, dc avem val initiala - 10000, incepe adunarea de la 10000
print(var3)

var4 = reduce(lambda a,b: a*b,random_numbers)
print(var4)
print (len(str(var4))) # lungimea sirului de caractere

#random_letters = ['b', 'z', 'f', 'h', 'l', 'u', 'o']
random.letters = []
count = 10

print(chr(64))

min_char = 97
max_char = 122

# for i in range(count):
#     random_letters.append(char(random.randint(min_char, max_char)))
#
# print(random_letters)

step1 = (random.sample(range(min_char, max_char+1), count))
print(step1)
step2 = list(map(lambda x: chr(x), step1))

random_letters = step2
print(random_letters)

### functie
print("===== Functie =====")

def generate_random_chars(count = 10, min_char = 97, max_char= 122):
    step1 = (random.sample(range(min_char, max_char + 1), count))
    step2 = list(map(lambda x: chr(x), step1))
    random_letters = step2
    return random_letters

random_letters = generate_random_chars(count = 10, min_char = 97, max_char= 122)
print(random_letters)

random_japanese_characters = generate_random_chars(count = 29, min_char = 12400, max_char = 12500)
print(random_japanese_characters)

print()

print("======= ZIP function =======") # primesti mai multe liste si le combini in tupluri

names = ['John', 'James', 'Turk', 'Maria', 'Oprah']
ages = [18,20,35,50,10]

combined = list(zip(names, ages)) #primul elem din prima lista cu primul elem din a doua lista si tot asa
print(combined)

combined2 = dict(zip(names, ages)) #creeaza dictionar
print(combined2)

print()

print("======= Key Values =======")

#facem lista de persoane cu nume, varsta, ceva scor si trebuie sa la filtram dupa varsta/ scor

names = ['John', 'James', 'Turk', 'Maria', 'Oprah']
ages = [18,20,35,50,10]
score = [6,8,4,10,9]


# people = [{
#     "name": "John",
#     "age": 18,
#     "score": 6
# },
# ]

zipped_people = list(zip(names, ages, score))
print(zipped_people)

people = []
for elem in zipped_people:
    #('John', 18, 6)
    people.append({
        "name": elem[0],
        "age":elem[1],
        "score":elem[2]
    })

pprint(people, sort_dicts=False)
print()
print("sortare")
sorted_list = sorted(people, key = lambda a: a['name'], reverse = False)
pprint(sorted_list, sort_dicts=False)













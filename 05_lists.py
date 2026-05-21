#variabile de referint
lista1 = [10, 30, 5, 7, 100, -5]
lista2 = lista1

print(lista1)

#modificam lista2 -> se modifica si lista1; valabil la list, set, dict
lista2.append(88)

print(lista1)

#variabile prin valoare
var1 = 100
var2=var1

var2 = 77

print(var1) # variabila nu s-a schimbat

# structuri de date primitive - int, float, bool, string

#structura de date complexa: list, dict, set, tuplu

lista3 = [9,10,100,5,50,4]

#slicing, splicing

#list[start:stop:step] #start, stop is indecsi; stop nu e inclusiv; doar startul e inclusiv; [)

# print(lista3[::-1])
# print(lista3[0:4:3])

lista4 = lista3[:] # slice creeaza o lista noua
lista4.append(88)

print(lista3) # nu se modifica lista3

lista5 = [7,10]
lista5.append(99)
lista5.extend([100,101,102])
lista5 += [103,104,105]
lista5.remove(101) # sterge primul nr 101 din lista, dc sunt 2, il sterge numai pe primul
print(lista5.index(100)) #indexul primul nr 100

lista5.sort()
print(lista5)
lista6 = sorted(lista5)
print(lista6)

# matrici; Matrix

matrice1 = [
    [3,4,10],
    [7,8,11],
    [0,3,99]
]
print(matrice1[2][0])

# list comprehension
lista7 = [3,4,10]
lista8 =[x ** 3 for x in lista7]
print(lista8)

lista9 =[x ** 3 for x in lista7 if x % 2 == 0   ]
print(lista9)

# strings

alfabet='   ABCdefghijklmn' #are indecs, putem face slice, sau -1 (inversam); lista imutabila, nu s epoate schimba
print(alfabet)
print(alfabet[::-1])

print(alfabet.lower()) #nu modifica forma initiala
print(alfabet.upper()) #nu modifica forma initiala

print(alfabet.strip())
print(alfabet.replace("A", "00"))


prop1 = "   Gabi a inceput sa invete python. El, un student, urmeaza acest curs, cursul de python.     "
print(prop1.strip().lower().split(".").remove(''))

rezultat1 = prop1.strip().lower().split(".")
rezultat1.remove('')
print(rezultat1)

# prop2 = '.'
# print(prop2.split('.'))


var3 = ['a' , 'b', 'c', 'detrical d3 10000IU']
rezultat2 = "-".join(var3)

print(rezultat2)

if 'd3' in rezultat2:
    print('avem vit d')

print(99 in lista5)

ex1 = 'AVG-JRD-IOR:RED-GRN-BLU:QWE-RTY-UIO'
#luati acest str si creati o matrice 3x3, in care sa pastrati doar literele

part1 = ex1.split(":")
print(part1)

rezultat3 = []
for elem in part1:
    print(elem)
    rezultat3.append(elem.split("-"))

print(rezultat3[1][0])


#WHILE while conditie > actiune
#folosim cand nu stim nr de pasi sau cand spatiul de explorare este necunoscut, dar avem o conditie clara de sfarsit
# for - cand parcurgem o lista (sau dict), cand stim clar cum arata structura de date, daca lista se modifica intre timp, for-ul nu este potrivit pt a pargurge lista

listaw = [4,10,20,50,100]

while len(listaw)>0:
    print(listaw.pop())

nr_imens = 1000000
while nr_imens>0:
    nr_imens = nr_imens - 10000
    print(nr_imens)


lista13 = [10,20,300,1000]
while True:
    if len(lista13)<=0:
        break
    print(lista13.pop())

#formatare ; f-string

name = 'Alex'
age = 25
profession = 'Carpenter'

print(f"Hello! My name is {name}. I'm {age} years old and I am a {{profession}}")

#concatenare
print("Hello name is " + name + " age is " + str(age) + " profession is " + profession)

#newline special character
msg = 'Line 1 \nLine 2'
print(msg)

#multi-line string
msg2 = '''
        Line 1
        line 2
        etc etc'''
print(msg2)



print("hello world!")

print("this is a change")
print("another change")

var1 = True


# IF statements stau la baza programarii

populatie_bv = 300000
nou_nascuti_curent = 35000
populatie_bv = populatie_bv + nou_nascuti_curent

if populatie_bv > 310000:
    print("populatia BV a crescut considerabil")
    print("felicitari")
    if populatie_bv > 330000:
        print("     populatia a crescut cu mai mult de 10%")
else:
    print("nu se nasc destui copii")


lista2 = [6,7,10,90,100,33,88,5,13]
#vrem sa printam numerele pare

# a + b
# a/b, a//b -> rezultatul impartirii
# a%b -> impartire cu rest, restul impartirii
# 5//3 = 1, 5%3=2

lista2 = [6,7,10,90,100,33,88,5,13,0]
nr_pare = []
nr_impare = []

for nr in lista2: #nr trece prin lista
    if nr % 2 == 0: #nr este par
        nr_pare.append(nr)
    else:
        nr_impare.append(nr)

print("Numerele pare sunt:")
print(nr_pare)

print("Numerele impare sunt:")
print(nr_impare)


#Expresii/ Porti logice

for nr in lista2:
    if nr % 2 == 0 and nr % 5 == 0:
        print("nr este par si multiplu de 5")
        print(nr)



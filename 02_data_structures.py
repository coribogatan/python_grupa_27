#liste

list1 = [4,5,10,20,30,100,500,999,1000]
print(list1[0])
print(list1[-1])

print(len(list1)//2)

index = len(list1)//2

print (list1[   index  ]   )

list2 = [0,1,2,50,100,100, 100,100,2,2,2,9,10,99]
print(list2)
#schimbam un element din lista folosint [] si punand indexul elementului in ele
list2[3] = 100
print(list2)

# DICTIONARE
#unordered
#key must be unique

persoana = {
    'key': 'valoare',
    'nume': 'Alex',
    'inaltime': '1.85m',
    'varsta': 27,
    'cetatean_roman': True,
    'bolnav': False,
    'greutate': 75.7,
}

#dict2 = {'key': 'valoare', 'nume': 'Alex', 'inaltime': '1.85m', 'varsta': 27, 'cetatean_roman': True, 'bolnav': False, 'greutate': 75.7}
#print (dict2)

print(persoana)

#fast lookup
print(persoana['key'])
print(persoana['varsta'])

persoana['inaltime'] = '3m'

persoana['CNP'] = '2831127314045'
print(persoana)

# cel mai intalnit tip de date >> boolean/ string (cuvinte)

#SETURI

elemset = {3,6,10,9,8,100,3}
print(elemset)

list2 = [0,1,2,50,100,100, 100,100,2,2,2,9,10,99]

list2_no_duplicates = set(list2)
print(list2_no_duplicates)

list4 = list(set(list2))
print(list4)

# TUPLU/ TUPLE lista fixa (inmutabke list)

coordinates = (0, 10)
coordinates3d = (0, 15, -5)

print(coordinates[1])

#METODE
#obiect.actiune/functie/metode (parametrii)

# catel = 'Spot'
# catel.latra('cioara')
# catel.mananca('peste')
# catel.miroase('adrian')
# catel.musca('adrian')

lista5= [7,8,100,99]
lista5.append(-50) #adauga element
print(lista5)

lista5.pop(1) #scoate elementul cu acel index
print(lista5)

lista5.reverse()
print(lista5)

lista5.sort()
print(lista5)

set2 = {7,6,8,8,10,90,100}
set2.add(-5)
set2.remove(90)
print(set2)

# CHEI DE DICTIONARE
dict_2 = {
    'key': 'value',
    1: 'one',
    3.14:'pi',
    True: False,
    (2,3): 'coordinates',
    'bizar': {
        'level12':{
            'list1':[0,1,2,3,100,99,-5]
        }
    }
}
print(dict_2)

print() #pune endline, ca si cum ai da Enter

print("end of file")


































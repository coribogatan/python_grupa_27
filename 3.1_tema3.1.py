# lista = ["Rosii", "Apa minerala", "Cafea"]
# var1 = ("1 - Afisare lista de cumparaturi")
# var2 = ("2 – Adaugare element")
# var3 = ("3 – Stergere element")
# var4 = ("4 – Stergere lista de cumparaturi")
# var5 = ("5 - Cautare in lista de cumparaturi")
#
# print(var1)
# print(var2)
# print(var3)
# print(var4)
# print(var5)
#
# option=int(input("Introduceti o optiune (1-5): "))
# print("Ati ales optiunea:", option)
#
# if option == 1:
#     print("Afisare lista de cumparaturi", lista)
# elif option == 2:
#     option1=str(input("Adaugare element. Ce element doriti sa adaugati? "))
#     lista.append(option1)
#     print("Noua lista este", lista)
# elif option == 3:
#     option3 = input("Stergere element. Ce element doriti sa stergeti? ")
#     if option3 in lista:
#         lista.remove(option3)
#         print("Elementul a fost sters.")
#         print("Noua lista este:", lista)
#     else:
#         print("Elementul nu se afla in lista.")
# elif option == 4:
#     del lista
#     print("Stergere lista de cumparaturi. Lista a fost stearsa!")
# elif option == 5:
#     option5=str(input("Cautare in lista de cumparaturi. Ce element doriti sa cautati? "))
#     if option5 in lista:
#         print("Elementul exista in lista. ")
#     else:
#         print("Elementul nu se afla in lista.")
# else:
#     print("Alegerea nu exista. Reincercati")


# var1 = ("1 - Afisare lista de cumparaturi")
# var2 = ("2 – Adaugare element")
# var3 = ("3 – Stergere element")
# var4 = ("4 – Stergere lista de cumparaturi")
# var5 = ("5 - Cautare in lista de cumparaturi")
# print(var1)
# print(var2)
# print(var3)
# print(var4)
# print(var5)

def optiune_lista_cumparaturi(list1):
    print("1 - Afisare lista de cumparaturi")
    print("2 – Adaugare element")
    print("3 – Stergere element")
    print("4 – Stergere lista de cumparaturi")
    print("5 - Cautare in lista de cumparaturi")
    # lista = ["Rosii", "Apa minerala", "Cafea"]
    option=int(input("Introduceti o optiune (1-5): "))
    if option == 1:
        print("Afisare lista de cumparaturi: ", list1)
    elif option == 2:
        option2 = str(input("Adaugare element. Ce element doriti sa adaugati? "))
        if option2 in list1:
            print("Elementul exista deja in lista de cumparaturi")
        else:
            list1.append(option2)
            print("Noua lista este", list1)
    elif option == 3:
        option3 = input("Stergere element. Ce element doriti sa stergeti? ")
        if option3 in list1:
            list1.remove(option3)
            print("Elementul a fost sters. Noua lista este", list1)
        else:
            print("Elementul nu se afla in lista.")
    elif option == 4:
        del list1
        print("Stergere lista de cumparaturi. Lista a fost stearsa!")
    elif option == 5:
        option5 = str(input("Cautare in lista de cumparaturi. Ce element doriti sa cautati? "))
        if option5 in list1:
            print("Elementul exista in lista. ")
        else:
            print("Elementul nu se afla in lista.")
    else:
        print("Alegerea nu exista. Reincercati")


lista = ["rosii", "apa minerala", "cafea"]
optiune_lista_cumparaturi(lista)
# terminalul are multiple stream-uri de text pe care le primeste si le afiseaza

# STDERR este stream-ul de erori

print("======= Inceput de curs exceptii: =======")
lista1 = [9, 10, 11, 33]

print(lista1)
print(lista1[3])

try:
    vari = int(input("De care index esti curios?"))
    print(lista1[vari])
# exception that is thrown from the int() conversion is caught as a ValueError
# exception that is thwouwn when accessing a non-existing index is caught as IndexError

except IndexError:
    print("we went to far")
except ValueError:
     print("you have to write an integer number")
except BaseException:
     print("you shall not pass!")
except BaseException:
     # don't do this
    pass


# exception bubble-up

var2 = 10
if var2 > 5:
    raise Exception("my variable is too high")

print("======= Sfarsit curs exceptii =======")








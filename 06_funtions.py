# functii - bucata de code care s epoate rula si reapela oricand; face codul reutilizabil; incapsuleaza o bucata de code
#primeste input si output

#definire functie
def greet(): # def e keyword; definim functia
    print("hello")
    print("this is flume")
#apelare functie
greet()


# a si b - parametri
def add(a,b):
    return a+b

# var2 = add(3,4)
# print(var2)

print(add(5, 10))
print(add(60,90))
print(add(100,333))

# mul
def mul(a, b):
    return a*b

var1 = mul(5, 15)
add(var1, 35)

#param se numeste a - argument este valoarea ce o dam parametrului - de ex 5

#creati sub, care scade a-b, div a/b si pow a**b

def sub(a,b):
    return a-b

def div(a,b):
    return a/b

def power(a,b):
    return a**b

# 6 - 4 * 10
rezultat = sub(6, mul(4, 10))
print(rezultat)

# 5 + 4 * 8 ** 2
rezultat2 = add(5, mul(4, pow(8, 2)))
print(rezultat2)

#return implicit, None
def speak(word="woof!"):
    print(word)
speak()
speak("meow!")

def drive(car_model, max_speed=130):
    print(f"{car_model} is running at a max speed of {max_speed}")

drive("Audi")
drive("Mazda", "red")

#typed function - adaugam ce tip de date avem

def modulo(a: int, b: int) -> int:
    """
    Return the remainder of the division between two numbers.
    :param a: the number that is devided
    :param b: the number that does the division
    :return: remainder
    """
    return a % b

#RST/ Sphinx style docs ^
print(modulo(13, 5))


nr = [10,11,21,5,-1,20,3]

def even_numbers(list1):
    # iteram prin lista. folosim modulo
    res = []
    for n in list1:
        if n % 2 == 0:
            print(f"am gasit numar par:{n}")
            res.append(n)
    return res


result = even_numbers(nr)
print(result)


nr2 = [7,22,4,5,-2,8,10]
result2 = even_numbers(nr2)
print(result2)













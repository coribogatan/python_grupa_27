import random
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





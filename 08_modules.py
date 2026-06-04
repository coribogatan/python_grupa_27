
import os

# operating system interaction

#operating system interaction

print(os.listdir())

if os.path.exists("manage.py"):
    print("Avem fisierul")
    print(os.path.getsize("manage.py"))
else:
    print("File not found")

#os.path.listdir() returneaza lista de foldere si fisiere
#os.path.isfile(fisier) - returneaza True daca "fisier" e fisier
#os.path.getsize(fisier) - marimea fisierului

#ex: Creati o functie care trece prin fisierele din folderul curent si returneaza marimea totala a fisierelor

# var1 = os.listdir()
# for n in var1:
#     if(os.path.isfile(n)) == True:
#         print(n)
#         print(os.path.getsize(n))
#         #print(f"Total size is: {sum(int(os.path.getsize(n)))}")

# print(os.path.isfile('abc.py'))
#
# print(os.path.getsize('abc.py'))

def total_files_size():
    """"
    Function that return file size for all files in root level directory.
    :return: total file size, in KB
    """
    files = os.listdir()
    total = 0
    for f in files:
        if(os.path.isfile(f)):
            marime = os.path.getsize(f)
            total = total + marime
    return total / 1024

#baza 2, nu baza 10
# 1 bit > 0 1
# 1 bite > 8 biti
# 1 kbyte = 2 ^ 8

print(total_files_size())




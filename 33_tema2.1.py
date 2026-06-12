cetateni = [
    {
        "CNP": 19304843895738,
        "Nume": "Marius Moga",
        "Varsta": 24,
        "Adresa": "Brasov, Jud Brasov",
        "Greutate": 75
    },
    {
        "CNP": 193048438345345,
        "Nume": "Matei Luca",
        "Varsta": 30,
        "Greutate": 70,
    },
    {
        "CNP": 293048438341234,
        "Nume": "Ana Pop",
        "Varsta": 26,
        "Greutate": 60.5,
    },
    {
        "CNP": 293048438341235,
        "Nume": "Luisa Crisan",
        "Varsta": 29,
        "Greutate": 55,
    },
    {
        "CNP": 193048438341235,
        "Nume": "Andrei Macarie",
        "Varsta": 31,
        "Greutate": 80,
    }
]

# print("Persoanele peste 25 ani si peste 60 kg sunt: ")
# for persoana in cetateni:
#     if persoana["Varsta"] >25 and persoana["Greutate"]>60:
#         print(persoana["Nume"])

def person_select(lista_persoane):
    selectie = []
    for persoana in lista_persoane:
        if persoana["Varsta"] > 25 and persoana["Greutate"] > 60:
            selectie.append(persoana["Nume"])
    return selectie


selection = person_select(cetateni)

if selection:
    print("Persoanele peste 25 ani si peste 60 kg sunt:")
    for nume in selection:
        print(nume)
else:
    print("Nu exista persoane care indeplinesc conditiile.")


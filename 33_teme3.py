var1 = ["ERR-Value Error-ER:10", "INF-Program launch Info-CD:5", "WRN-Low memory-WR:11"]

var2 = ["INF-Program exit-CD:14", "WRN-Low disk space-WR:99", "WRN-Bandwith reached-WR:87"]

# for s in var2:
#     if s.split("-")[0] == "ERR":
#         print("[ERROR]")
#     elif s.split("-")[0] == 'INF':
#         print("[INFO]")
#     elif s.split("-")[0] == 'WRN':
#         print("[WARNING]")
#     print(f"Mesaj: {s.split('-')[1]}")
#     # # s -> string :::: .split("-") -> list :::: [2] -> elem din lista dupa index :::: elem este string, deci s.split("-")[2] -> string :::: .split(":") -> list :::: acea_lista[1] -> al doilea element, care este numarul de cod ce ne intereseaza.
#     print(f"Cod: {s.split("-")[2].split(":")[1]}\n")

def text(var):
    for s in var:
        if s.split("-")[0] == "ERR":
            print("[ERROR]")
        elif s.split("-")[0] == 'INF':
            print("[INFO]")
        elif s.split("-")[0] == 'WRN':
            print("[WARNING]")
        print(f"Mesaj: {s.split('-')[1]}")
        print(f"Cod: {s.split("-")[2].split(":")[1]}\n")

text(var1)
text(var2)

print("Tema procesare stringuri")

for s in var2:
    if s.split("-")[0] == "ERR":
        print("[ERROR]")
    elif s.split("-")[0] == 'INF':
        print("[INFO]")
    elif s.split("-")[0] == 'WRN':
        print("[WARNING]")
    else: print(s.split("-")[0])
    print(f"Mesaj: {s.split('-')[1]}")
    print(f"Cod: {s.split("-")[2].split(":")[1]}\n")

#refactorizare: mutati code-ul intr-o functie si in loc de print folositi return un string care e mesajul formatat

def format_logs(param1):
    chunks = []
    for s in param1:
        if s.split("-")[0] == "ERR":
            chunks.append("[ERROR]")
        elif s.split("-")[0] == 'INF':
            chunks.append ("[INFO]")
        elif s.split("-")[0] == 'WRN':
            chunks.append ("[WARNING]")
        else:
            chunks.append(s.split("-")[0])
        chunks.append(f"Mesaj: {s.split('-')[1]}")
        chunks.append(f"Cod: {s.split("-")[2].split(":")[1]}\n")
    str_result = "\n".join(chunks)
    return str_result

result = format_logs(var2)
print(result)





def obj_constructor(name, owner, temperament = "Loving"):
    obj = {
        "name": name,
        "owner": owner,
        "temperament": temperament
    }
    return obj

cat1 = obj_constructor("Shadow", "Mark")
cat2 = obj_constructor("Paw", "Lydia", temperament="Feral")
cat2["name"] = "Shadow"

print(cat2)

cat3 = cat2
cat3["temperament"] = "Shy"

print(cat2)

cat4 = cat3.copy()
cat4["name"] = "Sol"

print(cat3)
print(cat4)

# cat1, cat2, cat3, cat4 - cate sloturi de memorie ocupa ytoate aceste obiecte?
# 2, 3 sau 4? - correct 3




















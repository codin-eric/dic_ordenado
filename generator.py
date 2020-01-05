"""
Generador de archivo json
"""

import random
import json

nombres = ["Juan", "Pedro", "Pablo", "Ignacio", "Julian", "Jose", "Mariano"]

dic_lst = []
for i in range(5):
    lista = [{index: random.randint(1, 100)} for index in nombres]

    dic_lst.extend(lista)

print(dic_lst)

with open("dic_lst.json", "w") as file:
    json.dump(dic_lst, file)

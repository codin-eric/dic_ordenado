"""
Leer de un json una lista de diccionarios con multiples keys repetidas
a una lista de diccionarios agrupando los elementos bajo las mismas
keys.

Con defaultdict() podes evitar el problema de las keys no existentes pero
no tenia internet y no me podia acordar el nombre de esa función
"""
import json

with open("dic_lst.json", "r") as file:
    lista_datos = json.load(file)

dic_datos = {}
for dic in lista_datos:
    for index, value in dic.items():
        if not dic_datos.get(index):
            dic_datos[index] = [value]
        else:
            dic_datos[index].append(value)

print(dic_datos)

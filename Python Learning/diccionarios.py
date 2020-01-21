midiccionario={"Alemania":"Berlin", "Francia":"Paris", "Espaia":"Madrid"}
midiccionario["Italia"]="Lisboa"
print(midiccionario)
midiccionario["Italia"]="Roma"
print(midiccionario)
del midiccionario["Espaia"]
print(midiccionario)

milista=["Espania", "Francia", "Reino Unido"]
midiccionario={milista[0]:"Madrid", milista[1]:"Paris", milista[2]:"Londres"}
print(midiccionario)

midiccionario2={"Alemania":"Berlin", 23:"Jordan", "Mosqueteros":3}
print(midiccionario2)

midiccionario3={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "Anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(midiccionario3)

print(midiccionario3.keys())
print(midiccionario3.values())
print(len(midiccionario3))
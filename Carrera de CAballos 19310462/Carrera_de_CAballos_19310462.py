import random
import numpy as np
import cv2
import networkx as nx
import matplotlib.pyplot as plt


#Competidores
Grupo_Papaya=["P1","P2","P3","P4","P5"]
Grupo_Coche=["C1","C2","C3","C4","C5"]
Grupo_Amor=["A1","A2","A3","A4","A5"]
Grupo_Netflix=["N1","N2","N3","N4","N5"]
Grupo_Madagascar=["M1","M2","M3","M4","M5"]
print('Carrera 1:',Grupo_Papaya)
print('Carrera 2:',Grupo_Coche)
print('Carrera 3:',Grupo_Amor)
print('Carrera 4:',Grupo_Netflix)
print('Carrera 5:',Grupo_Madagascar)

#Arreglos de Velocidad

Velocidad=np.zeros((5,5))
Dimension=Velocidad.shape
for x in range(Dimension[0]):
    for y in range(Dimension[0]):
        Velocidad[x,y]=random.randint(1,200)
print('\nResultados')

for x in range(5):
    Velocidad[x].sort()

Velocidad=Velocidad[np.argsort(Velocidad[:,-1])]
for x in range(5):
    print("Carrera",5-x,":",Velocidad[x])
#Arreglo Para las primeras 5 carreras
for x in range(5):
    print('ganador grupo',5-x,Velocidad[x,4])
#Arreglo de carrera 6
Carrera_6 =Velocidad[np.argsort(Velocidad[:, -1])]
Carrera_6.sort()
for x in range(5):
  print(Carrera_6[x]) 
print("Carrera 6:", Carrera_6, "\n")  
print("Caballo más rapido: ", int(Carrera_6[4,4]), "Velocidad tope\n")
#Arreglo de carrera 7
Carrera_7= [Carrera_6[2, 4], Carrera_6[3, 4], Carrera_6[3, 3], Carrera_6[4, 3], Carrera_6[4, 2]]
Carrera_7.sort()
print("Carrera 7:", Carrera_7, "\n")
print ("Caballo en segundo lugar: ", int(Carrera_7[4]), "Velocidad tope")
print(" Podio:\n primer lugar: ",int(Carrera_6[4,4]),"en velocidad tope ","\n En segundo lugar: ",int(Carrera_7[4]),"en velocidad tope")


#Grafo
Primer_Lugar= Carrera_6[4,4]
Segundo_Lugar= Carrera_7[4]
Podio = nx.Graph()  
Podio.add_edge('Podio ',Primer_Lugar) 
Podio.add_edge('Podio ',Segundo_Lugar) 
fig, ax = plt.subplots()
nx.draw(Podio, ax=ax, with_labels=True, )
plt.show()


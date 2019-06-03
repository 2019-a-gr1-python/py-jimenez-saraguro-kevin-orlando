import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


columnas_a_usar = [
    'name',
    'ID',
    'ALIGN',
    'SEX',
    'GSM',
    'ALIVE',
    'APPEARANCES',
    'FIRST APPEARANCE'
    ,'YEAR']
contenido_archivo = pd.read_csv(
    'dc-data.csv',
    usecols=columnas_a_usar
    )

print(contenido_archivo['name'].max())
grupo_personajes_bando_genero = contenido_archivo.groupby(["ALIGN","SEX"])['name']
total_personajes_x_ALIGN_SEX = []
ALIGN_SEX = []

for indice,personaje, in enumerate(grupo_personajes_bando_genero):
    print(personaje[0][0] + "  "+ personaje[0][1], (personaje[1].count()))
    ALIGN_SEX.append(personaje[0][0] + " - " +personaje[0][1])
    total_personajes_x_ALIGN_SEX.append(len(personaje[1]))
    
    
# Plot
plt.pie(total_personajes_x_ALIGN_SEX,labels=ALIGN_SEX,
autopct='%1.1f%%')
plt.legend(ALIGN_SEX, loc="best")
plt.axis('equal')
plt.show()


index = np.arange(len(ALIGN_SEX))
#plt.xlabel('En x')
#plt.ylabel('En y')
#plt.plot(ALIGN_SEX,total_personajes_x_ALIGN_SEX,'ro')
#plt.xticks(index, ALIGN_SEX, fontsize=5, rotation=90)



#print(index)
plt.bar(index, total_personajes_x_ALIGN_SEX)
plt.xlabel('Generos y Bandos', fontsize=5)
plt.ylabel('No de Personajes', fontsize=5)
plt.xticks(index, ALIGN_SEX, fontsize=5, rotation=90)
plt.title('Numero de personajes por bando y genero de DC Comics')
plt.show()


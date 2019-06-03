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

contenido_archivo_csv_DCComics = pd.read_csv(
    'dc-data.csv',
    usecols=columnas_a_usar
    )

grupo_personajes_bando_sexo = contenido_archivo_csv_DCComics.groupby(["ALIGN","SEX"])['name']
total_personajes_x_bando_sexo = []
bando_sexo = []

for personaje in grupo_personajes_bando_sexo:
    bando_sexo.append(personaje[0][0] + " - " +personaje[0][1])
    total_personajes_x_bando_sexo.append(len(personaje[1]))
    
    



index = np.arange(len(bando_sexo))
plt.bar(index, total_personajes_x_bando_sexo)
plt.xlabel('Generos y Bandos', fontsize=5)
plt.ylabel('No de Personajes', fontsize=5)
plt.xticks(index, bando_sexo, fontsize=5, rotation=90)
plt.title('Numero de personajes por bando y genero de DC Comics')
plt.show()

################################################
grupo_personajes = contenido_archivo_csv_DCComics.groupby(["ALIVE"])['name']
arreglo_alive = []
total_personajes_alive = []
print(grupo_personajes)
for tipo,personaje in  grupo_personajes:
    arreglo_alive.append(tipo)
    total_personajes_alive.append(len(personaje))
    print(tipo)
    print(personaje)

# Plot
plt.pie(total_personajes_alive,labels=arreglo_alive,
autopct='%1.1f%%')
plt.legend(arreglo_alive)
plt.axis('equal')
plt.show()
#########################################
arreglo_gsm_sex=[]
arreglo_total_gsm_sex=[]

grupo_personajes_sex_gsm = contenido_archivo_csv_DCComics.groupby(["GSM","SEX"])['name']
for tipo,personaje in grupo_personajes_sex_gsm:
    arreglo_gsm_sex.append(tipo)
    arreglo_total_gsm_sex.append(len(personaje))
    print(tipo)
    print(personaje)
    
plt.pie(arreglo_total_gsm_sex,labels=arreglo_gsm_sex,
autopct='%1.1f%%')
plt.legend(arreglo_gsm_sex)
plt.axis('equal')
plt.show()


grupo_personajes_anio = contenido_archivo_csv_DCComics.groupby(["YEAR","GSM","SEX"])['name'].apply(list)
print(type(grupo_personajes_anio),grupo_personajes_anio)
"""
total_mecos_90 = 0
total_mecos_2000 = 0
contador = 0
for index,personajes in enumerate(grupo_personajes_anio.items()):
    
    if (personajes[0][0] < 1990 and personajes[0][1] == 'Bisexual Characters'):
        total_mecos_90 = len(personajes[1]) + total_mecos_90
        print(personajes[0][0])
        
    elif (personajes[0][0] > 1990 and personajes[0][0] < 2000 and personajes[0][1] == 'Bisexual Characters'):
        total_mecos_2000 = len(personajes[1]) + total_mecos_2000
        print(personajes[0][0])
    else:
        contador = len(personajes[1]) + contador        
        print(personajes[0][0])
            
print(total_mecos_90)
print(total_mecos_2000)
print(contador)  

"""    
#print(grupo_personajes_anio)
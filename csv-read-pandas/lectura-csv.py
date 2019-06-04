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
df_personaje_anio = pd.DataFrame(grupo_personajes_anio)


total_mecos_90_bi = 0
total_mecos_90_ho = 0
total_mecos_2000_bi = 0
total_mecos_2000_ho = 0
total_mecos_2010_bi = 0
total_mecos_2010_ho = 0
for index,personajes in enumerate(grupo_personajes_anio.items()):
    
    if (personajes[0][0] < 1990): 
        if (personajes[0][1] == 'Bisexual Characters'):
            total_mecos_90_bi = len(personajes[1]) + total_mecos_90_bi            
        else:
            total_mecos_90_ho = len(personajes[1]) + total_mecos_90_ho
            
    if (personajes[0][0] > 1990 and personajes[0][0] < 2000): 
        if (personajes[0][1] == 'Bisexual Characters'):
            total_mecos_2000_bi = len(personajes[1]) + total_mecos_2000_bi            
        else:
            total_mecos_2000_ho = len(personajes[1]) + total_mecos_2000_ho
    
    if (personajes[0][0] < 2000): 
        if (personajes[0][1] == 'Bisexual Characters'):
            total_mecos_2010_bi = len(personajes[1]) + total_mecos_2010_bi            
        else:
            total_mecos_2010_ho = len(personajes[1]) + total_mecos_2010_ho
    
        
print(total_mecos_90_bi)
print(total_mecos_90_ho)
print(total_mecos_2000_bi)
print(total_mecos_2000_ho)
print(total_mecos_2010_bi)
print(total_mecos_2010_ho)
anios = ['< 1990','1900 - 2000','2000 >',]
datos_personajes = [[total_mecos_90_bi,total_mecos_90_ho],[total_mecos_2000_bi,total_mecos_2000_bi],[total_mecos_2010_bi,total_mecos_2010_bi]]
print(datos_personajes[0])
#index = np.arange(3)
#plt.bar(index, datos_personajes[0], color = "b", width = 0.25)
#plt.bar(index, datos_personajes[1], color = "g", width = 0.25)
#plt.bar(index, datos_personajes[2], color = "r", width = 0.25)
#plt.xticks(index, anios, fontsize=5, rotation=90)
#plt.title('Numero de personajes por bando y genero de DC Comics')
#plt.show()


datos = [[1, 2, 3], [3, 5, 3], [8, 6, 4]]
X = np.arange(4)
plt.bar(X + 0.00, datos[0], color = "b", width = 0.25)
plt.bar(X + 0.25, datos[1], color = "g", width = 0.25)
plt.bar(X + 0.50, datos[2], color = "r", width = 0.25)
plt.xticks(X+0.38, ["A","B","C","D"])

#print(grupo_personajes_anio)
import json

def calculadora(numero_uno,numero_dos,operacion="sumar"):

    def crear_archivo():
        contenido = {
            "consolas":[]
        }
        try:
            archivo_leido = open("./prueba.json","x")
            archivo_leido.write(json.dumps(contenido))
            archivo_leido.close()
            return True
        except Exception as error:
            return False

    def leer_archivo():        
        if crear_archivo():
            crear_archivo()
            return 'archivo creado'
        else:                
            try:
                archivo_leido = open("./prueba.json","r") # r por defecto                
                contenido = json.loads(archivo_leido.read())                                
                archivo_leido.close()
                return contenido                
            except Exception as error:                
                return False

    def escribir_archivo(registro):    
        print("mi regitro",registro)    
        contenido = leer_archivo()  
        if contenido:
            try:                                               
                contenido['consolas'].append(registro)                
                archivo_escribir = open("./prueba.json","w") # r por defecto                
                nuevo_registro = json.dumps(contenido)                
                archivo_escribir.write(nuevo_registro)
                archivo_escribir.close()
                return 'registro creado'                
            except Exception as error:                
                return "Hubo un error"
        else:
            return 'error al leer'
            

    def crear_registro():
        print("Nombre de la empresa")
        empresa = input()        
        print("Nombre de la consola")
        consola = input()        
        print("Precio de la consola")
        precio = input()        
        registro = {
            "empresa":empresa,
            "consola":consola,
            "precio":precio
        }
        escribir_archivo(registro)
        return "registro creado"


    def listar_registros():
        contenido = leer_archivo()
        if contenido:
            for consola in contenido['consolas']:
                print('Empresa: ',consola["empresa"] ,'-','Consola:',consola["consola"],'-','Precio:',consola["precio"])
        else:
            print('error')        
        

    def operacionesCalculadora():
        return{            
            "crear_archivo":listar_registros()
        }[operacion]

    return operacionesCalculadora()


print(calculadora(2,3,'crear_archivo'))
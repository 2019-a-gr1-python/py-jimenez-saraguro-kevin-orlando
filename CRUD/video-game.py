import json

def CRUD_consolas(operacion):

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
        existe_archivo = crear_archivo()                
        if existe_archivo:
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

    def escribir_archivo(contenido):                        
        if contenido:
            try:                                                                             
                archivo_escribir = open("./prueba.json","w") # r por defecto                
                nuevo_contenido = json.dumps(contenido)                
                archivo_escribir.write(nuevo_contenido)
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
        contenido = leer_archivo()
        contenido['consolas'].append(registro)  
        escribir_archivo(contenido)
        return "registro creado"


    def listar_registros():
        contenido = leer_archivo()
        if contenido:
            for consola in contenido['consolas']:
                print('Empresa: ',consola["empresa"] ,'-','Consola:',consola["consola"],'-','Precio:',consola["precio"])                
        else:
            print('error')      
            return False


    def eliminar_registro():
        print('Ingrese el nombre de la consola a eliminar')
        nombre_consola = input()
        contenido = leer_archivo()
        for inidice, consola in enumerate(contenido['consolas']):            
            existe_consola = consola['consola'] == nombre_consola
            if existe_consola: 
                contenido['consolas'].pop(inidice)
                escribir_archivo(contenido)
                break
        return "registro eliminado"

    def modificar_registro():
        print('Ingrese el nombre de la consola a eliminar')
        nombre_consola = input()
        contenido = leer_archivo()
        for inidice, consola in enumerate(contenido['consolas']):            
            existe_consola = consola['consola'] == nombre_consola
            if existe_consola: 
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
                contenido['consolas'][inidice] = registro
                escribir_archivo(contenido)
                return "registro EDITADO"

    def operaciones_CRUD():
        return{            
            1:crear_registro(),
            2:listar_registros(),
            3:eliminar_registro(),
            4:modificar_registro()
        }[operacion]

    return operaciones_CRUD()


print(CRUD_consolas(2))
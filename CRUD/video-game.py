import json

def calculadora(numero_uno,numero_dos,operacion="sumar"):
    def sumar():
        return numero_uno + numero_dos

    def restar():
        return numero_uno - numero_dos

    def dividir():
        return numero_uno / numero_dos

    def multiplicar():
        return numero_uno * numero_dos

    
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
                #contenido['consolas'].append(json.dumps({"nombre":"ps4","precio":400.99}))                
                return contenido['consolas']                
            except Exception as error:                
                return "Hubo un error"+error
        

    def operacionesCalculadora():
        return{
            "sumar":sumar(),
            "restar":restar(),
            "multiplicar":multiplicar(),
            "crear_archivo":leer_archivo()
        }[operacion]

    return operacionesCalculadora()


print(calculadora(2,3,'crear_archivo'))
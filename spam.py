# Octubre 2, 2022

import json
from pathlib import Path
from mensajes import limp

# Imprime el mensaje con la probabilidad de spam
# Palabras -> Lista de palabras a validar
# Diccionario -> Diccionario de palabras con sus probabilidades
def getProbabilidad(Palabras, Diccionario):
    Suma = 0
    Contador = 0
    ContadorNo = 0
    for i in Palabras:
        Value = Diccionario.get(i)
        if  Value != None:
            Suma = Suma + float(Value)
            Contador = Contador + 1
        else: ContadorNo = ContadorNo + 1
    if Contador > 0:
        print(f"\nPalabras encontradas en la base de conocimiento: {Contador} / {ContadorNo + Contador}\nProbabilidad de ser spam: {int(Suma / Contador * 100)}%")
    else: print("No se encontro ninguna palabra en la base de conocimiento :(")

def main():
    print("\n******************************************\n* Diana Axelle Grande Mendoza	18590586 *\n* Erwin Martínez Pérez		17590511 *\n* Evelyn Sarahi Flores Silva\t18590223 * \n******************************************\n")

    JPATH = '.'
    JPALABRAS = 'BC_Palabras.json'
    Ruta = Path(JPATH) / JPALABRAS
    NoPalabras = []
    NoPalabras2 = []

    # Se crean dos listas, una donde estan las frases que no deben de contar al momento de crear las
	# probabilidadesy otra en donde estan las palabras
    with Path('./LPalabras.json').open() as N:
        for i in list(map(lambda i: i[0], list(json.load(N)))):
            if len(i.split()) > 1: NoPalabras2.append(i.upper())
            else: NoPalabras.append(i.upper())

    # Se limpian los datos y se obtiene la probabilidad
    if Ruta.exists():
        with Ruta.open() as P: Palabras = json.load(P)
        Mensaje = input("Ingresa el texto a analizar: ").upper()
        for i in NoPalabras2:
            if i in Mensaje: Mensaje = Mensaje.replace(i, '')
        getProbabilidad(list(set(limp(Mensaje).split()) - set(NoPalabras)), Palabras)
    else: print(f"No existe {JPALABRAS}")

if __name__ == "__main__":
    main()
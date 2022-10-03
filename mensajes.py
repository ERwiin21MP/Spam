# Octubre 2, 2022

import json
from pathlib import Path

# Retorna una palabra libre de caracteres especiales
#Palabra -> Palabra a limpiar de caracteres
def limp(Palabra):
	for caracter in ['¿', '!', '\"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~' '»', '«']:
		if caracter in Palabra: Palabra = Palabra.replace(caracter, '')
	return Palabra

# Retorna una lista de todas las palabras de SPAM o de NO_SPAM
# Key -> Puede ser SPAM o NO_SPAM, depende de lo que se quiera obtener
# D -> Diccionario al que se le va a sacar la informacion
def getPalabras(Key, D):
	Lista = []
	for i in list(D.get(Key)):
		for j in i:
			Lista.append(j)
	return Lista

# Retorna la longitud de la cadena mas grande dentro de una lista
# Lista -> Lista de cadenas a evaluar
# N -> Longitud inicial
def longitud(Lista, N):
	for i in Lista:
		if len(str(i)) > N:
			N = len(i)
	return N + 2

# Retorna un renglon de la tabla de impresion
# Lon -> Veces que se va imprimir - en la tabla
def ren(Lon):
	S = "+"
	for i in Lon:
		for j in range(i):
			S = S + "-"
		S = S + "+"
	return S

# Retorna el numero de veces que se encontro una palabra dentro de una lista
# i -> Palabra a buscar
# Lista -> Lista donde se va a buscar
def getCount(i, Lista):
	Contador = 0
	for j in Lista:
		if i == j: Contador = Contador + 1
	return Contador

# Retorna la palabra con los espacios necesarios para que se imprima correctamente la tabla
pal = lambda Cadena, Longitud: Cadena + ' ' * (Longitud - len(Cadena) - 2)

#Función principal
def main():
	print("\n******************************************\n* Diana Axelle Grande Mendoza	18590586 *\n* Erwin Martínez Pérez		17590511 *\n* Evelyn Sarahi Flores Silva\t18590223 * \n******************************************\n")

	SPAM = 'SPAM'
	NO_SPAM = 'NoSPAM'
	D = {SPAM: [], NO_SPAM: []}
	NoPalabras = []
	NoPalabras2 = []
	TodasLasPalabras = []
	Contador_Spam = []
	Contador_NoSpam = []
	PS = []
	P = []

	# Se crean dos listas, una donde estan las frases que no deben de contar al momento de crear las
	# probabilidadesy otra en donde estan las palabras
	with Path('./LPalabras.json').open() as N:
		for i in list(map(lambda i: i[0], list(json.load(N)))):
			if len(i.split()) > 1: NoPalabras2.append(i.upper())
			else: NoPalabras.append(i.upper())

	# Se abre el archivo que contiene los mensajes y los guarda en D
	with (Path('.').resolve() / 'mensajes.txt').open() as Mensaje:
		Key = SPAM
		for Linea in Mensaje:
			for i in NoPalabras2:
				if i in Linea: Linea = Linea.replace(i, '')
			if not '###' in Linea: D[Key].append([limp(e) for e in [e for e in Linea.upper().strip().split(' ') if e]][:])
			else: Key = NO_SPAM

	# Se guarda todas las palabras del archivo en la lista TodasLasPalabras
	for i in list(D.values()):
		for j in i:
			for k in j: TodasLasPalabras.append(k)

	# Se eliminan las prepociciones y las palabras repetidas
	PalabrasUnicas = list(set(TodasLasPalabras) - set(NoPalabras))
	PalabrasUnicas.sort()

	# Se obtiene un listado de todas las palabras de spam y no spam
	Spam = getPalabras(SPAM, D)
	NoSpam = getPalabras(NO_SPAM, D)

	# Se obtiene los contadores
	for i in PalabrasUnicas:
		Contador = getCount(i, Spam)
		Contador2 = getCount(i, NoSpam)
		Contador_Spam.append(str(Contador))
		Contador_NoSpam.append(str(Contador2))
		PS.append(f"{Contador}/{Contador + Contador2}")
		P.append(str("{:.4f}".format(Contador / (Contador + Contador2))))

	# Se guarda un diccionario de clave valor, donde la clave es la palabra y el valor es la probabilidad de spam
	J = dict()
	for i in range(len(PalabrasUnicas)): J[PalabrasUnicas[i]] = P[i]

	# Se guarda en un archivo el diccionario creado
	with Path('./BC_Palabras.json').open('w') as out: out.write(json.dumps(J))

	# Se obtiene las longitudes mayores de las cadenas
	Longitudes = [longitud(PalabrasUnicas, 7), longitud(Contador_Spam, 4), longitud(Contador_NoSpam, 7), longitud(PS, 4), longitud(P, 1)]

	# Se imprime el encabezado de la tabla
	print(f"{ren(Longitudes)}\n| {pal('Palabra', Longitudes[0])} | {pal('Spam', Longitudes[1])} | {pal('No Spam', Longitudes[2])} | {pal('P(S)', Longitudes[3])} | {pal('%', Longitudes[4])} |\n{ren(Longitudes)}")

	# Se imprime la tabla
	for i in range(len(PalabrasUnicas)):
		print(f"| {pal(PalabrasUnicas[i], Longitudes[0])} | {pal(Contador_Spam[i], Longitudes[1])} | {pal(Contador_NoSpam[i], Longitudes[2])} | {pal(PS[i], Longitudes[3])} | {pal(P[i], Longitudes[4])} |\n{ren(Longitudes)}")

if __name__ == "__main__":
    main()
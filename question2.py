import re

def mostrar_introduccion():
    print("Este programa compara dos archivos de texto")
    print("e informa el número de palabras en común y el porcentaje de coincidencias")
    print()

def obtener_palabras(archivo):
    palabras = {}
    try:
        with open(archivo, 'r') as f:
            texto = f.read()
            palabras_encontradas = re.findall(r'\b\w+\b', texto.lower())
            for palabra in palabras_encontradas:
                palabras[palabra] = palabras.get(palabra, 0) + 1
        return palabras
    except FileNotFoundError:
        print("Error: El archivo no se encuentra.")
        return None

def obtener_coincidencias(diccionario1, diccionario2):
    coincidencias = {}
    for palabra, conteo1 in diccionario1.items():
        if palabra in diccionario2:
            conteo2 = diccionario2[palabra]
            minimo_conteo = min(conteo1, conteo2)
            coincidencias[palabra] = minimo_conteo
    return coincidencias

def mostrar_resultados(diccionario1, diccionario2, coincidencias):
    print("Palabras en el Archivo #1 =", len(diccionario1))
    print("Palabras en el Archivo #2 =", len(diccionario2))
    print("Palabras en común =", len(coincidencias))

    porcentaje1 = 100.0 * len(coincidencias) / len(diccionario1)
    porcentaje2 = 100.0 * len(coincidencias) / len(diccionario2)

    print("% del Archivo #1 en superposición =", porcentaje1)
    print("% del Archivo #2 en superposición =", porcentaje2)

def main():
    mostrar_introduccion()

    archivo1 = input("Nombre del Archivo #1? ")
    archivo2 = input("Nombre del Archivo #2? ")

    diccionario1 = obtener_palabras(archivo1)
    diccionario2 = obtener_palabras(archivo2)

    if diccionario1 is not None and diccionario2 is not None:
        coincidencias = obtener_coincidencias(diccionario1, diccionario2)
        mostrar_resultados(diccionario1, diccionario2, coincidencias)

if __name__ == "__main__":
    main()

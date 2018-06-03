def pick_file():
    ''' (None) -> StringPath Función que abre un diálogo para seleccionar un archivo y devuelve el path del archivo
    NOTA: Si el usuario pulsa "Cancelar", el valor devuelto será cadena vacía ("") '''
    from tkinter import Tk
    from tkinter import filedialog

    Tk().withdraw() # No queremos una GUI completa, así que se oculta el resto de la GUI
    filename = filedialog.askopenfilename(initialdir="../ven", title="fichero",
                                            filetypes=(("txt files", "*.txt"),
                                                ("all files", "*.*"))) # Mostramos un Diálogo para abrir ficheros

    return filename # Se regresa el path

def open_AFD(path):
    ''' (StringPath) -> AFD '''
    # Abrimos el fichero que contiene el AFD
    fich = open(path, 'r')  # Ruta del fichero, solo lectura

    # Empezamos leyendo el alfabeto
    alfabeto = fich.readline().split()

    # Definimos los estados
    estados = []
    edoini = []
    edosfin = []

    transiciones = []

    # Leemos todos los estados
    linea = fich.readline()
    while linea:
        linea = linea.replace("\n", "")
        tokens = linea.split()

        # Si nos indica que es el estado inicial
        if (tokens[0] == 'i'):
            if (len(edoini) > 1):
                sys.exit("\nERROR: Se encontró más de un estado inicial.\n")
            edoini.append(tokens[1])
            estados.append(tokens[1])
            tokens = tokens[2:]

        # Si nos indica que es un estado final
        elif (tokens[0] == 'f'):
            edosfin.append(tokens[1])
            estados.append(tokens[1])
            tokens = tokens[2:]

        # Los que no entran en los casos anteriores
        else:
            estados.append(tokens[0])
            tokens = tokens[1:]

        transiciones.append(tokens)

        # Actualizamos
        linea = fich.readline()

    print("El archivo se ha cargado correctamente")

    # Podríamos considerar una buena idea implementar una tablahash de tablashash
    # El modo de acceso sería:
    # transhash[edoactual][elemento_entrante]
    # Lo comentado anteriormente se verá con más detalle después
    # Comenzamos a crear nuestro AFD (transhash)
    i = 0
    j = 0
    transhash = {}
    for edo in estados:
        transhash[edo] = {}  # Para cada estado en las transiciones, añadimos su dict/hash asociado a la letra
        for letra in alfabeto:
            transhash[edo][letra] = transiciones[i][j]
            j += 1
        i += 1
        j = 0
    print("Se ha creado la tabla de transiciones con exito")
    print("El alfabeto válido es el siguiente:")
    print(alfabeto, "\n")


    return alfabeto, edoini[0], edosfin, transhash


def validar_cadena(cadena):
    ''' (str) -> bool Se valida si la cadena proporcionada es una palabra válida para el autómata '''

    alfabeto, edoini, edosfin, transhash = open_AFD(pick_file())

    edoactual = edoini
    char = cadena[0]
    n = len(cadena)
    i = 0
    while (i != n):
        if (not (char in alfabeto)):
            return False  # Se dió una cadena que no está dentro del alfabeto válido
        if (transhash[edoactual][char] == '-'):
            return False  # Se encontró que no es válido y no pertenece al lenguaje aceptado por el autómata

        edoactual = transhash[edoactual][char]
        i += 1
        if (len(cadena) == i):
            break
        char = cadena[i]

    if edoactual in edosfin:
        return True  # Terminó bien el recorrido y en un estado final

    return False  # Terminó en un estado NO FINAL

if __name__ == '__main__':

    if validar_cadena(input("\nIntroduce la cadena a validar\n>>> ")):
        print("La cadena es válida :D")
    else:
        print("La cadena NO ES VALIDA")
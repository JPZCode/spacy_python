# Programa que regresar la categoría a la que pertenece una paralabra determinada.
# Autor: J. Pamela y Marco A.

word = input("Introduce una cadena de texto: ")

def words(word):

    wd = {
    #Teacher  #
        "maestro" : "teacher",
        "maestra" : "teacher",
        "profesor" : "teacher",
        "profesora" : "teacher",
        "asesor" : "teacher",
        "asesora" : "teacher",
        "doctor" : "teacher",
        "doctora" : "teacher",
        "ingeniero" : "teacher",
        "ingeniera" : "teacher",
        "licenciado" : "teacher",
        "licenciada" : "teacher",
        "docente" : "teacher",
    # Place  #
        "salón" : "place",
        "laboratorio" : "place",
        "edificio" : "place",
        "cubículo" : "place",
    # Email  #
        "correo electrónico" : "email",
        "correo" : "email",
        "email" : "email",
        "e-mail" : "email",
    # Telephone  #
        "teléfono" : "telephone",
        "celular" : "telephone",
        "número telefónico" : "telephone",
        "teléfono celular" : "telephone",
    # Horary #
        "horario" : "horary",
        "carga de horario" : "horary",
        "día" : "horary",
        "hora" : "horary"
    }

    for i in wd:
        x = wd.get(word)
        print(x)
        break

words(word);
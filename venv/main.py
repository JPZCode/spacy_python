import spacy
nlp = spacy.load('es')

questions = [
    #Teléfono de profesores
    u'¿Cuál es el teléfono del profesor Alejandro Vargas?',
    u'¿Cuál es el teléfono de la maestra Reyna Beltran?',
    u'¿Cuál es el teléfono del maestro Valerio?',
    u'¿Cuál es el teléfono de la profesora Martha Luz?',
    u'¿Cuál es el teléfono celular de la maestra Chabero?',
    u'¿Cuál es el teléfono celular de la profesora Martha Luz?',
    u'¿Cuál es el teléfono celular del maestrao Rincones?',
    u'¿Cuál es el teléfono celular de la maestra Ana?',
    # #Correo de profesores
    u'¿Cuál es el correo del profesor Rincones?',
    u'¿Cuál es el correo de Reyna Beltran?',
    #Horario de profesores
    u'¿Cuál es el horario de la mañana del profesor Melchorl Leal Suárez?',
    u'¿Cuál es el horario de la tarde de la maestra Reyna Beltran?',
    u'¿Cuál es el horario de la noche de Alejrandro Vargas?',
    #Lugar donde se encuentra
    u'¿Dónde se encuentra el profesor Alejandro Vargas?',
    u'¿Cuál es el salón donde está el profesor Melchor Adrian Leal Suárez?',
    u'¿Cuál es el salón donde se encuentra el profesor Caracheo?',
    #Teléfono, Correo, Horario, Lugar
    u'¿Cuál es el teléfono y correo del profesor Melchor?',
    u'¿Cuál es el teléfono, correo y horario la maestra Rosio?',
    u'¿Cuál es el teléfono, correo y horario la profesora Juanita?',
    u'¿Cuál es el teléfono, correo, horario y salón del maestro Fernández?',
    u'¿Cuál es el correo y teléfono de Acuña?',
    u'¿Cuál es el correo, teléfono y horario del doctor Salvador?',
    u'¿Cuál es el correo, teléfono, horario y salòn de Vargas Diaz?',
    u'¿Cuál es el horario y teléfono de la mestra Erika del Río?',
    u'¿Cuál es el horario, teléfono, correo y salón de la profesora Magalhy?',
    u'¿Cuál es el salón, teléfono, correo y horario del maestro Acuña?',
    #Personas ayudando a la causa
    u'¿Qué correo utiliza el profesor Alex Vargas?',
    u'¿En dónde se encuentra el profesor Alex Vargas?',
    u'¿En dónde se encuentra Alex Vargas?',
    u'¿Cuál es el horario del profesor Vargas Diaz?',
    u'¿En que salón se encuentra el profesor Alejandro Vargas Diaz?',
    u'¿Cuál es el horario de clases del profesor Acuña?',
    u'¿Cuál es la experiencia del profesor Rincones?',
    u'¿Cuál es el salón, teléfono, correo y horario del maestro Acuña y de la mestra Magalhy?'
    ]

for question in questions:
    doc = nlp(question)

    patron = ''

    for token in doc:
        patron = patron + token.pos_ + ' '

    print(patron)
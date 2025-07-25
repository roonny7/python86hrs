print('*** Agenda de contactos ***')
agenda = {
    "Carlos" : {
        "telefono" : "789454",
        "email" : "carlos@gmail.com",
        "direccion" : "conocida"
    },
    "Maria" : {
        "telefono": "12487",
        "email": "maria@gmail.com",
        "direccion": "direccion de maria"
    },
    "Pedro": {
        "telefono": "12487",
        "email": "pedro@gmail.com",
        "direccion": "Plaza pedro"
    }
}

print(f'La agenda es : {agenda}')

# Acceder a la información de un contacto en específico
print(f'''Información del contacto de María :
    Teléfono : {agenda['Maria']['telefono']}
    Email : {agenda.get('Maria').get('email')}
    Email : {agenda.get('Maria').get('direccion')}
''')

# Agregar un nuevo contacto
agenda['Ana'] = {
    "telefono" : "878454",
    "email" :  "analawanga@gmail.com",
    "direccion" : "avenida siempre viva"
}
print(f'La agenda es : {agenda}')

# Eliminar un contacto, cualquira de los dos
agenda.pop('Pedro')
#del agenda['Pedro']
print(f'La agenda es : {agenda}')

#Mostramos los contactos de la agenda
print(f'\nContactos de la agenda')
for nombre, detalles in agenda.items():
    print(f'''Nombre : {nombre}
    Teléfono : {detalles.get('telefono')}
    Email : {detalles['email']}
    Dirección : {detalles['direccion']}''')
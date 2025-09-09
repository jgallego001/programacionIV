def obtenerDatosDelUsuario():
    print('Ingrese las características del cultivo a consultar.')

    datosUsuario = {
        "departamento": input('Departamento:  ').upper(),
        "municipio": input('Municipio:  ').upper(),
        "cultivo": input('Tipo de cultivo:  ').capitalize(),
        "nRegistros": int(input('Número de registros a consultar:  '))
    }

    return datosUsuario

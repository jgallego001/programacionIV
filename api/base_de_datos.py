import pandas as pd
from ui.datos_de_usuario import obtenerDatosDelUsuario

pd.set_option("display.max_columns", None)  # Muestra todas las columnas
pd.set_option("display.max_rows", None)     # (Opcional) Muestra todas las filas

pd.set_option("display.float_format", "{:.2f}".format) #Muestra los números grandes sin notación científica

def importarDatos(archivo):
    dataFrame = pd.read_excel(archivo, engine="openpyxl")

    return dataFrame


def filtrarDatos(dataFrame, inputUsuario):
    depto = inputUsuario["departamento"]
    municipio = inputUsuario["municipio"]
    cultivo = inputUsuario["cultivo"]
    numRegistros = inputUsuario["nRegistros"]

    dfFiltrado = dataFrame[(dataFrame["Departamento"] == depto) &
                           (dataFrame["Municipio"] == municipio) &
                           (dataFrame["Cultivo"] == cultivo)][:numRegistros]
    return dfFiltrado


def retornarDatos():
    return filtrarDatos(importarDatos("resultado_laboratorio_suelo.xlsx"), obtenerDatosDelUsuario())


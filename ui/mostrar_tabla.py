import pandas as pd
from tabulate import tabulate
from api.base_de_datos import retornarDatos

pd.set_option("display.max_columns", None)  # Muestra todas las columnas
pd.set_option("display.max_rows", None)     # (Opcional) Muestra todas las filas

def obtenerDatosFinales(dfFiltrado):
    depto = dfFiltrado["Departamento"].unique()[0]
    municipio = dfFiltrado["Municipio"].unique()[0]
    cultivo = dfFiltrado["Cultivo"].unique()[0]
    topologia = ", ".join(dfFiltrado["Topografia"].unique())
    medianaPH = f"{float(dfFiltrado['pH'].median()):.2f}"
    medianaFosforo = f"{float(dfFiltrado['Fosforo'].median()):.2f}"
    medianaPotasio = f"{float(dfFiltrado['Potasio'].median()):.2f}"

    arregloDatosFinales = [[depto, municipio, cultivo, topologia, medianaPH, medianaFosforo, medianaPotasio]]

    return arregloDatosFinales

def imprimirTabla(datosFiltrados):
    print(tabulate(obtenerDatosFinales(datosFiltrados), headers=["Departamento", "Municipio", "Cultivo", "Topología", "Mediana pH", "Mediana Fosforo","Mediana Potasio"], tablefmt="fancy_grid"))



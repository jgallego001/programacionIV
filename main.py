from ui import mostrar_tabla
from api import base_de_datos

def main():
    datosFiltrados = base_de_datos.retornarDatos()
    mostrar_tabla.imprimirTabla(datosFiltrados)

if __name__ == "__main__":
    main()
import networkx as nx
import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext

# Crear un grafo de conocimiento utilizando networkx
grafo_conocimiento = nx.DiGraph()

# Agregar nodos y relaciones al grafo de conocimiento
grafo_conocimiento.add_node("William Shakespeare", tipo="autor", periodo="Renacimiento")
grafo_conocimiento.add_node("Romeo y Julieta", tipo="obra", genero="Tragedia", año="1597",
                            resumen="Romeo y Julieta es una de las obras más conocidas de William Shakespeare. "
                                    "Es una tragedia que cuenta la historia de dos jóvenes amantes de familias "
                                    "rivales en Verona.")
grafo_conocimiento.add_edge("William Shakespeare", "Romeo y Julieta", relacion="escribió")
grafo_conocimiento.add_node("Hamlet", tipo="obra", genero="Tragedia", año="1600",
                            resumen="Hamlet es otra de las grandes tragedias de Shakespeare. La obra gira en torno "
                                    "al príncipe Hamlet y su búsqueda de venganza por la muerte de su padre.")
grafo_conocimiento.add_edge("William Shakespeare", "Hamlet", relacion="escribió")
grafo_conocimiento.add_node("Macbeth", tipo="obra", genero="Tragedia", año="1606",
                            resumen="Macbeth es una tragedia que explora la ambición y el poder. Sigue la historia "
                                    "de Macbeth, un noble escocés que comete asesinato para alcanzar el trono.")
grafo_conocimiento.add_edge("William Shakespeare", "Macbeth", relacion="escribió")
grafo_conocimiento.add_node("Otelo", tipo="obra", genero="Tragedia", año="1603",
                            resumen="Otelo es una tragedia que trata sobre los celos y la manipulación. Cuenta la "
                                    "historia del general Otelo y su esposa Desdémona.")
grafo_conocimiento.add_edge("William Shakespeare", "Otelo", relacion="escribió")
grafo_conocimiento.add_node("La Tempestad", tipo="obra", genero="Comedia", año="1611",
                            resumen="La Tempestad es una comedia que presenta temas de perdón y redención. Sigue "
                                    "la historia del mago Próspero y su hija Miranda, quienes naufragan en una isla "
                                    "desierta.")
grafo_conocimiento.add_edge("William Shakespeare", "La Tempestad", relacion="escribió")
grafo_conocimiento.add_node("Renacimiento", tipo="época histórica", duracion="Siglo XIV al Siglo XVII")
grafo_conocimiento.add_edge("William Shakespeare", "Renacimiento", relacion="vivió durante")

# Función para buscar información en el grafo de conocimiento
def buscar_informacion():
    entidad_busqueda = entrada.get()
    if entidad_busqueda in grafo_conocimiento.nodes:
        informacion = obtener_informacion(entidad_busqueda)
        if informacion:
            mostrar_resultado(f"Información sobre '{entidad_busqueda}':\n{informacion_str(informacion)}")
        else:
            mostrar_resultado(f"No se encontró información sobre '{entidad_busqueda}'.")
    else:
        mostrar_resultado(f"No se encontró la entidad '{entidad_busqueda}' en el grafo de conocimiento.")

# Función para obtener información del grafo
def obtener_informacion(entidad):
    informacion = {}
    if entidad in grafo_conocimiento.nodes:
        informacion["Tipo"] = grafo_conocimiento.nodes[entidad]["tipo"]
        informacion["Relaciones"] = list(grafo_conocimiento.in_edges(entidad, data=True))
        for atributo, valor in grafo_conocimiento.nodes[entidad].items():
            if atributo != "tipo":
                informacion[atributo.capitalize()] = valor
    return informacion

# Función para convertir información en cadena
def informacion_str(info):
    info_str = ""
    for clave, valor in info.items():
        if clave == "Resumen":
            info_str += f"{clave}: {valor}\n\n"  # Agregar un espacio antes del resumen
        else:
            info_str += f"{clave}: {valor}\n"
    info_str += "Relaciones:\n"
    for relacion in info["Relaciones"]:
        info_str += f"- {relacion[0]} {relacion[2]['relacion']} {relacion[1]}\n"
    return info_str

# Función para mostrar resultados en una ventana nueva
def mostrar_resultado(texto):
    ventana_resultado = tk.Toplevel()
    ventana_resultado.title("Resultado")
    ventana_resultado.geometry("800x600")  # Tamaño de la ventana de resultados

    # Crear un widget de texto desplazable para mostrar la información
    texto_resultado = scrolledtext.ScrolledText(ventana_resultado, wrap=tk.WORD, width=80, height=20)
    texto_resultado.insert(tk.INSERT, texto)
    texto_resultado.pack(padx=20, pady=20)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Consulta de Grafo de Conocimiento")

# Aumentar el tamaño de la ventana para ocupar la pantalla completa
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
ventana.geometry(f"{ancho_pantalla}x{alto_pantalla}")

# Crear etiqueta e input
etiqueta = tk.Label(ventana, text="Ingrese una consulta:", font=("Arial", 36))  # Cambiar fuente y tamaño del texto
etiqueta.pack(pady=40)
entrada = tk.Entry(ventana, font=("Arial", 28))  # Cambiar fuente y tamaño del texto
entrada.pack()

# Cambiar el color de fondo del botón y aumentar el tamaño de fuente
boton_buscar = tk.Button(ventana, text="Buscar", command=buscar_informacion, bg="green", fg="white",
                         font=("Arial", 28))
boton_buscar.pack(pady=40)

# Ejecutar la ventana
ventana.mainloop()

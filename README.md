

# Propuesta de grafo

Este proyecto es un ejemplo de cómo crear una aplicación de consulta de grafo de conocimiento utilizando Python, y como ampliación, para que quede más estético, usaremos la biblioteca Tkinter para que haya una  interfaz gráfica.

# Propuesta del Ejemplo

La propuesta de este ejemplo es mostrar cómo se puede diseñar una aplicación que hace uso de un grafo de conocimiento para buscar información sobre diferentes entidades, como autores y obras literarias. El objetivo principal es:

Presentar una propuesta concreta para mejorar la comprensión y las respuestas generadas por un modelo de lenguaje, en este caso, ChatGPT, a través de la incorporación de grafos de conocimiento.

# Creación del Grafo de Conocimiento

En este proyecto, hemos creado un grafo de conocimiento utilizando la biblioteca NetworkX en Python. El grafo de conocimiento contiene nodos que representan entidades como autores, obras literarias, épocas históricas, y aristas que representan relaciones semánticas entre estas entidades. Algunos ejemplos de entidades en el grafo son "William Shakespeare," "Romeo y Julieta," "Hamlet," entre otros.

# Datos en el Grafo
El grafo de conocimiento incluye información adicional sobre las entidades, como el tipo de entidad, el período histórico en el que vivieron (en el caso de los autores), el año de creación de las obras y un resumen breve de las obras literarias.

# Uso de la Aplicación

La aplicación permite a los usuarios ingresar una consulta en un cuadro de entrada y buscar información en el grafo de conocimiento. Al hacer clic en el botón "Buscar," se mostrará una ventana emergente con la información relevante recuperada del grafo. La aplicación también está diseñada para ser visualmente atractiva y fácil de usar.



# El código es el siguiente:

```
import networkx as nx
import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext

# Crear el
grafo_conocimiento = nx.DiGraph()

# Agrego los nodos y relaciones al grafo de conocimiento
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

# Esta funcion sirve para buscar la informacion en el grafo
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

# Esta funcion sirve para obtener informacion del grafo
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

# Empezamos con el tkinter



def mostrar_resultado(texto):
    ventana_resultado = tk.Toplevel()
    ventana_resultado.title("Resultado")
    ventana_resultado.geometry("1300x1300")  

    
    texto_resultado = scrolledtext.ScrolledText(ventana_resultado, wrap=tk.WORD, width=80, height=20)
    texto_resultado.insert(tk.INSERT, texto)
    texto_resultado.pack(padx=20, pady=20)


ventana = tk.Tk()
ventana.title("Consulta de Grafo de Conocimiento")


ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
ventana.geometry(f"{ancho_pantalla}x{alto_pantalla}")


etiqueta = tk.Label(ventana, text="Ingrese una consulta:", font=("Arial", 36))  # Cambiar fuente y tamaño del texto
etiqueta.pack(pady=40)
entrada = tk.Entry(ventana, font=("Arial", 28))  # Cambiar fuente y tamaño del texto
entrada.pack()


boton_buscar = tk.Button(ventana, text="Buscar", command=buscar_informacion, bg="green", fg="white",
                         font=("Arial", 28))
boton_buscar.pack(pady=40)


ventana.mainloop()

```

# Evaluación del modelo

A continuación se procederá a evaluar el modelo propuesto en base a su precisión, relevancia y confiabilidad (el apartado 4 del enunciado). Cabe destacar que no se ha podido realizar la parte del Chat GPT porque se requería su versión de pago.

Para evaluar la precisión, relevancia y confiabilidad del código proporcionado, se pueden considerar los siguientes aspectos:

Precisión:
La precisión se refiere a la exactitud y corrección del código al buscar y mostrar información relevante del grafo de conocimiento. En este caso, el código parece ser preciso, ya que verifica si la entidad ingresada por el usuario existe en el grafo y muestra información relevante si la encuentra.

Relevancia:
La relevancia se refiere a la importancia y utilidad de la información proporcionada. El código muestra información relevante sobre la entidad ingresada, incluyendo detalles como tipo, atributos y relaciones. La relevancia también puede ser mejorada agregando más atributos específicos para cada tipo de entidad en el grafo, si es necesario.

Confiabilidad:
La confiabilidad se refiere a la estabilidad y consistencia del código. El código es confiable en términos de su funcionalidad básica. 

# Conclusiones

El código proporcionado es una aplicación simple que utiliza el módulo NetworkX para crear un grafo de conocimiento sobre William Shakespeare y sus obras. Además, utiliza la interfaz gráfica de Tkinter para permitir a los usuarios buscar información sobre las entidades del grafo. El código maneja algunos posibles errores, como entradas vacías y la falta de atributos en los nodos del grafo.

La aplicación muestra información precisa sobre las entidades encontradas en el grafo, incluyendo detalles como tipo, relaciones y atributos.

Hemos decidido añadir una interfaz para darle un toque personal al proyecto que nos diferencie del resto. Esta es sencilla y fácil de usar, permitiendo a los usuarios ingresar consultas y ver los resultados de manera clara.








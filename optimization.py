from tkinter import *
from tkinter import ttk
from modules.module import optimizeDistance

# Declaracion de la ventana princial
window = Tk()
window.title('Optimizacion')
window.geometry('800x600')
window.columnconfigure(0, weight=1)

# Declaracion del frame principal de la vista
frm = Frame(window, padx=20, pady=20, background='#353b48',)
frm.columnconfigure(0, weight=1)
frm.rowconfigure(0, weight=1)
frm.grid(sticky="nsew")
frm.pack(fill='both', expand=True, side='top')

# Declaracion de los distintos frames de cada vista
frm1: Frame
frm2: Frame
frm3: Frame
frm4: Frame
frm5: Frame

pointsQuantity: int # Cantidad de puntos
points: list = [] # Puntos
pointActual: int = 0 # Punto actual
pointX: int = 0 # Punto X
pointY: int = 0 # Punto Y
point: tuple

# Creacion de estilos para los botones
styles = ttk.Style()
styles.configure(
    "MyButton.TButton",
    foreground="#353b48",
    padding=10,
    font=('', 14),
    cursor='pointer'
)

""" 
    Funcion que pasa de una vista a otra y guarda la informacion suministrada
    num = entero que indica que vista se mostrara
    data = data necesaria para la siguiente vista
"""


def destroyFrm(num, data):
    global points, pointsQuantity, pointActual, pointX, pointY
    # Si el Frame es el numero 1, se guarda la cantidad de puntos a ingresar
    if num == 1:
        frm1.destroy()
        pointsQuantity = data
        pointActual += 1
        view_two()  # Se muestra la vista numero 2

    # Si el Frame es el numero 2, se guarda la coordenada (x,y) ingresada y/o se envia a la vista 3
    elif num == 2:
        frm2.destroy()
        points.append(data)
        if int(pointActual) == int(pointsQuantity): 
            result = optimizeDistance(points)
            view_three(result)
        else: 
            pointActual += 1
            view_two()


    # Si el Frame es el numero 3, se destruye y se reinicia las vistas
    elif num == 3:
        frm3.destroy()
        points.clear()
        pointsQuantity = 0
        pointActual = 0
        pointX = 0
        pointY = 0
        view_one()

""" 
    Funcion para reiniciar el proceso en caso de haber alguna equivocacion 
"""


""" 
    Funcion que muestra la primera vista y guarda el modo si sera codificacion o decodificacion
"""


def view_one():
    global frm1

    # Se maqueta la primera vista
    frm1 = Frame(frm, padx=10, pady=10, )
    frm1.columnconfigure(0, weight=1)
    frm1.columnconfigure(1, weight=1)
    frm1.rowconfigure(0, weight=1)
    frm1.rowconfigure(1, weight=1)
    frm1.grid(sticky="nsew")

    # Label para mostrar un mensaje
    ttk.Label(frm1, text="¿Cuantos puntos quieres ingresar?", font=('', 18)).grid(
        column=0, columnspan=2, row=0,)
    # Input para recibir la cantidad de puntos
    entry = ttk.Entry(frm1, width=40, font=('', 14),)
    entry.grid(
        column=0, row=1, ipadx=5, ipady=5)
    # Boton para continuar
    ttk.Button(frm1, text="Enter", style="MyButton.TButton",
               command=lambda: destroyFrm(1, entry.get())).grid(column=1, row=1)

""" 
    Funcion que muestra la segunda vista y guarda la cadena binaria a utilizar
"""


def view_two():
    global frm2

    # Se maqueta la segunda vista
    frm2 = Frame(frm, padx=10, pady=10)
    frm2.columnconfigure(0, weight=1)
    frm2.columnconfigure(1, weight=1)
    frm2.rowconfigure(0, weight=1)
    frm2.rowconfigure(1, weight=1)
    frm2.columnconfigure(2, weight=1)
    frm2.rowconfigure(2, weight=1)
    frm2.grid(sticky="nsew")

    # Label para mostrar un mensaje
    ttk.Label(frm2, text="Valor de X:", font=('', 18)).grid(
        column=0, row=0)
    # Input para recibir la cadena de bits
    entryX = ttk.Entry(frm2, width=40, font=('', 14),)
    entryX.grid(
        column=1, row=0, ipadx=5, ipady=5)
    # Label para mostrar un mensaje
    ttk.Label(frm2, text="Valor de Y", font=('', 18)).grid(
        column=0, row=1)
    entryY = ttk.Entry(frm2, width=40, font=('', 14),)
    entryY.grid(
        column=1, row=1, ipadx=5, ipady=5)

    # Boton para continuar
    ttk.Button(frm2, text="Enter", style="MyButton.TButton",
               command=lambda: destroyFrm(2, (int(entryX.get()), int(entryY.get())))).grid(column=1, row=2)


""" 
    Funcion que muestra la tercera vista y se pregunta el metodo a utilizar Hamming o CRC
"""


def view_three(result):
    global frm3

    # Se maqueta la tercera vista
    frm3 = Frame(frm, padx=10, pady=10)
    frm3.columnconfigure(0, weight=1)
    frm3.columnconfigure(1, weight=1)
    frm3.rowconfigure(0, weight=1)
    frm3.rowconfigure(1, weight=1)
    frm3.columnconfigure(2, weight=1)
    frm3.rowconfigure(2, weight=1)
    frm3.grid(sticky="nsew")

    newPointWithDistance = result[0]
    distancePointZero = result[1]
    newPoint = newPointWithDistance[0]
    newDistance= newPointWithDistance[1]
    
    # Label para mostrar un mensaje
    ttk.Label(frm3, text="Distancia con el punto en (0,0):", font=('', 18)).grid(
        column=0, row=0)
    ttk.Label(frm3, text=distancePointZero, font=('', 18)).grid(
    column=1, row=0)
    # Label para mostrar un mensaje
    text = "Distancia con el nuevo punto en (" + str(newPoint[0]) + ',' + str(newPoint[1]) + "):"
    ttk.Label(frm3, text=text, font=('', 18)).grid(
        column=0, row=1)
    ttk.Label(frm3, text=newDistance, font=('', 18)).grid(
    column=1, row=1)
    # Boton para regresar a la primera vista
    # Boton para continuar
    ttk.Button(frm3, text="Regresar", style="MyButton.TButton",
               command=lambda: destroyFrm(3, NONE)).grid(column=1, row=2)


# Se llama a la primera funcion que muestra la primera vista
view_one()

# Servicio que mantiene actualizada la vista
window.mainloop()

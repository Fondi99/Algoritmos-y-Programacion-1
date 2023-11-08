import tkinter

ventana = tkinter.Tk()
ventana.geometry("1200x800")

etiqueta = tkinter.Label(ventana, text="Hola Mundo", bg="yellow")
etiqueta.pack(fill=tkinter.BOTH)

boton = tkinter.Button(ventana, text="Presiona")
boton.pack()

ventana.mainloop()
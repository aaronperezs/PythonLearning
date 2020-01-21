from Tkinter import *

root=Tk()

miFrame=Frame(root, width=500, height=400)

miFrame.pack()

#Label(miFrame, text="Hola soy una etiqueta", fg="blue", font=("Noto sans", 18)).place(x=50,y=200)

Label(miFrame, image="face.png").place(x=50,y=200)

miBoton=Button(miFrame, text="Hola soy un boton")
miBoton.place(x=300,y=200)

root.mainloop()
import tkinter


def parabola(x):
    y = x * x
    return y


mainWindow = tkinter.Tk()

mainWindow.title("Parabola")
mainWindow.geometry("640x480")
canvas = tkinter.Canvas(mainWindow, width=1200, height=980)
canvas.grid(row=0, column=0)


for x in range(-100, 100):
    y = parabola(x)
    print(y)

mainWindow.mainloop()
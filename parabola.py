import tkinter
import math


def parabola(page, size):
    for x in range(size):
        y = x * x / size
        plot(page, x, y)
        plot(page, -x, y)


def circle(page, radius, g, h):
    page.create_oval(g + radius, h + radius, g - radius, h - radius, outline="red", width=2)
    # for x in range(g * 50, (g + radius) * 50):
    #     x /= 50
    #     print(x)
    #     y = h + (math.sqrt(radius ** 2 - ((x - g) ** 2)))
    #     plot(page, x, y)
    #     plot(page, x, 2 * h - y)
    #     plot(page, 2 * g - x, y)
    #     plot(page, 2 * g - x, 2 * h - y)


def draw_axes(page):
    page.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill="white")
    page.create_line(0, y_origin, 0, -y_origin, fill="white")
    print(locals())


def plot(page, x, y):
    page.create_line(x, -y, x + 1, -y + 1, fill="red")


mainWindow = tkinter.Tk()

mainWindow.title("Parabola")
mainWindow.geometry("640x480")
canvas = tkinter.Canvas(mainWindow, width=640, height=480, background="black")
canvas.grid(row=0, column=0)

# canvas2 = tkinter.Canvas(mainWindow, width=640, height=480, background="pink")
# canvas2.grid(row=0, column=1)

# print(repr(canvas), repr(canvas2))
draw_axes(canvas)
# draw_axes(canvas2)

parabola(canvas, 100)
parabola(canvas, 200)

circle(canvas, 100, 100, 100)
circle(canvas, 100, 100, -100)
circle(canvas, 100, -100, 100)
circle(canvas, 100, -100, -100)

circle(canvas, 10, 30, 30)
circle(canvas, 10, 30, -30)
circle(canvas, 10, -30, 30)
circle(canvas, 10, -30, -30)
circle(canvas, 30, 0, 0)

circle(canvas, -56, -50, -34)
circle(canvas, 90, -90, 74)


mainWindow.mainloop()

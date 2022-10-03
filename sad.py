# импортируем tkinter
import tkinter
# создаем окно
window = tkinter.Tk()
# создаем холст и размещаем его в окне
canvas = tkinter.Canvas(window)
canvas.pack()

# координаты левого верхнего
# угла прямоугольника, в который должен быть вписан круг
x0 = 50
y0 = 50

# координаты правого нижнего
# угла прямоугольника
x1 = 150
y1 = 150

canvas.create_oval(x0, y0, x1, y1)
window.mainloop()
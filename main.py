from tkinter import *
from tkinter import messagebox

windows = Tk()
windows.title('Калькулятор индекса массы тела (ИМТ)')
windows.geometry(f'400x300+{windows.winfo_screenwidth() // 2 - 200}+{windows.winfo_screenheight() // 2 - 150}')

frame = LabelFrame(
    windows,
    padx=10,
    pady=10
)
frame.pack(expand=True)

height_lb = Label(
    frame,
    text="Введите свой рост (в см)  "
)
height_lb.grid(row=3, column=1)

weight_lb = Label(
    frame,
    text="Введите свой вес (в кг)  ",
)
weight_lb.grid(row=4, column=1)

height_tf = Entry(
    frame,
)
height_tf.grid(row=3, column=2)

weight_tf = Entry(
    frame,
)
weight_tf.grid(row=4, column=2, pady=5)


def calculate_bmi():
    kg = int(weight_tf.get())
    m = int(height_tf.get()) / 100
    bmi = kg / (m * m)
    bmi = round(bmi, 1)

    if bmi <= 18.5:
        messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует недостаточному весу')
    elif (bmi > 18.5) and (bmi <= 24.9):
        messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует нормальному весу')
    elif (bmi > 24.9) and (bmi <= 29.9):
        messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует избыточному весу')
    else:
        messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует ожирению')


cal_btn = Button(
    frame,
    text='Рассчитать ИМТ',
    command=calculate_bmi
)
cal_btn.grid(row=5, column=2)

windows.mainloop()

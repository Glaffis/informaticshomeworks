from tkinter import *
from tkinter import ttk
def calculate(*args):
    try:
        value = feet.get()
        allowed_chars = "0123456789+-*/%(). "
        if not value:
            meters.set("")
            return
        if not all(ch in allowed_chars for ch in value):
            meters.set("Ошибка")
            return
        result = eval(value, {"__builtins__": {}}, {})
        meters.set(str(result))
    except Exception as e:
        meters.set(f"Ошибка: {e}")

root = Tk()
root.title("Калькулятор")

mainframe = ttk.Frame(root, padding="10 10 10 10")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
feet = StringVar()   
meters = StringVar() 

ttk.Label(mainframe, text="Выражение:").grid(column=1, row=1, sticky=W)
entry = ttk.Entry(mainframe, width=40, textvariable=feet)
entry.grid(column=2, row=1, sticky=(W, E))

ttk.Button(mainframe, text="Рассчитать", command=calculate).grid(column=2, row=2, sticky=W)

ttk.Label(mainframe, text="Результат:").grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=3, sticky=(W, E))

root.bind("<Return>", calculate)

entry.focus()
root.mainloop()

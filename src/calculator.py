from enum import Enum
from tkinter import *

c = 0

current_operator = ""

root = Tk()
root.title("Simple calculator")

e = Entry(root, width=40)
e.grid(row=0, column=0, columnspan=3, rowspan=1)


def compute():
    global current_operator
    string = e.get()
    print("Current operator: " + current_operator)
    operator_index = string.index(current_operator)
    print(operator_index)
    a = float(string[0:operator_index])
    b = float(string[operator_index + 1:])
    if current_operator == "+":
        print("Add branch")
        return a + b
    elif current_operator == "-":
        print("Sub branch")
        return a - b
    elif current_operator == "*":
        return a * b
    else:
        return a / b


def test():
    c += 1
    print(c)


def on_click(number):
    e.delete(0, END)
    e.insert(0, number)


def set_text(text):
    e.delete(0, END)
    e.insert(0, text)


def on_click(entry):
    global current_operator
    if entry == "=":
        set_text(compute())
        current_operator = ""
    else:
        if current_operator == "" and entry == "+" or entry == "-" or entry == "*" or entry == "/":
            current_operator = entry
        a = str(e.get())
        set_text(a + str(entry))
    global c
    c += 1


button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: on_click(0))
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: on_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: on_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: on_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: on_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: on_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: on_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: on_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: on_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: on_click(9))

button_equals = Button(root, text="=", padx=80, pady=60, command=lambda: on_click("="))
button_add = Button(root, text="+", padx=40, pady=20, command=lambda: on_click("+"))
button_sub = Button(root, text="-", padx=40, pady=20, command=lambda: on_click("-"))
button_mul = Button(root, text="*", padx=40, pady=20, command=lambda: on_click("*"))
button_div = Button(root, text="/", padx=40, pady=20, command=lambda: on_click("/"))

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_equals.grid(row=4, column=1, columnspan=2, rowspan=2)
button_add.grid(row=5, column=0)

button_sub.grid(row=6, column=0)
button_mul.grid(row=6, column=1)
button_div.grid(row=6, column=2)


# button.pack()
# greeting.pack()

def main():
    c = 0
    root.mainloop()


main()

from tkinter import *

calculator_window = Tk()
calculator_window.geometry("312x324")
calculator_window.resizable(0, 0)
calculator_window.title("My Calculator")

def button_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def button_clear():
    global expression
    expression = ""
    input_text.set("")

def button_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""

expression = ""

input_text = StringVar()

input_frame = Frame(calculator_window, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#a6a6a6", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

buttons_frame = Frame(calculator_window, width=312, height=272.5, bg="#4d4d4d")
buttons_frame.pack()

clear_button = Button(buttons_frame, text="C", fg="white", width=32, height=3, bd=0, bg="#808080", cursor="hand2", command=lambda: button_clear())
clear_button.grid(row=0, column=0, columnspan=3, padx=1, pady=1)

divide_button = Button(buttons_frame, text="/", fg="white", width=10, height=3, bd=0, bg="#808080", cursor="hand2", command=lambda: button_click("/"))
divide_button.grid(row=0, column=3, padx=1, pady=1)

seven_button = Button(buttons_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#666666", cursor="hand2", command=lambda: button_click(7))
seven_button.grid(row=1, column=0, padx=1, pady=1)

eight_button = Button(buttons_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#666666", cursor="hand2", command=lambda: button_click(8))
eight_button.grid(row=1, column=1, padx=1, pady=1)

nine_button = Button(buttons_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#666666", cursor="hand2", command=lambda: button_click(9))
nine_button.grid(row=1, column=2, padx=1, pady=1)

multiply_button = Button(buttons_frame, text="*", fg="white", width=10, height=3, bd=0, bg="#808080", cursor="hand2", command=lambda: button_click("*"))
multiply_button.grid(row=1, column=3, padx=1, pady=1)

four_button = Button(buttons_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#666666", cursor="hand2", command=lambda: button_click(4))
four_button.grid(row=2, column=0, padx=1, pady=1)

five_button = Button(buttons_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#666666", cursor="hand2", command=lambda: button_click(5))
five_button.grid(row=2, column=1, padx=1, pady=1)

six_button = Button(buttons_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#666666", cursor="hand2", command=lambda: button_click(6))
six_button.grid(row=2, column=2, padx=1, pady=1)

minus_button = Button(buttons_frame, text="-", fg="white", width=10, height=3, bd=0, bg="#808080", cursor="hand2", command=lambda: button_click("-"))
minus_button.grid(row=2, column=3, padx=1, pady=1)

one_button = Button(buttons_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#666666", cursor="hand2", command=lambda: button_click(1))
one_button.grid(row=3, column=0, padx=1, pady=1)

two_button = Button(buttons_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#666666", cursor="hand2", command=lambda: button_click(2))
two_button.grid(row=3, column=1, padx=1, pady=1)

three_button = Button(buttons_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#666666", cursor="hand2", command=lambda: button_click(3))
three_button.grid(row=3, column=2, padx=1, pady=1)

plus_button = Button(buttons_frame, text="+", fg="white", width=10, height=3, bd=0, bg="#808080", cursor="hand2", command=lambda: button_click("+"))
plus_button.grid(row=3, column=3, padx=1, pady=1)

zero_button = Button(buttons_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#666666", cursor="hand2", command=lambda: button_click(0))
zero_button.grid(row=4, column=0, columnspan=2, padx=1, pady=1)

point_button = Button(buttons_frame, text=".", fg="white", width=10, height=3, bd=0, bg="#808080", cursor="hand2", command=lambda: button_click("."))
point_button.grid(row=4, column=2, padx=1, pady=1)

equals_button = Button(buttons_frame, text="=", fg="white", width=10, height=3, bd=0, bg="#808080", cursor="hand2", command=lambda: button_equal())
equals_button.grid(row=4, column=3, padx=1, pady=1)

calculator_window.mainloop()

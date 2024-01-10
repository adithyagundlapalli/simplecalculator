import tkinter as tk

expression = ""


def buttonClick(item):
  global expression
  expression += str(item)
  textResult.delete(1.0, "end")
  textResult.insert(1.0, expression)

def mili():
  textResult.insert(1.0, "128√e980")

def sqrt():
  global expression
  expression = sqrt(expression)
  textResult.delete(1.0, "end")
  textResult.insert(1.0, expression)
   


def btnEqual():
  global expression
  
  try:
    expression = str(eval(expression))
    textResult.delete(1.0, "end")
    textResult.insert(1.0, expression)

  except:
    buttonClear()
    textResult.insert(1.0, "Error")


def buttonClear():
  global expression
  expression = ""
  textResult.delete(1.0, "end")


root = tk.Tk()
root.geometry("300x200")
root.configure(background='black')

root.title("Simple Calculator")

textResult = tk.Text(root, height=1, width=16, font=("Arial", 20))
textResult.grid(columnspan=5)


button1 = tk.Button(root,
                    text="1",
                    command=lambda: buttonClick(1),
                    width=5,
                    font=("Arial", 14))
button1.grid(row=2, column=1)

button2 = tk.Button(root,
                    text="2",
                    command=lambda: buttonClick(2),
                    width=5,
                    font=("Arial", 14))
button2.grid(row=2, column=2)

button3 = tk.Button(root,
                    text="3",
                    command=lambda: buttonClick(3),
                    width=5,
                    font=("Arial", 14))
button3.grid(row=2, column=3)

button4 = tk.Button(root,
                    text="4",
                    command=lambda: buttonClick(4),
                    width=5,
                    font=("Arial", 14))
button4.grid(row=3, column=1)

button5 = tk.Button(root,
                    text="5",
                    command=lambda: buttonClick(5),
                    width=5,
                    font=("Arial", 14))
button5.grid(row=3, column=2)

button6 = tk.Button(root,
                    text="6",
                    command=lambda: buttonClick(6),
                    width=5,
                    font=("Arial", 14))
button6.grid(row=3, column=3)

button7 = tk.Button(root,
                    text="7",
                    command=lambda: buttonClick(7),
                    width=5,
                    font=("Arial", 14))
button7.grid(row=4, column=1)

button8 = tk.Button(root,
                    text="8",
                    command=lambda: buttonClick(8),
                    width=5,
                    font=("Arial", 14))
button8.grid(row=4, column=2)

button9 = tk.Button(root,
                    text="9",
                    command=lambda: buttonClick(9),
                    width=5,
                    font=("Arial", 14))
button9.grid(row=4, column=3)

button0 = tk.Button(root,
                    text="0",
                    command=lambda: buttonClick(0),
                    width=5,
                    font=("Arial", 14))
button0.grid(row=5, column=2)

buttonplus = tk.Button(root,
                    text="+",
                    command=lambda: buttonClick("+"),
                    width=5,
                    font=("Arial", 14), bg='orange')
buttonplus.grid(row=2, column=4)

buttonminus = tk.Button(root,
                    text="-",
                    command=lambda: buttonClick("-"),
                    width=5,
                    font=("Arial", 14), bg='orange')
buttonminus.grid(row=3, column=4)

buttonmultiply = tk.Button(root,
                    text="x",
                    command=lambda: buttonClick("*"),
                    width=5,
                    font=("Arial", 14), bg='orange')
buttonmultiply.grid(row=4, column=4)

buttondivide = tk.Button(root,
                    text="÷",
                    command=lambda: buttonClick("/"),
                    width=5,
                    font=("Arial", 14), bg='orange')
buttondivide.grid(row=5, column=4)

buttonpow = tk.Button(root,
                    text="^",
                    command=lambda: buttonClick("**"),
                    width=5,
                    font=("Arial", 14))
buttonpow.grid(row=6, column=1)

buttondot = tk.Button(root,
                    text=".",
                    command=lambda: buttonClick("."),
                    width=5,
                    font=("Arial", 14))
buttondot.grid(row=6, column=2)

buttonclose = tk.Button(root,
                    text=")",
                    command=lambda: buttonClick(")"),
                    width=5,
                    font=("Arial", 14))
buttonclose.grid(row=5, column=3)

buttonopen = tk.Button(root,
                    text="(",
                    command=lambda: buttonClick("("),
                    width=5,
                    font=("Arial", 14))
buttonopen.grid(row=5, column=1)

'''
buttonsqrt = tk.Button(root,
                    text="√x",
                    command=lambda: sqrt,
                    width=5,
                    font=("Arial", 14))
buttonsqrt.grid(row=7, column=2)'''

buttonequals = tk.Button(root,
                    text="=",
                    command=btnEqual,
                    width=5,
                    font=("Arial", 14))
buttonequals.grid(row=6, column=4)

buttonclear = tk.Button(root,
                    text="Clear",
                    command=lambda: buttonClear(),
                    width=5,
                    font=("Arial", 14),bg='orange')
buttonclear.grid(row=6, column=3)

buttonmili = tk.Button(root,
                    text="MILI♡",
                    command=lambda: mili(),
                    width=5,
                    font=("Arial", 14),bg='orange')
buttonmili.grid(row=7, column=1)

root.mainloop()

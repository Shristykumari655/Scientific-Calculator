import tkinter as tk
import math
#Create Calculator window
window = tk.Tk()

#Window title
window.title("My Calculator")

#Window size
window.geometry("400x600")
window.configure(bg="black")

#Calculator display
display = tk.Entry(window, font = ("Arial",28), justify="right", bg="black", fg="white", insertbackground="white")
display.grid(row = 0, column=0, columnspan=4,padx =10, pady =20,)

def backspace():
     current = display.get()
     display.delete(0, tk.END)
     display.insert(0, current[:-1])

button_backspace = tk.Button(window, text ="⌫", width ="5", height ="2", command=backspace)
button_backspace.grid(row= 1, column= 1, padx=5, pady=5)

def percentage():
     try:
          value = float(display.get())
          result = value/100
          display.delete(0, tk.END)
          display.insert(0, str(result))
     except:
          display.delete(0, tk.END)
          display.insert(0, "Error")

button_percentage = tk.Button(window, text="%", width= "5", height="2", bg="#666666", fg="white", command=percentage)
button_percentage.grid(row=1, column=2, padx=5, pady=5)

def plus_minus():
     try:
          value = float(display.get())
          value = -value
          display.delete(0, tk.END)
          display.insert(0, str(value))
     except:
          display.delete(0, tk.END)
          display.insert(0, "Error")

button_plus_minus= tk.Button(window, text="+/-", width="5", height="2",bg ="#666666", fg= "white", command=plus_minus)
button_plus_minus.grid(row=5,column=0, padx=5, pady=5)

def square_root():
     try:
          value = float(display.get())
          result = math.sqrt(value)
          display.delete(0, tk.END)
          display.insert(0, str(result))
     except ValueError:
          display.delete(0, tk.END)
          display.insert(0, "Error")

button_square_root = tk.Button(window, text="v", width="5", height="2",bg="#666666", fg="white", command=square_root)
button_square_root.grid(row= 6, column=0, padx =5, pady= 5)

def square():
     try:
          value = float(display.get())
          result = value**2
          display.delete(0, tk.END)
          display.insert(0, str(result))
     except:
          display.delete(0, tk.END)
          display.insert(0, "Error")

button_square = tk.Button(window, text="x²", width="5", height="2", bg ="#666666", fg="white", command=square)
button_square.grid(row=6, column=1, padx=5, pady=5)


def button_click(value):
    display.insert(tk.END, value)

def operator_click(operator):
    display.insert(tk.END, operator)

def calculate():
        expression = display.get()

        try:
            result = eval(expression)
            display.delete(0, tk.END)
            display.insert(0, result)
        except ZeroDivisionError:
             display.delete(0, tk.END)
             display.insert(0, "Cannot divide by 0")
        except:
            display.delete(0,tk.END)
            display.insert(0, "Error")
def clear_display():
     display.delete(0, tk.END)

     def keyboard_input(event):
          key = event.char
          if key in"0123456789.+-*/":
               display.insert(tk.END , key)
          elif event.keysym == "Return":
               calculate()
          elif event.keysym == "Backspace":
               backspace()
          elif event.keysym == "Escape":
               clear_display()
               window.bind("<Key>", keyboard_input)

                 
    
#Calculator buttons

button_decimal = tk.Button(window, text =".", width ="5", height="2", bg ="#333333", fg ="white", command= lambda:button_click("."))
button_decimal.grid( row=5, column=2, padx=5, pady=5)


button_7 = tk.Button(window, text ="7",width ="5", height ="2", bg= "#333333", fg= "white", command=lambda: button_click("7"))
button_7.grid(row = 2, column = 0, padx= 5, pady=5)


button_8 = tk.Button(window , text ="8",width ="5", height ="2",bg="#333333", fg="white" ,command =lambda: button_click("8"))
button_8.grid(row= 2, column =1, padx =5, pady = 5)


button_9 = tk.Button(window, text="9", width="5", height="2",bg= "#333333", fg="white", command=lambda: button_click("9"))
button_9.grid (row=2, column =2, padx =5, pady=5)

button_4 = tk.Button(window, text ="4", width ="5", height="2", bg= "#333333", fg="white", command=lambda: button_click("4"))
button_4.grid(row=3, column =0, padx=5 ,pady=5)

button_5 = tk.Button(window, text ="5", width ="5", height="2", bg ="#333333", fg= "white", command=lambda: button_click("5"))
button_5.grid(row =3, column =1, padx=5, pady=5)

button_6 = tk.Button(window, text ="6", width="5", height="2", bg="#333333", fg="white", command=lambda: button_click("6"))
button_6.grid(row= 3, column =2, padx=5, pady=5)

button_1 = tk.Button(window, text ="1", width = "5", height="2",bg ="#333333",fg ="white" ,command=lambda: button_click("1"))
button_1.grid(row = 4, column =0, padx=5, pady= 5)

button_2 = tk.Button(window, text ="2", width= "5", height ="2",bg ="#333333", fg="white", command=lambda: button_click("2"))
button_2.grid(row = 4, column = 1, padx= 5, pady =5)

button_3 = tk.Button(window, text ="3", width = "5", height="2", bg ="#333333", fg="white",command=lambda: button_click("3"))
button_3.grid(row = 4, column = 2, padx= 5, pady =5)

button_0 = tk.Button(window, text="0", width = "5", height= "2", bg ="#333333", fg="white",command=lambda: button_click("03"))
button_0.grid(row = 5, column =1, padx= 5, pady =5)

button_add = tk.Button(window, text ="+", width ="5", height="2", bg="#ff9500", fg="white", command=lambda: operator_click("+"))
button_add.grid(row = 4, column = 3, padx=5, pady=5)

button_subtract = tk.Button(window, text ="-", width ="5", height ="2",bg="#ff9500", fg="white", command=lambda: operator_click("-"))
button_subtract.grid(row = 3, column = 3, padx=5, pady=5)

button_mul = tk.Button(window, text ="*", width ="5", height ="2",bg ="#ff9500", fg ="white", command=lambda: operator_click("*"))
button_mul.grid(row = 2, column = 3, padx=5, pady=5)

button_div = tk.Button(window, text="/", width ="5", height ="2",bg="#ff9500", fg ="white", command=lambda: operator_click("/"))
button_div.grid(row = 1, column = 3, padx=5, pady=5)

button_clear = tk.Button(window, text = "C", width ="5", height ="2",bg ="#666666", fg="white", command=clear_display)
button_clear.grid(row = 1, column = 0, padx = 5, pady =5)

button_equal = tk.Button(window, text = "=", width = "5", height ="2",bg="#ff9500", fg ="white", command=calculate)
button_equal.grid(row = 5, column = 3, padx=5, pady=5)


#Run the window
window.mainloop()
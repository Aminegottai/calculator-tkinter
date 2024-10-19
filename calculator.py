import tkinter as tk
from tkinter import ttk
def add(x,y):
    return x+y 
def sous(x,y):
    return x-y 
def mult(x,y):
    return x*y 
def div(x,y):
    if y!=0:
        return x/y
    else :
        t_box.insert(0,'erreur')
def supp():
    t_box.delete("1.0",tk.END)


def validate_input(): 
    user_input = t_box.get("1.0", tk.END).strip()  
    for i in user_input:
        if i not in "0123456789+-*/.() ":
            t_box.delete("1.0", tk.END) 
def click(value):
    t_box.insert(tk.END, value)
def calculate():
    try:
        expression = t_box.get("1.0", tk.END).strip()  
        result = eval(expression)  
        t_box.delete("1.0", tk.END)  
        t_box.insert(tk.END, result)  
    except Exception as e:
        t_box.delete(0, tk.END) 
        t_box.insert(tk.END, 'erreur') 

window = tk.Tk()
window.configure(bg='black') 
window.title("Calculatrice")
window.geometry("315x480")
window.resizable(False, False) 

t_box = tk.Text(window, height=7, width=30, font=("Arial", 18),fg='white',background='black',relief="solid")  
t_box.grid(row=0, column=0, columnspan=4, padx=0, pady=10)


for i in range(4):
    window.grid_columnconfigure(i, weight=1)

bt_1 = tk.Button(window, text="AC", font=("Arial", 14), bg="#56739A", fg="white",command=supp)
bt_1.grid(row=1, column=0, padx=1, pady=1, sticky="nsew")  

bt_2 = tk.Button(window, text="+/-", font=("Arial", 14), bg="#56739A", fg="white",command=click('+/-'))
bt_2.grid(row=1, column=1, padx=1, pady=1, sticky="nsew")  

bt_3 = tk.Button(window, text='%', font=("Arial", 14), bg="#56739A", fg="white",command=click('%'))
bt_3.grid(row=1, column=2, padx=1, pady=1, sticky="nsew")  

bt_4 = tk.Button(window, text="/", font=("Arial", 14), bg="#ED7F10", fg="white",command=click('/'))
bt_4.grid(row=1, column=3, padx=1, pady=1, sticky="nsew")  

bt_5 = tk.Button(window, text="7", font=("Arial", 14), bg="#56739A", fg="white", command=lambda: click('7'))
bt_5.grid(row=2, column=0, padx=1, pady=10, sticky="nsew")  

bt_6 = tk.Button(window, text="8", font=("Arial", 14), bg="#56739A", fg="white", command=lambda: click('8'))
bt_6.grid(row=2, column=1, padx=1, pady=10, sticky="nsew")  

bt_7 = tk.Button(window, text="9", font=("Arial", 14), bg="#56739A", fg="white", command=lambda: click('9'))
bt_7.grid(row=2, column=2, padx=1, pady=10, sticky="nsew")  

bt_8 = tk.Button(window, text="*", font=("Arial", 14), bg="#ED7F10", fg="white", command=lambda: click('*'))
bt_8.grid(row=2, column=3, padx=1, pady=10, sticky="nsew")  

bt_9 = tk.Button(window, text="4", font=("Arial", 14), bg="#56739A", fg="white", command=lambda: click('4'))
bt_9.grid(row=3, column=0, padx=1, pady=10, sticky="nsew")  

bt_10 = tk.Button(window, text="5", font=("Arial", 14), bg="#56739A", fg="white", command=lambda: click('5'))
bt_10.grid(row=3, column=1, padx=1, pady=10, sticky="nsew")  

bt_11 = tk.Button(window, text="6", font=("Arial", 14), bg="#56739A", fg="white", command=lambda: click('6'))
bt_11.grid(row=3, column=2, padx=1, pady=10, sticky="nsew")  

bt_12 = tk.Button(window, text="-", font=("Arial", 14), bg="#ED7F10", fg="white", command=lambda: click('-'))
bt_12.grid(row=3, column=3, padx=1, pady=10, sticky="nsew")

bt_13 = tk.Button(window, text="1", font=("Arial", 14), bg="#56739A", fg="white", command=lambda: click('1'))
bt_13.grid(row=4, column=0, padx=1, pady=10, sticky="nsew")

bt_14 = tk.Button(window, text="2", font=("Arial", 14), bg="#56739A", fg="white", command=lambda: click('2'))
bt_14.grid(row=4, column=1, padx=1, pady=10, sticky="nsew")

bt_15 = tk.Button(window, text="3", font=("Arial", 14), bg="#56739A", fg="white", command=lambda: click('3'))
bt_15.grid(row=4, column=2, padx=1, pady=10, sticky="nsew")

bt_16 = tk.Button(window, text="+", font=("Arial", 14), bg="#ED7F10", fg="white", command=lambda: click('+'))
bt_16.grid(row=4, column=3, padx=1, pady=10, sticky="nsew")

bt_17 = tk.Button(window, text="0", font=("Arial", 14), bg="#56739A", fg="white", command=lambda: click('0'))
bt_17.grid(row=5, column=0, columnspan=2, padx=1, pady=10, sticky="nsew")

bt_18 = tk.Button(window, text=",", font=("Arial", 14), bg="#56739A", fg="white", command=lambda: click('.'))
bt_18.grid(row=5, column=2, padx=1, pady=10, sticky="nsew")

bt_19 = tk.Button(window, text="=", font=("Arial", 14), bg="#ED7F10", fg="white", command=calculate)
bt_19.grid(row=5, column=3, padx=1, pady=10, sticky="nsew")
t_box.bind("<KeyRelease>", lambda event: validate_input()) 

window.mainloop()

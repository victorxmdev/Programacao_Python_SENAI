import tkinter as tk


def somar():
    n1 = float(numero1.get())
    n2 = float(numero2.get())
    soma = n1 + n2
    resultado.config(text = f'{soma}')

# CRIAR AS OUTRAS FUNÇÕES 
# ----------

root = tk.Tk()

root.geometry('300x525')

root.title('CALCULADORA')

text = tk.Label(root, text= 'CALCULADORA', fg = 'blue', justify='center',bg='yellow')
text.grid(row=1, column=1,  )

text2 = tk.Label(root, text= 'Digite um numero')
text2.grid(row=2, column=2, pady=10, padx=10)

numero1 = tk.Entry(root, width=10)
numero1.grid(row=3, column=2, pady=10, padx=10)

text3 = tk.Label(root, text= 'Digite um numero')
text3.grid(row=4, column=2, pady=10, padx=10)

numero2 = tk.Entry(root, width=10)
numero2.grid(row=5, column=2, pady=10, padx=10)

resultado = tk.Label(root, text = 'resultado')
resultado.grid(row=6, column=2, pady=10, padx=10)

btn =  tk.Button(root, text = '+', command=somar)
btn.grid(row=7, column=2, pady=10, padx=10)


# CRIAR MAIS 3 BOTÕES 
# ----------


root.mainloop()
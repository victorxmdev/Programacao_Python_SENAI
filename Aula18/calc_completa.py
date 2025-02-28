import tkinter as tk

def somar():
    n1 = float(numero1.get())
    n2 = float(numero2.get())
    soma = n1 + n2
    resultado.config(text = f'{soma}')

def subtrair():
    n1 = float(numero1.get())
    n2 = float(numero2.get())
    subtracao = n1 - n2
    resultado.config(text=f'{subtracao}')

def multiplicar():
    n1 = float(numero1.get())
    n2 = float(numero2.get())
    multiplicacao = n1 * n2
    resultado.config(text=f'{multiplicacao}')

def dividir():
    n1 = float(numero1.get())
    n2 = float(numero2.get())
    if n2 != 0:
        divisao = n1 / n2
        resultado.config(text=f'{divisao}')
    else:
        resultado.config(text='Erro: Divisão por zero!')

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

resultado = tk.Label(root, text = 'Resultado')
resultado.grid(row=6, column=2, pady=10, padx=10)

btn =  tk.Button(root, text = '+', command=somar)
btn.grid(row=7, column=2, pady=10, padx=10)


btn_subtrair = tk.Button(root, text='-', command=subtrair)
btn_subtrair.grid(row=8, column=1, pady=10, padx=10)

btn_multiplicar = tk.Button(root, text='*', command=multiplicar)
btn_multiplicar.grid(row=8, column=2, pady=10, padx=10)

btn_dividir = tk.Button(root, text='/', command=dividir)
btn_dividir.grid(row=8, column=3, pady=10, padx=10)


root.mainloop()

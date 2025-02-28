import tkinter as tk

def display():
    texto = input_1.get()
    text_display.config(text = f'{texto}')

janela = tk.Tk()
janela.title('Texto')

# criação da janela
janela.geometry('350x500')

# texto na tela
text = tk.Label(janela, text = 'INSIRA UM TEXTO NA TELA')
text.pack()

# input
input_1 = tk.Entry(janela)
input_1.pack()

btn = tk.Button(janela, text ="clique aqui")
btn.pack()

text_display = tk.Label(janela, text = "teste")
text_display.pack()

janela.mainloop()
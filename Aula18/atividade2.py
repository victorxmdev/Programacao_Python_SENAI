#Crie um formulário em Tkinter, contendo, nome, idade, e-mail, endereço, celular.

import tkinter as tk

def enviar():
    nomeenv = nome.get()
    idadeenv = idade.get()
    emailenv = email.get()
    enderecoenv = endereco.get()
    celularenv = celular.get()
    
    print(f'Nome: {nomeenv}')
    print(f'Idade: {idadeenv}')
    print(f'E-mail: {emailenv}')
    print(f'Endereço: {enderecoenv}')
    print(f'Celular: {celularenv}')

root = tk.Tk()
root.title('Formulário')

tk.Label(root, text='Nome:').grid(row=0, column=0, padx=10, pady=10)
nome = tk.Entry(root)
nome.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text='Idade:').grid(row=1, column=0, padx=10, pady=10)
idade = tk.Entry(root)
idade.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text='E-mail:').grid(row=2, column=0, padx=10, pady=10)
email = tk.Entry(root)
email.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text='Endereço:').grid(row=3, column=0, padx=10, pady=10)
endereco = tk.Entry(root)
endereco.grid(row=3, column=1, padx=10, pady=10)

tk.Label(root, text='Celular:').grid(row=4, column=0, padx=10, pady=10)
celular = tk.Entry(root)
celular.grid(row=4, column=1, padx=10, pady=10)

# Submit button
btn_enviar = tk.Button(root, text='Enviar', command=enviar)
btn_enviar.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()

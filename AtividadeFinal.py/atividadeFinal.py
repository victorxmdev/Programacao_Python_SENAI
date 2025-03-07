import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def calcular_imc(peso, altura):
    #Calcula o índice de massa corporal (IMC) com base no peso e altura fornecidos.
    altura = altura.replace(',', '.')
    peso = peso.replace(',', '.')
    altura = float(altura)
    peso = float(peso)
    return peso / (altura ** 2)

def conectar():
    #Estabelece uma conexão com o banco de dados SQLite.
    return sqlite3.connect('teste.db')

def criar_tabela():
    #Cria a tabela 'usuarios' no banco de dados se ela não existir.
    conn = conectar()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        peso REAL NOT NULL,
        altura REAL NOT NULL,
        idade INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def inserir_usuario():
    #Insere um novo usuário no banco de dados com os dados fornecidos.
    nome = entry_nome.get()
    peso = entry_peso.get().replace(',', '.')
    altura = entry_altura.get().replace(',', '.')
    idade = entry_idade.get()
    if nome and peso and altura and idade:
        conn = conectar()
        c = conn.cursor()
        c.execute('INSERT INTO usuarios(nome, peso, altura, idade) VALUES(?,?,?,?)', (nome, peso, altura, idade))
        conn.commit()
        conn.close()
        messagebox.showinfo('AVISO', 'DADOS INSERIDOS COM SUCESSO!')
        mostrar_usuario()
    else:
        messagebox.showerror('ERRO', 'ALGO DEU ERRADO!')

def mostrar_usuario():
    #Exibe os dados dos usuários na tabela.
    for row in tree.get_children():
        tree.delete(row)
    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT * FROM usuarios')
    usuarios = c.fetchall()
    for usuario in usuarios:
        tree.insert("", "end", values=(usuario[0], usuario[1], usuario[2], usuario[3], usuario[4]))
    conn.close()

def delete_usuario():
    #xclui o usuário selecionado da tabela do banco de dados.
    dado_del = tree.selection()
    if dado_del:
        user_id = tree.item(dado_del)['values'][0]
        conn = conectar()
        c = conn.cursor()
        c.execute('DELETE FROM usuarios WHERE id = ?', (user_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo('', 'DADO DELETADO')
        mostrar_usuario()
    else:
        messagebox.showerror('', 'OCORREU UM ERRO')

def editar():
    #Edita os dados do usuário selecionado no banco de dados.
    selecao = tree.selection()
    if selecao:
        user_id = tree.item(selecao)['values'][0]
        novo_nome = entry_nome.get()
        novo_peso = entry_peso.get().replace(',', '.')
        novo_altura = entry_altura.get().replace(',', '.')
        novo_idade = entry_idade.get()
        messagebox.showinfo('Confirmação', f'Valores antigos:\nNome: {tree.item(selecao)["values"][1]}\nPeso: {tree.item(selecao)["values"][2]}\nAltura: {tree.item(selecao)["values"][3]}\nIdade: {tree.item(selecao)["values"][4]}\n\nNovos valores:\nNome: {novo_nome}\nPeso: {novo_peso}\nAltura: {novo_altura}\nIdade: {novo_idade}')
        if messagebox.askyesno('Confirmar', 'Deseja atualizar os dados?'):
            conn = conectar()
            c = conn.cursor()
            c.execute('UPDATE usuarios SET nome = ?, peso = ?, altura = ?, idade = ? WHERE id = ?', (novo_nome, novo_peso, novo_altura, novo_idade, user_id))
            conn.commit()
            conn.close()
            messagebox.showinfo('', 'DADOS ATUALIZADOS')
            mostrar_usuario()
    else:
        messagebox.showerror('', 'ALGO DEU ERRADO!')

janela = tk.Tk()
janela.title('CRUD')

# Criação dos labels e campos de entrada para nome, idade, peso e altura
label_nome = tk.Label(janela, text='Nome:')
label_nome.grid(row=0, column=0, padx=10, pady=10)

entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

label_idade = tk.Label(janela, text='Idade:')
label_idade.grid(row=1, column=0, padx=10, pady=10)

entry_idade = tk.Entry(janela)
entry_idade.grid(row=1, column=1, padx=10, pady=10)

label_peso = tk.Label(janela, text='Peso (kg):')
label_peso.grid(row=2, column=0, padx=10, pady=10)

entry_peso = tk.Entry(janela)
entry_peso.grid(row=2, column=1, padx=10, pady=10)

label_altura = tk.Label(janela, text='Altura (m):')
label_altura.grid(row=3, column=0, padx=10, pady=10)

entry_altura = tk.Entry(janela)
entry_altura.grid(row=3, column=1, padx=10, pady=10)

# Criação dos botões para salvar, deletar e atualizar os dados
btn_salvar = tk.Button(janela, text='Salvar', command=inserir_usuario)
btn_salvar.grid(row=4, column=0, padx=10, pady=10)

btn_deletar = tk.Button(janela, text='Deletar', command=delete_usuario)
btn_deletar.grid(row=4, column=1, padx=10, pady=10)

btn_atualizar = tk.Button(janela, text='Atualizar', command=editar)
btn_atualizar.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Criação da tabela para exibir os dados dos usuários
columns = ('ID', 'Nome', 'Peso', 'Altura', 'Idade')
tree = ttk.Treeview(janela, columns=columns, show='headings')
tree.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

for col in columns:
    tree.heading(col, text=col)

criar_tabela()
mostrar_usuario()

janela.mainloop()
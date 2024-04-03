import tkinter as tk
from tkinter import ttk
import modelo as crud

class PrincipalIBD():
    def __init__(self,win):
        self.objBD = crud.AppBD()
        self.janela = win

        self.treeProdutos = ttk.Treeview(self.janela,
        columns= ("codigo do produto", "Nome","Preço"), show= "heading"

janela = tk.Tk() # criar a janela principal
product_app = PrincipalIBD(janela)
janela.title("Bem vindo a aplicação de banco")
janela.geometry("900x700")
janela.mainloop()
from classes import Cliente
from classes import Funcionario
from classes import Produto
from classes import Vendas

from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fonte = ("Arial", "12")

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()

        self.titulo = Label(self.container1, text="Informe os dados de vendas :")
        self.titulo["font"] = ("Arial", "12", "bold")
        self.titulo.pack ()
                
        
        self.lblidproduto = Label(self.container2,
        text="id_produto:", font=self.fonte, width=10)
        self.lblidproduto.pack(side=LEFT)
        self.txtidproduto = Entry(self.container2)
        self.txtidproduto["width"] = 10
        self.txtidproduto["font"] = self.fonte
        self.txtidproduto.pack(side=LEFT)    
    
        
        self.lblcliente = Label(self.container4, text="Cliente:",
        font=self.fonte, width=10)
        self.lblcliente.pack(side=LEFT)
        self.txtcliente = Entry(self.container4)
        self.txtcliente["width"] = 25
        self.txtcliente["font"] = self.fonte
        self.txtcliente.pack(side=LEFT)        

    
        
        self.lbltelefone= Label(self.container5, text="Telefone:",
        font=self.fonte, width=10)
        self.lbltelefone.pack(side=LEFT)
        self.txttelefone = Entry(self.container5)
        self.txttelefone["width"] = 25
        self.txttelefone["font"] = self.fonte
        self.txttelefone.pack(side=LEFT)     
        
        self.lblquantidade= Label(self.container6, text ="Quantidade:",
        font=self.fonte, width=10)
        self.lblquantidade.pack(side=LEFT)
        self.txtquantidade = Entry(self.container6)
        self.txtquantidade["width"] = 25
        self.txtquantidade["font"] = self.fonte
        self.txtquantidade.pack(side=LEFT)     

        self.lblvalor= Label(self.container7, text="Valor:",
        font=self.fonte, width=10)
        self.lblvalor.pack(side=LEFT)
        self.txtvalor = Entry(self.container7)
        self.txtvalor["width"] = 25
        self.txtvalor["font"] = self.fonte
        self.txtvalor.pack(side=LEFT) 
              
           
        self.widget2 = Label(master)
        self.widget2.pack()
        self.lblmsg = Label(self.widget2, text="Finalizar cadastro")
        self.lblmsg["font"] = ("Verdana", "10", "italic", "bold")
        self.lblmsg.pack ()
        self.txtsair = Button(self.widget2)
        self.txtsair["text"] = "Sair"
        self.txtsair["font"] = ("Arial", "10")
        self.txtsair["width"] = 10
        self.txtsair["command"] = self.widget2.quit
        self.txtsair.pack()     
        
    
    def set_produto(self):
        lista_produtos = Produto("id_produto", "estoque")
        lista_produtos = []
        lista_produtos.append({'id_produto': self.lblidproduto,
                               'estoque': ""})        
        
    def set_cliente(self):
        lista_cliente = []
        lista_cliente.append(self.lblcliente)
        
    
    def set_telefone(self):
        lista_telefone = []
        lista_telefone.append(self.lbltelefone)
        
    
    def set_quantidade(self):
        lista_quantidade = []
        lista_quantidade.append(self.lblquantidade)
        
    
    def set_valor(self):
        lista_valor = []
        lista_valor.append(self.lblvalor)
        
    def get_produto(self):
        return self.get_produto
        
    
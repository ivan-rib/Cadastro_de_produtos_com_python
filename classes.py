
class Cliente():
    
    nome = ""
    telefone = ""
    
    def __init__ (self, nome,telefone):
        self.nome = nome
        self.telefone = telefone
        
            
    def set_nome(self, nome):
        try:
            self.nome = nome
        except Exception as e:
            print(str(e))
    
                
    def set_telefone(self, telefone):
        try:
            self.telefone = telefone
        except Exception as e:
            print(str(e))
            
            
    def get_nome(self):
        return self.nome       
    
           
    def get_telefone(self):
        return self.telefone
        
            
class Funcionario():
    
    nome_funcionario = ""    
    
    def __init__ (self, nome_funcionario):
        self.nome_funcionario = nome_funcionario        
        
    def set_nome(self, nome):
        try:
            self.nome = nome
        except Exception as e:
            print(str(e))
    
    def set_setor(self, setor):
        try:
            self.setor = setor
        except Exception as e:
            print(str(e))
        
    def get_nome(self):
        return self.nome       
    
    def get_setor(self):
        return self.setor  
 
class Produto():
       
    id_produto = ""
    estoque = 0
    
    def __init__(self, id_produto,estoque):
        
        self.id_produto = id_produto
        self.estoque = estoque
       
    def set_id(self, id_produto):
        try:
            self.id_produto = id_produto
        except Exception as e:
            print(str(e))
    
                
    def set_estoque(self, estoque):
        try:
            self.estoque = estoque
        except Exception as e:
            print(str(e))   
            
    def get_id_produto(self):
        return self.id_produto       
    
    def get_estoque(self):
        return self.estoque 
    
    
            
class Vendas(Cliente):
    
    quantidade = 0
    valor = 0
    
    def __init__ (self, nome,telefone, quantidade, valor):
        super().__init__(nome, telefone)
        self.quantidade = quantidade
        self.valor = valor
        
    def set_id(self, quantidade):
        try:
            self.quantidade = quantidade
        except Exception as e:
            print(str(e))
    
    def set_descricao(self, valor):
        try:
            self.valor = valor
        except Exception as e:
            print(str(e))
            
    def get_quantidade(self):
        return self.quantidade      
    
    def get_valor(self):
        return self.valor 
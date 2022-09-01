from conexao import conexao

class model:
    def _init_(self):
        self.conex = conexao()
        self.conex.conectar()
        
    def inserir(self, nome, telefone, endereco, dataDenascimento):
        try:
            sql = "Insert into person(codigo, nome, telefone, endereco, dataDenascimento) values('', '{}', '{}', '{}', '{}')".format(nome, telefone, endereco, dataDenascimento)
            self.conex.execute(sql)
            self.conex.commit()
            return "{} Inserido!".format(self.conex.rowcount)
        except Exception as erro:
            return erro
        
    
    def consultar(self, codigo):
        try:
            sql = "select * from person where codigo = '{}'".format(codigo)
            self.conex.execute(sql)
            
            for(codigo, nome, telefone, endreco, dataDeNascimento) in self.conex:
                msg = msg + "\nCódigo: {}, Nome: {}, Telefone: {}, Endereço: {}, Nascimento: {}".format(codigo, nome, telefone, endreco, dataDeNascimento)
            return msg
    except Exception as erro:
        return erro
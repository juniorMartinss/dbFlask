import mysql.connector #importando a biblioteca para possibilitar a conexão com o banco de dados
from mysql.connector import errorcode #habilitar mensagem de erro

class conexao:
    def _init_(self):
        pass
        
    def conectar(self):
        try: 
            self.db_connection = mysql.connector.connect(host="localhost", user="root", password="", database="bancoFlask") #endereço para conexão com o banco de dados 
            return self.db_connection
        except mysql.connector.Error as erro:
            if erro.errno == errorcode.ER_BAD_DB_ERROR:
                print('Banco de Dados não EXISTE!')
            elif erro.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('Usuário ou senha INVÁLIDO!')
            else:
                print(erro)
        else:
            self.db_connection.close()
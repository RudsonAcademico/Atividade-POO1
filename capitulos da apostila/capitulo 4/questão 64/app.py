#from banco_dados_sql import Conexao
from banco_dados_nosql import Conexao

conexao = Conexao()
print(conexao.conectar())

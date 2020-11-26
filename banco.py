import mysql.connector
from caixa import CaixaDiario, depositoPrevio, servicoPrevio


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="CartorioDP",
  autocommit=True
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM usuario")

myresult = mycursor.fetchall()


def login_bd(nome,senha):
    for x in myresult:
        if x[1] == nome and x[2] == senha:
            return True


def busca_nome_bd(nome_busca):
   
    
    #sql = ("SELECT nomecrianca, DATE_FORMAT(datanasc,'%d-%m-%Y') AS datanascimento,  DATE_FORMAT(dataregistro,'%d-%m-%Y') AS dataDecla,livro,letra,folha,termo FROM nascimentos LIMIT 5")
    sql= ("SELECT * FROM nascimentos")
    mycursor.execute(sql)
    
    lista_nomes=[]
    myresult = mycursor.fetchall()
    
    for x in myresult:
      
     
        if nome_busca in x[7]:
           
            lista_nomes.append(x)
    
    return lista_nomes


def busca_deposito():
    sql= ("SELECT * FROM deposito_previo")
    mycursor.execute(sql)

    lista_depositos=[]
    depositos =[]
    lista_0 = []
    
    myresult = mycursor.fetchall()

    for x in myresult:
        lista_depositos = depositoPrevio(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7])
        
        depositos = depositoPrevio(lista_depositos.cod_deposito,lista_depositos.cpf_solicitante,lista_depositos.nome_solicitante,lista_depositos.tipo_documento,lista_depositos.criador,lista_depositos.data_criacao,lista_depositos.telefone,lista_depositos.usuario)
        
        lista_0.append(depositos)
        
    return lista_0

def cadastra_deposito(cpf,nome,tipo_documento,criador,data_e_hora_em_texto,telefone,id_user):
        #insert into deposito_previo(cpf,nome_solicitante,tipo_documento,criador,data_criacao,telefone,Usuario_idUsuario) values(' 025-762-354-62  ','LETICIA MARREIRO','TESTE DE REGISTRO COM DIRCE','Dirce','2020-11-26',null,2);
        sql = "INSERT INTO deposito_previo (cpf,nome_solicitante,tipo_documento,criador,data_criacao,telefone,Usuario_idUsuario) VALUES (%s, %s,%s, %s,%s, %s,%s)"
        val = (cpf,nome,tipo_documento,criador,data_e_hora_em_texto,telefone,id_user)
        #insert into deposito_previo(criador,tipo_documento,cpf,data_criação,horario,Usuario_idUsuario) values ('Lucas','ESCRITURA PUBLICA DE COMPRA E VENDA','025-753-123.69','2020-11-23',null,1);
        mycursor.execute(sql, val)
        print(mycursor.rowcount, "record inserted.")
def busca_servico():
    sql= ("SELECT * FROM servico_previo")
    mycursor.execute(sql)
    lista_servicos =[]
    servicos = []
    servico_0 =[]

    myresult = mycursor.fetchall()

    for x in myresult:
        lista_servicos = servicoPrevio(x[8],x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7])
        servicos = servicoPrevio(lista_servicos.cod_deposito,lista_servicos.cod_servico,lista_servicos.descricao_servico,lista_servicos.data_registro,lista_servicos.data_entrega,lista_servicos.user_inicio,lista_servicos.user_fim,lista_servicos.realizacao,lista_servicos.valor)
        servico_0.append(servicos)
    return servico_0




















         
    

# import mysql.connector
# from caixa import CaixaDiario, depositoPrevio, servicoPrevio

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="root",
#   database="CartorioDP"
# )

# mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM usuario")

# myresult = mycursor.fetchall()


# def login_bd(nome,senha):
#     for x in myresult:
#         if x[1] == nome and x[2] == senha:
#             return True


# def busca_nome_bd(nome_busca):

#     #sql = ("SELECT nomecrianca, DATE_FORMAT(datanasc,'%d-%m-%Y') AS datanascimento,  DATE_FORMAT(dataregistro,'%d-%m-%Y') AS dataDecla,livro,letra,folha,termo FROM nascimentos LIMIT 5")
#     sql= ("SELECT * FROM nascimentos")
#     mycursor.execute(sql)

#     lista_nomes=[]
#     myresult = mycursor.fetchall()

#     for x in myresult:


#         if nome_busca in x[7]:

#             lista_nomes.append(x)

#     return lista_nomes


# def busca_deposito():
#     sql= ("SELECT * FROM deposito_previo")
#     mycursor.execute(sql)

#     lista_depositos=[]
#     depositos =[]
#     lista_0 = []

#     myresult = mycursor.fetchall()

#     for x in myresult:
#         lista_depositos = depositoPrevio(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7])

#         depositos = depositoPrevio(lista_depositos.cod_deposito,lista_depositos.cpf_solicitante,lista_depositos.nome_solicitante,lista_depositos.tipo_documento,lista_depositos.criador,lista_depositos.data_criacao,lista_depositos.telefone,lista_depositos.usuario)

#         lista_0.append(depositos)
#     return lista_0

# def cadastra_deposito():

#         #insert into deposito_previo(criador,tipo_documento,cpf,data_criação,horario,Usuario_idUsuario) values ('Lucas','ESCRITURA PUBLICA DE COMPRA E VENDA','025-753-123.69','2020-11-23',null,1);
#         pass






















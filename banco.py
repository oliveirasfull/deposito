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
        sql= ("SELECT * FROM nascimentos WHERE nomecrianca LIKE '%' %s '%'")
        teste = (nome_busca,)
        mycursor.execute(sql,teste)
        print('teste_BD')
        lista_nomes=[]
        myresult = mycursor.fetchall()
        
        for x in myresult:
            
            
            if nome_busca in x[7]:
                
                lista_nomes.append(x)
        
        return lista_nomes
def busca_deposito():
    #sql= ("SELECT deposito_previo.iddeposito_previo,deposito_previo.cpf,deposito_previo.nome_solicitante,deposito_previo.tipo_documento,deposito_previo.criador,deposito_previo.data_criacao,deposito_previo.telefone,deposito_previo.Usuario_idUsuario FROM servico_previo,deposito_previo where servico_previo.deposito_previo_iddeposito_previo = deposito_previo.iddeposito_previo AND realizado =0")
    sql = ("SELECT * FROM deposito_previo ORDER BY iddeposito_previo DESC LIMIT 500")
    mycursor.execute(sql)

    lista_depositos=[]
    depositos =[]
    lista_0 = []
    
    myresult = mycursor.fetchall()

    for x in myresult:
        lista_depositos = depositoPrevio(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8])
        
        depositos = depositoPrevio(lista_depositos.cod_deposito,lista_depositos.cpf_solicitante,lista_depositos.nome_solicitante,lista_depositos.tipo_documento,lista_depositos.criador,lista_depositos.data_criacao,lista_depositos.telefone,lista_depositos.usuario,lista_depositos.pago)
        
        lista_0.append(depositos)
        
    return lista_0
def cadastra_deposito(cpf,nome,tipo_documento,criador,data_e_hora_em_texto,telefone,id_user,pago):
        #insert into deposito_previo(cpf,nome_solicitante,tipo_documento,criador,data_criacao,telefone,Usuario_idUsuario) values(' 025-762-354-62  ','LETICIA MARREIRO','TESTE DE REGISTRO COM DIRCE','Dirce','2020-11-26',null,2);
        sql = "INSERT INTO deposito_previo (cpf,nome_solicitante,tipo_documento,criador,data_criacao,telefone,Usuario_idUsuario,pago) VALUES (%s, %s,%s, %s,%s, %s,%s,%s)"
        val = (cpf,nome,tipo_documento,criador,data_e_hora_em_texto,telefone,id_user,pago)
        #insert into deposito_previo(criador,tipo_documento,cpf,data_criação,horario,Usuario_idUsuario) values ('Lucas','ESCRITURA PUBLICA DE COMPRA E VENDA','025-753-123.69','2020-11-23',null,1);
        mycursor.execute(sql, val)
        print(mycursor.rowcount, "record inserted.")
        print("************************************************************")
        print("CRIOU DEPOSITO")
        print("************************************************************")        
def delete_deposito(cod):
        sql2 = "DELETE FROM servico_previo WHERE deposito_previo_iddeposito_previo = %s"
        teste = (cod,)
        mycursor.execute(sql2,teste)
        sql = "DELETE FROM deposito_previo WHERE iddeposito_previo = %s"
        mycursor.execute(sql,teste)
        print(mycursor.rowcount, "record inserted.")
        print("************************************************************")
        print("APAGOU DEPOSITO")
        print("************************************************************")
def delete_servico(cod):
        sql2 = "DELETE FROM servico_previo WHERE idservico_previo = %s"
        teste = (cod,)
        mycursor.execute(sql2,teste)
        print(mycursor.rowcount, "record inserted.")
        print("************************************************************")
        print("APAGOU SERVICO")
        print("************************************************************")
def busca_servico(codigo):
        sql= "SELECT * FROM servico_previo WHERE deposito_previo_iddeposito_previo = %s"
        teste = (codigo,)
        mycursor.execute(sql,teste)
        lista_servicos =[]
        servicos = []
        servico_0 =[]   
        myresult = mycursor.fetchall()  
        for x in myresult:
            lista_servicos = servicoPrevio(x[8],x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8])
            servicos = servicoPrevio(lista_servicos.cod_deposito,lista_servicos.cod_servico,lista_servicos.descricao_servico,lista_servicos.data_registro,lista_servicos.data_entrega,lista_servicos.user_inicio,lista_servicos.user_fim,lista_servicos.realizacao,lista_servicos.valor,lista_servicos.pago)
            servico_0.append(servicos)
        
        return servico_0
def cadastro_servico(descricao_servico,data_registro,data_entrega,user_inicio,user_fim,realizado,valor,deposito_previo_iddeposito_previo,pago):
        sql = "INSERT INTO servico_previo (descricao_servico,data_registro,data_entrega,user_inicio,user_fim,realizado,valor,deposito_previo_iddeposito_previo,pago) VALUES (%s, %s,%s, %s,%s, %s,%s,%s)"
        
        val = (descricao_servico,data_registro,data_entrega,user_inicio,user_fim,realizado,valor,deposito_previo_iddeposito_previo,pago)
        mycursor.execute(sql, val)
        print(mycursor.rowcount, "record inserted.")
        print("************************************************************")
        print("CRIOU SERVIÇO")
        print("************************************************************")   
def atualizar_servico(cod,data):
        sql = "UPDATE servico_previo SET realizado = %s WHERE idservico_previo = %s"
        val = ("1", cod)
        mycursor.execute(sql, val)
        sql1 = "UPDATE servico_previo SET data_entrega = %s WHERE idservico_previo = %s"
        val1 =(data,cod) 
        mycursor.execute(sql1, val1)
        print(mycursor.rowcount, "record inserted.")
        print("************************************************************")
        print("REALIZOU O SERVIÇO")
        print("************************************************************")   
def servicos_abertos():
        sql = "SELECT SUM(VALOR) FROM servico_previo WHERE realizado = 0"
        
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for i in myresult:
                valor_total= i[0]
        sql_parte2 ="SELECT SUM(servico_previo.valor) FROM deposito_previo,servico_previo WHERE servico_previo.deposito_previo_iddeposito_previo = deposito_previo.iddeposito_previo and deposito_previo.pago = 0"

        mycursor.execute(sql_parte2)
        myresult2 = mycursor.fetchall()
        for i in myresult2:
                total_orcamento = i[0]
        total_deposito_previo = valor_total - total_orcamento

        return total_deposito_previo
def lista_de_depositos_com_servico_aberto():
        sql = "SELECT deposito_previo_iddeposito_previo from servico_previo where realizado =0 group by deposito_previo_iddeposito_previo"
        lista_aberta =[]
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        
        return myresult
def qtd_servicos_abertos():
        sql= 'SELECT count(*) FROM servico_previo WHERE realizado = 0'
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for i in myresult:
                valor = i[0]

        return valor
def servicos_realizado_dia(data):

        #DATA = 2020-12-02
        lista_realizados=[]
        lista_realizados_dia =[]
        sql ="SELECT deposito_previo_iddeposito_previo,data_entrega,descricao_servico,valor,user_inicio FROM servico_previo where data_entrega = %s AND realizado =1"
        val = (data,)
        mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
        
        for x in myresult:
                lista_realizados = (x[0],x[1],x[2],x[3],x[4])
                lista_realizados_dia.append(lista_realizados)
               
        return lista_realizados_dia
def pagamento_servico(cod):
        sql = "UPDATE deposito_previo SET pago = %s WHERE idservico_previo = %s"
        val = ("1", cod)
        mycursor.execute(sql, val)
        print(mycursor.rowcount, "record inserted.")
        print("************************************************************")
        print("PAGAMENTO REALIZADO COM SUCESSO")
        print("************************************************************")   

def sistema():
        sql = "UPDATE deposito_previo SET pago = %s WHERE idservico_previo = %s"

        


       




















         
    

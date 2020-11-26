from flask import Flask, render_template,request, redirect
import json

from caixa import CaixaDiario, depositoPrevio, servicoPrevio
from banco import *
app = Flask(__name__)


user = 'Paulo'






#lista_deposito_previo = depositoPrevio('4','321.654.963-00','RONEY BARROS FERREIRA- ME','BAIXA/CANCELAMENTO DE CDULA DE CREDITO N° 5043',None,'29/07/2020',None,user)
#lista_deposito_previo1 = depositoPrevio('2','321.654.963-00','MARCELO ALGUNTO CAVOLCANTE','BAIXA/CANCELAMENTO DE CDULA DE CREDITO N° 5043',None,'13/11/2020',None,user)

#all_depositos_previos = [lista_deposito_previo, lista_deposito_previo1]
all_depositos_previos = []

#lista_servico_previo = servicoPrevio('1','102','PROTOCOLO PARA TESTE 1 VIA ','29/07/2020 12:49','10/08/2020 12:49',user,None,False,22.12,lista_deposito_previo.cpf_solicitante,lista_deposito_previo.nome_solicitante,lista_deposito_previo.tipo_documento,lista_deposito_previo.criador,'29/07/2020 12:49')

#lista_servico_previo0 = servicoPrevio('1','100','PROTOCOLO PARA TESTE 2 VIA ','29/07/2020 12:49','10/08/2020 12:49',user,None,False,22.12,lista_deposito_previo.cpf_solicitante,lista_deposito_previo.nome_solicitante,lista_deposito_previo.tipo_documento,lista_deposito_previo.criador,'29/07/2020 12:49')
#lista_servico_previo1 = servicoPrevio('2', '101','PROTOCOLO MARCELO','13/11/2020 12:49','10/08/2020 12:49',user,None,False,19.10,lista_deposito_previo1.cpf_solicitante,lista_deposito_previo1.nome_solicitante,lista_deposito_previo1.tipo_documento,lista_deposito_previo1.criador,'29/07/2020 12:49')
#all_servicos_previos = [lista_servico_previo,lista_servico_previo1,lista_servico_previo0]

serv1 = CaixaDiario(user,'1','19.10','CERTIDAO DE 2° VIA','026.879.987-30','27/10/2020 15:16') 

lista = [serv1]

registro_nome = []
lista_deposito_previo3 =[]



@app.route('/', methods=['GET'])
def login():

    return render_template('login.html')
@app.route('/autenticar', methods=['POST'])
def autenticar ():
    senha = request.form['senha'] 
    usuario = request.form['usuario']
    validar = login_bd(usuario,senha)
    if validar == True:
        return redirect('/index')
    else:
        ##return redirect('/erro') 
        return redirect('/index')

@app.route('/erro')
def erro():

    return render_template('login_erro.html')
@app.route('/index')
def index():
    usuario = user
    
    return render_template('index.html', usuario=usuario)



@app.route('/nascimento')
def nascimento():
    sub_registro = []
    for x in registro_nome:
        sub_registro = x 



    return render_template('livros/nascimento.html',nascimento=sub_registro)

@app.route('/busca' ,methods=['GET', 'POST'])
def busca_nascimento():
    registro_nome.clear()
    nome = request.form['nome_sql']
    nome_maiusculo = nome.upper()
    registro_nome.append(busca_nome_bd(nome_maiusculo))
    
    
    return redirect('/nascimento')




@app.route('/casamento')
def casamento():
    with open('static/json/casamentos.json', encoding='utf-8') as f:
        data= json.load(f)
    return render_template('livros/casamento.html',casamentos=data)

@app.route('/obito')
def obito():
    with open('static/json/obitos.json', encoding='utf-8') as f:
        data= json.load(f)
   
    return render_template('livros/obito.html',obitos=data)

@app.route('/tables')
def tables():
    
    

    
    return render_template('tables.html')

@app.route('/servico')
def servico():
    total = float()
    for i in lista:
       total += float(i.valor)
                        
  

    return render_template('servico.html',servico =lista, bruto = total)
@app.route('/caixadia' ,methods=['GET', 'POST'])
def caixaDoDia():
    from random import randint
    from datetime import datetime
    cpf = request.form['cpf']
    valor = request.form['valor']
    servico = request.form['servico']

    ale =randint(2,100)
    
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y')
    caixa = CaixaDiario(user,ale,valor,servico,cpf,data_e_hora_em_texto)

    lista.append(caixa)
  
    return redirect('/servico')
@app.route('/previo')
def previo():
    
    all_depositos_previos = busca_deposito()
    for i in all_depositos_previos:
        print(i.cod_deposito)

    
    return render_template('cadastro_deposito_previo.html',depositoGlobal= all_depositos_previos,servico =lista)


@app.route('/carrega_servicos' ,methods=['GET', 'POST'])
def carrega_servicos():
    

    #all_depositos_previos.append(busca_deposito(lista_deposito_previo3))
    
    
    
    


    
    return redirect('/previo')

@app.route('/depositoPrevio', methods=['GET','POST'])
def deposito_previo():
    from datetime import datetime
    from random import randint
    cpf = request.form['cpf']
    nome = request.form['nome_solicitante']
    tipo_documento = request.form['tipo_documento']
    criador = request.form['criador']
    telefone = request.form['telefone_solicitante']

    ale =randint(2,100)
    ale2 =randint(100,200)

    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y')
    deposito = depositoPrevio(ale,cpf,nome,tipo_documento,criador,data_e_hora_em_texto,telefone,user)

    
    

    
    all_depositos_previos.append(deposito)

  



    return redirect('/previo')



@app.route('/servicoPrevio/<cod>', methods=['GET','POST'])
def servico_previ0(cod):
    from datetime import datetime
    from random import randint
    data_e_hora_atuais = datetime.now()
    ale2 =randint(100,200)
    lista_servico=None
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y')
    codigo = cod 
    servico_previo = request.form['servico_previo']
    valor_servico = request.form['valor_servico']

    for out in all_depositos_previos:
        for deposito in all_servicos_previos:
            if deposito.cod_deposito == codigo:
                lista_servico = servicoPrevio(deposito.cod_deposito,ale2,servico_previo,data_e_hora_atuais,None,user,None,False,valor_servico,deposito.cpf_solicitante,deposito.nome_solicitante,deposito.tipo_documento,deposito.criador,data_e_hora_em_texto)
                break
            all_servicos_previos.append(lista_servico)
   

    return redirect ('/previo')
    

    
    

    

@app.route('/registro/<cod>', methods=['POST'])
def registro(cod):
    codigo = int(cod)
    
    lista_doida = []
    all_depositos_previos = busca_deposito()

    for i in all_depositos_previos:
        if i.cod_deposito == codigo:
            deposito_serv = depositoPrevio(i.cod_deposito,i.cpf_solicitante,i.nome_solicitante,i.tipo_documento,i.criador,i.data_criacao,i.telefone,i.usuario)
            lista_doida.append(deposito_serv)

   
            


  
   
    return render_template('registro_servico.html',teste=cod, deposito = lista_doida)












@app.route('/cards')
def card():
    return render_template('cards.html')

@app.route('/depositoPrevioTotal')
def DepositoPrevio():
    
    pendente = 52000
    
    return render_template('deposito_previo.html',pendente=pendente,caixa=32000,progresso=50)
          

if __name__ == '__main__':
   app.run(host= '0.0.0.0',debug=True,port='5000')
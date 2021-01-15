from flask import Flask, render_template,request, redirect, url_for, make_response
import json
import pdfkit
from  flask  import  Flask 

from caixa import CaixaDiario, depositoPrevio, servicoPrevio
from banco import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from io import BytesIO




app = Flask(__name__)






user = 'Paulo'






#lista_deposito_previo = depositoPrevio('4','321.654.963-00','RONEY BARROS FERREIRA- ME','BAIXA/CANCELAMENTO DE CDULA DE CREDITO N° 5043',None,'29/07/2020',None,user)
#lista_deposito_previo1 = depositoPrevio('2','321.654.963-00','MARCELO ALGUNTO CAVOLCANTE','BAIXA/CANCELAMENTO DE CDULA DE CREDITO N° 5043',None,'13/11/2020',None,user)

#all_depositos_previos = [lista_deposito_previo, lista_deposito_previo1]
all_depositos_previos = busca_deposito()

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
    print('tese')
    
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
    nome_minusculo = request.form['nome_solicitante']
    nome = nome_minusculo.upper()
    tipo_documento_minus = request.form['tipo_documento']
    tipo_documento = tipo_documento_minus.upper()
    criador = request.form['criador']
    telefone = request.form['valor_servico']

    #ale =randint(2,100)
    ale2 =randint(100,200)


    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%y/%m/%d')
  
    

    return render_template('caixadia.html')


@app.route('/previo')
def previo():
    deposito_com_servico_aberto1 =[]
    all_depositos_previos = busca_deposito()
    deposito_com_servico_aberto = lista_de_depositos_com_servico_aberto()
    for i in deposito_com_servico_aberto:
        deposito_com_servico_aberto1.append(i[0])
        
    
    return render_template('cadastro_deposito_previo.html',depositoGlobal= all_depositos_previos,servico =lista,servico_ativo = deposito_com_servico_aberto1)


@app.route('/apaga_deposito/<cod>' ,methods=['GET', 'POST'])
def apagar_deposito(cod):
    delete_deposito(cod)
    

    #all_depositos_previos.append(busca_deposito(lista_deposito_previo3))
        
    return redirect('/previo')
@app.route('/apaga_servico/<ist>/<cod>' ,methods=['GET', 'POST'])
def apagar_servico(ist,cod):
    delete_servico(cod)

   
    return redirect (url_for('registro',cod=ist))


@app.route('/recarrega_deposito')
def recarregar_deposito():
    redirect('/previo')


@app.route('/depositoPrevio', methods=['GET','POST'])
def deposito_previo():
    from datetime import datetime
    from random import randint
    cpf = request.form['cpf']
    nome_minusculo = request.form['nome_solicitante']
    nome = nome_minusculo.upper()
    tipo_documento_minus = request.form['tipo_documento']
    tipo_documento = tipo_documento_minus.upper()
    criador = request.form['criador']
    telefone = request.form['telefone_solicitante']

    #ale =randint(2,100)
    ale2 =randint(100,200)
    pago =1

    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%y/%m/%d')
    if criador == "Joao Paulo":
        id_user = 3
    if criador == "Dirce":
        id_user = 2
    if criador == "Gabriel":
        id_user = 5
    if criador == "Natacha":
        id_user = 6
    if criador == "Everaldo":
        id_user = 7
    
    cadastra_deposito(cpf,nome,tipo_documento,criador,data_e_hora_em_texto,telefone,id_user,pago)

    return redirect('/previo')

@app.route('/registro/<cod>', methods=['GET','POST'])
def registro(cod):
    total = 0
    servico_realizado = 0
    servico_aberto = 0
    
    codigo = int(cod)
    lista_servicos =[]
    lista_doida = []
    
    all_depositos_previos = busca_deposito()
    all_servicos_previos = busca_servico(codigo)


    for i in all_depositos_previos:
        if i.cod_deposito == codigo:
            deposito_serv = depositoPrevio(i.cod_deposito,i.cpf_solicitante,i.nome_solicitante,i.tipo_documento,i.criador,i.data_criacao,i.telefone,i.usuario,i.pago)
            lista_doida.append(deposito_serv)
   
    for j in all_servicos_previos:
        if j.cod_deposito == codigo:
            servicos = servicoPrevio(j.cod_deposito,j.cod_servico,j.descricao_servico,j.data_registro,j.data_entrega,j.user_inicio,j.user_fim,j.realizacao,j.valor)

            lista_servicos.append(servicos)

            if j.realizacao == 0:
                
                servico_aberto = j.valor + servico_aberto
            if j.realizacao == 1:
                servico_realizado = j.valor + servico_realizado
    total = servico_realizado+servico_aberto

  
    #valor_servico1 = request.form['valor_servico'] 
   
    return render_template('registro_servico.html',teste=cod, deposito = lista_doida, servicos = lista_servicos,total=total,servico_aberto=servico_aberto,servico_realizado=servico_realizado)


@app.route('/servicoPrevio/<cod>', methods=['GET','POST'])
def servico_previ0(cod):  
    from datetime import datetime
    from random import randint
    all_depositos_previos = busca_deposito()
    pago = 1
    data_e_hora_atuais = datetime.now()
    ale2 =randint(100,200)
    lista_servico=None
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%y/%m/%d')
    codigo = int(cod)
    all_servicos_previos = busca_servico(codigo)
    data_entrega = None
    user_fim = None
    realizado = 0
    servico_previo = request.form['servico_previo']
    valor_servico = request.form['valor_servico']
    servico_previo_maiunsculo = servico_previo.upper()
    for i in all_depositos_previos:   
        if i.cod_deposito == codigo:
            cadastro_servico(servico_previo_maiunsculo,data_e_hora_em_texto,data_entrega,i.criador,user_fim,realizado,valor_servico,codigo,pago)
             
                #cadastro_servico(servico_previo_maiunsculo,data_e_hora_em_texto,data_entrega,j.criador,user_fim,realizado,valor_servico,i.cod_deposito)

    return redirect (url_for('registro',cod=cod))


@app.route('/comprovante/<cod>', methods=['GET','POST'])
def comprovante(cod):
    codigo = int(cod)
    from reportlab.lib import utils
    from reportlab.lib.pagesizes import letter
    total = 0
    servico_realizado = 0
    servico_aberto = 0
    lista_servicos =[]

    nome = 'LUCAS CRISTHIAN'
    
    
    lista_doida = []
    
    all_depositos_previos = busca_deposito()
    all_servicos_previos = busca_servico(cod)

  
    for i in all_depositos_previos:
        deposito_serv = depositoPrevio(i.cod_deposito,i.cpf_solicitante,i.nome_solicitante,i.tipo_documento,i.criador,i.data_criacao,i.telefone,i.usuario,i.pago)
        lista_doida.append(deposito_serv)

    for x in lista_doida:
        if x.cod_deposito == codigo:
            print('LARISSA TU E TOP')
            nome = x.nome_solicitante

        	
   
    for j in all_servicos_previos:

            servicos = servicoPrevio(j.cod_deposito,j.cod_servico,j.descricao_servico,j.data_registro,j.data_entrega,j.user_inicio,j.user_fim,j.realizacao,j.valor)

            lista_servicos.append(servicos)

            if j.realizacao == 0:
                
                servico_aberto = j.valor + servico_aberto
            if j.realizacao == 1:
                servico_realizado = j.valor + servico_realizado
    total = servico_realizado+servico_aberto
    

  

    
    output = BytesIO()  
    p = canvas.Canvas(output)
    p.setTitle('comprovante')
    image_path ="../Deposito_previo_2.0/static/img/cart.jpg"
    img = utils.ImageReader(image_path)
    img_width, img_height = img.getSize()
    aspect = img_height / float(img_width)
 
    p.saveState()
    p.drawImage(image_path, 225, 765,
               width=200, height=(150 * aspect))
    p.restoreState()
    p.drawString(105,750,'SERVENTIA EXTRAJUDICIAL DA COMARCA DE SENA MADUREIRA/AC')
    p.drawString(30,703,'DOCUMENTO:')
    p.line(120,700,580,700)

   


    
    p.drawString(120,703,nome)
    #p.drawString(500,750,"12/12/2010")
    

   
    p.line(100,50,510,50)
    p.drawString(245,30,'FUNCIONÁRIO')
    p.showPage()
    p.save()

    pdf_out = output.getvalue()
    output.close()  
    response = make_response(pdf_out)
    response.headers['Content-Disposition'] = "attachment; filename=comprovante.pdf"
    response.mimetype = 'application/pdf'




    return response
    

   



@app.route('/atualiza/<ist>/<cod>', methods=['GET','POST'])
def atualiza_servico(ist,cod):
    from datetime import datetime
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%y/%m/%d')
    atualizar_servico(cod,data_e_hora_em_texto)



    return redirect (url_for('registro',cod=ist))


@app.route('/depositoPrevioTotal')
def DepositoPrevio():
    from datetime import datetime
    
    total = 0.0
    
    data_e_hora_atuais = datetime.now()
    data = data_e_hora_atuais.strftime('%y/%m/%d')
    servico_do_dia =[]
    pendente = servicos_abertos()
    for i in pendente:
        pendente1= i[0]
    qtd = qtd_servicos_abertos()

    servicos_dia = servicos_realizado_dia(data)
    for i in servicos_dia:
        servico_do_dia.append(i)
    for i in servico_do_dia:
        parte = i[3]
        parte1 = float(parte)
       
       
        total = total + parte1
       
    
    return render_template('deposito_previo.html',pendente=pendente1,caixa=32000,qtd_servicos = qtd,servico_do_dia=servico_do_dia,total = total)

          

if __name__ == '__main__':
   app.run(host= '0.0.0.0',debug=True,port='5000')
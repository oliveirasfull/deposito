class CaixaDiario:
    def __init__(self,usuario,cod_servico,valor,descricao,cpf,data):
        self.usuario = usuario
        self.cod_servico = cod_servico
        self.valor = valor
        self.descricao = descricao
        self.cpf= cpf
        self.data= data


class depositoPrevio(object):
    def __init__(self,cod_deposito,cpf_solicitante,nome_solicitante,tipo_documento,criador,data_criacao,telefone,usuario,pago):
        self.cod_deposito = cod_deposito
        self.cpf_solicitante = cpf_solicitante
        self.nome_solicitante = nome_solicitante
        self.tipo_documento = tipo_documento
        self.criador = criador
        self.data_criacao = data_criacao
        self.telefone = telefone
        self.usuario = usuario
        self.pago = pago
class servicoPrevio(depositoPrevio): 
    def __init__(self,cod_deposito,cod_servico,descricao_servico,data_registro,data_entrega,user_inicio,user_fim,realizacao,valor):
        self.cod_servico = cod_servico
        self.descricao_servico = descricao_servico
        self.data_registro = data_registro
        self.data_entrega = data_entrega
        self.user_inicio = user_inicio
        self.user_fim = user_fim
        self.realizacao = realizacao
        self.valor = valor
        self.cod_deposito = cod_deposito
      
        

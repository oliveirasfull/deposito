from app import db
from .deposito_previo import DepositoPrevio

class ServicoPrevio(db.Model):
    __tablename__ = 'servico_previo'
    id_servico_previo = db.Column(db.Integer(), primary_key=True)
    descricao_servico = db.Column(db.String(length=99))
    data_registro = db.Column(db.DateTime())
    data_entrega = db.Column(db.DateTime())
    user_inicio = db.Column(db.String(length=45))
    user_fim = db.Column(db.String(length=45))
    relaizado = db.Column(db.Boolean)
    horario = db.Column(db.DateTime())
    id_deposito_previo = db.Column(db.Integer, db.ForeignKey('deposito_previo.id_deposito_previo'))
    deposito_previo = db.relationship('DepositoPrevio', back_populates='servico_previo')

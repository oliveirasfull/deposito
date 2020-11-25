from app import db
from .usuario import Usuario


class DepositoPrevio(db.Model):
    __tablename__ = 'deposito_previo'
    id_deposito_previo = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(length=20))
    nome_solicitante = db.Column(db.String(length=50))
    tipo_documento = db.Column(db.String(length=99))
    criador = db.Column(db.String(length=45))
    data_criacao = db.Column(db.DateTime(), default='now()')
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
    usuario = db.relationship('Usuario', back_populates="deposito_previo")
    servico_previo = db.relationship('ServicoPrevio', back_populates='deposito_previo')

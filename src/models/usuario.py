from app import db


class Usuario(db.Model):
    __tablename__ = 'usuario'
    id_usuario = db.Column(db.Integer(), primary_key=True)
    nome = db.Column(db.String(length=45))
    password = db.Column(db.String(length=45))

    deposito_previo = db.relationship('DepositoPrevio', back_populates='usuario')


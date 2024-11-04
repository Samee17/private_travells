# models.py
from app import db


class Driver(db.Model):
    __tablename__ = 'drivers'

    license = db.Column(db.String(10), primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email_id = db.Column(db.String(100), nullable=False, unique=True)
    address = db.Column(db.String(150), nullable=False)

    def __init__(self, license, first_name, last_name, email_id, address):
        self.license = license
        self.first_name = first_name
        self.last_name = last_name
        self.email_id = email_id
        self.address = address

    def to_dict(self):
        return {
            'license': self.license,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email_id': self.email_id,
            'address': self.address
        }

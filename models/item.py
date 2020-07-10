from datetime import datetime

from db import db


class ItemModel(db.Model):

    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(80))
    category = db.Column(db.String(80))
    city = db.Column(db.String(80))
    picture = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    description = db.Column(db.String(200))
    phone_number = db.Column(db.String(12))
    created_at = db.Column(db.DateTime, default=datetime.utcnow())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    users = db.relationship('UserModel')

    def __init__(self, user_id, item_name, category, city, phone_number):
        self.user_id = user_id
        self.item_name = item_name
        self.category = category
        self.city = city
        self.phone_number = phone_number

    def json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'item_name': self.item_name,
            'category': self.category,
            'city': self.city,
            'picture': self.picture,
            'price': self.price,
            'description': self.description,
            'phone_number': self.phone_number,
            'created_at': self.created_at.isoformat()
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

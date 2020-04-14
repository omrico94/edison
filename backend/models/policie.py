from backend import db
import json

class Policie(db.Model):
    __tablename__ = 'policie'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    sensors = db.Column(db.Integer, nullable=True)
    activationTime = db.Column(db.DateTime(), nullable=False)
    status = db.Column(db.Boolean, nullable=False)

    def to_json(self):
        return json.dump(self, defualt=lambda obj: obj.__dict__, sort_keys=True, indent=4)

    def __repr__(self):
        return f"<Policie: id = {self.id}, title = {self.title}, " \
               f"sensors= {self.sensors}, username = {self.activationTime}, email = {self.status}>"

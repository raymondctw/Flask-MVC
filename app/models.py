from app import db

class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    role = db.Column(db.String(30), nullable=False)
    status = db.Column(db.String(30), nullable=False)

    __table_args__ = (
        db.UniqueConstraint('username', 'email', name='_username_email_uc'),
    )

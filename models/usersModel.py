from datetime import datetime
from sqlalchemy.sql import func
import hashlib
import random
from app import db

def acakid():
    random_number = str(random.randint(100,999))
    hash = hashlib.sha256(random_number.encode()).hexdigest()[:3]
    return hash


class User(db.Model):
    id = db.Column(db.String(3), primary_key=True, default=acakid)
    nama = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    nomer_telepon = db.Column(db.String(13), unique=True, nullable=False)
    alamat = db.Column(db.String(250))
    poin = db.Column(db.Float, default=0)
    img_profil = db.Column(db.String(250), default="default.png")
    role = db.Column(db.String(4), default="user")
    is_verified = db.Column(db.Boolean, default=False)
    verification_code = db.Column(db.String(6), nullable=True)
    verification_expiry = db.Column(db.DateTime, nullable=True)  
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=func.now()) 
    updated_at = db.Column(db.DateTime, default=func.now(), onupdate=func.now())  
    def ubahKejson(self):
        return {
            "id": self.id,
            "nama":self.nama,
            "email":self.email,
            "nomer_telepon": self.nomer_telepon,
            "alamat": self.alamat,
            "poin": self.poin,
            "img_profil": self.img_profil,
            "role": self.role,
            "is_verified": self.is_verified,
        }


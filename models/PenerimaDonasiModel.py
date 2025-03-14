
from app import db
from datetime import datetime
from sqlalchemy.sql import func
import hashlib
import random


def acakid():
    random_number = str(random.randint(100,999))
    hash = hashlib.sha256(random_number.encode()).hexdigest()[:3]
    return hash


class PenerimaDonasi(db.Model):    
    __tablename__ = 'penerima_donasi'
    id_penerima = db.Column(db.String(3), primary_key=True,default=lambda: acakid())
    nama = db.Column(db.String(255), nullable=False)
    kontak = db.Column(db.String(255), nullable=False)
    deskripsi = db.Column(db.String(255), nullable=False)
    alamat = db.Column(db.Text, nullable=True)
    latitude = db.Column(db.Text, nullable=True)
    longtitude = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=func.now()) 
    deleted_at = db.Column(db.DateTime, default=func.now()) 
    updated_at = db.Column(db.DateTime, default=func.now(), onupdate=func.now())  

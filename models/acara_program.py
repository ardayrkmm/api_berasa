from app import db
from datetime import datetime
from sqlalchemy.sql import func
import hashlib
import random


def acakid():
    random_number = str(random.randint(100,999))
    hash = hashlib.sha256(random_number.encode()).hexdigest()[:3]
    return hash


class AcaraProgram(db.Model):
    id_program = db.Column(db.String(3), primary_key=True, default=acakid)
    judul = db.Column(db.String(255), nullable=False)
    deskripsi = db.Column(db.Text, nullable=False)
    total_donasi = db.Column(db.BigInteger, default=0)
    alamat = db.Column(db.String(250))
    tanggal = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, nullable=True)
    

from app import db
from datetime import datetime
from sqlalchemy.sql import func
import hashlib
import random


def acakid():
    random_number = str(random.randint(100,999))
    hash = hashlib.sha256(random_number.encode()).hexdigest()[:3]
    return hash


class GaleriMakanan(db.Model):
    id_galerimakanan = db.Column(db.String(3), primary_key=True, default=acakid)
    url = db.Column(db.String(255), nullable=False)
    id_barang = db.Column(db.String(3), db.ForeignKey('barang_donasi.id_barang_donasi'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
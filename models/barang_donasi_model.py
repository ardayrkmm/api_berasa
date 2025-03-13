
from app import db
from datetime import datetime
from sqlalchemy.sql import func
import hashlib
import random


def acakid():
    random_number = str(random.randint(100,999))
    hash = hashlib.sha256(random_number.encode()).hexdigest()[:3]
    return hash

class BarangDonasi(db.Model):
    __tablename__ = 'barang_donasi'
    id_barang_donasi = db.Column(db.String(3), primary_key=True,default=lambda: acakid())
    nama_makanan = db.Column(db.String(255), nullable=False)
    deskripsi = db.Column(db.String(255), nullable=False)
    jumlah_porsi = db.Column(db.Integer, nullable=False)
    batas_waktu_konsumsi = db.Column(db.String(250), nullable=True)
    id_donasi = db.Column(db.String(3), db.ForeignKey('donasi.id_donasi'), nullable=False)
    id_jenis = db.Column(db.String(3), db.ForeignKey('jenis_makanan.id_jenis'), nullable=False)
    galeri_makanan = db.relationship('GaleriMakanan', backref='barang', lazy=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    jenis_makanan = db.relationship('JenisMakanan', backref='barang_donasi', lazy=True)

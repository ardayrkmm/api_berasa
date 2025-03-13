from app import db
from datetime import datetime
from sqlalchemy.sql import func
import hashlib
import random
from models.PenerimaDonasiModel import PenerimaDonasi
from models.acara_program import AcaraProgram


def acakid():
    random_number = str(random.randint(100, 999))
    hash_value = hashlib.sha256(random_number.encode()).hexdigest()[:3]
    return hash_value

class Donasi(db.Model):
    __tablename__ = 'donasi'  # Tambahkan nama tabel eksplisit
    
    id_donasi = db.Column(db.String(3), primary_key=True, default=lambda: acakid())  # Gunakan lambda agar dipanggil setiap insert
    nama = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(255), nullable=False)
    deskripsi = db.Column(db.String(255), nullable=False)
    tanggal = db.Column(db.DateTime, default=func.now(), nullable=False)

    id_user = db.Column(db.String(3), db.ForeignKey("user.id"), nullable=False)
    id_program = db.Column(db.String(3), db.ForeignKey("acara_program.id_program"), nullable=True)
    id_penerima = db.Column(db.String(3), db.ForeignKey("penerima_donasi.id_penerima"), nullable=True)

    created_at = db.Column(db.DateTime, default=func.now()) 
    updated_at = db.Column(db.DateTime, default=func.now(), onupdate=func.now())  

    barang_donasi = db.relationship('BarangDonasi', backref='donasi', lazy=True)
    penerima = db.relationship(PenerimaDonasi, backref='penerima_donasi', lazy=True)
    acara_program = db.relationship(AcaraProgram, backref='acara_program', lazy=True)

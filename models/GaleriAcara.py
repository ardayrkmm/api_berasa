from app import db
import uuid
from datetime import datetime

class GaleriGambarAcara(db.Model):
    id_galeri = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    id_program = db.Column(db.String(36), db.ForeignKey('acara_program.id_program'), nullable=False)
    url_gambar = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, nullable=True)

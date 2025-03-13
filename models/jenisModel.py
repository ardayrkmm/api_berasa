from datetime import datetime
from sqlalchemy.sql import func
import hashlib
import random
from app import db
def acakid():
    random_number = str(random.randint(100,999))
    hash = hashlib.sha256(random_number.encode()).hexdigest()[:3]
    return hash

class JenisMakanan(db.Model):
    __tablename__ = 'jenis_makanan'

    id_jenis = db.Column(db.String(3), primary_key=True, default=acakid)
    nama_jenis = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime)
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
    nama_program = db.Column(db.String(255), nullable=False)

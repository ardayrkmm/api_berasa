import os
import uuid
from datetime import datetime
from flask import request, jsonify, current_app
from app import bcrypt, db, mail
from models.acara_program import AcaraProgram
from models.GaleriAcara import GaleriGambarAcara
from werkzeug.utils import secure_filename

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

def save_file(file):
    if file and allowed_file(file.filename):
        filename = f"{uuid.uuid4()}.{file.filename.rsplit('.', 1)[1].lower()}"
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return filename
    return None

def add_acara():
    data = request.form
    files = request.files.getlist('gambar')

    acara = AcaraProgram(
        judul=data['judul'],
        deskripsi=data['deskripsi'],
        total_donasi=int(data.get('total_donasi', 0)),
        alamat=data['alamat'],
        tanggal=datetime.strptime(data['tanggal'], '%Y-%m-%d')
    )
    db.session.add(acara)
    db.session.commit()

    # Simpan gambar ke tabel galeri
    for file in files:
        if file and allowed_file(file.filename):
            filename = save_file(file)
            if filename:
                galeri = GaleriGambarAcara(id_program=acara.id_program, url_gambar=filename)
                db.session.add(galeri)

    db.session.commit()
    return jsonify({'message': 'Acara berhasil ditambahkan'}), 201

def get_acara(id_acara):
    acara = AcaraProgram.query.get(id_acara)
    if not acara:
        return jsonify({'message': 'Acara tidak ditemukan'}), 404

    galeri = GaleriGambarAcara.query.filter_by(id_acara=id_acara).all()
    gambar_list = [g.url_gambar for g in galeri]

    return jsonify({
        'id_acara': acara.id_acara,
        'judul': acara.judul,
        'deskripsi': acara.deskripsi,
        'total_donasi': acara.total_donasi,
        'alamat': acara.alamat,
        'tanggal': str(acara.tanggal),
        'gambar': gambar_list,
        'created_at': str(acara.created_at),
        'updated_at': str(acara.updated_at)
    })

def delete_acara(id_acara):
    acara = AcaraProgram.query.get(id_acara)
    if not acara:
        return jsonify({'message': 'Acara tidak ditemukan'}), 404

    # Tandai acara dan gambar sebagai terhapus
    acara.deleted_at = datetime.utcnow()
    GaleriGambarAcara.query.filter_by(id_acara=id_acara).update({'deleted_at': datetime.utcnow()})
    db.session.commit()

    return jsonify({'message': 'Acara berhasil dihapus'}), 200

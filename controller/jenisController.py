import uuid
from flask import jsonify, request
from app import db
from models.jenisModel import JenisMakanan


def tambah():
    data = request.get_json()
    jenis_baru = JenisMakanan(
        
        nama_jenis=data['nama_jenis'],
    )
    db.session.add(jenis_baru)
    db.session.commit()
    return jsonify({'message': 'Jenis makanan berhasil ditambahkan'}), 201


def baca():
    jenis_makanan = JenisMakanan.query.all()
    hasil = [
        {
            'id_jenis': jm.id_jenis,
            'nama_jenis': jm.nama_jenis,
        } for jm in jenis_makanan
    ]
    return jsonify(hasil), 200


def edit(id_jenis):
    data = request.get_json()
    jenis_makanan = JenisMakanan.query.get_or_404(id_jenis)
    jenis_makanan.nama_jenis = data['nama_jenis']
    db.session.commit()
    return jsonify({'message': 'Jenis makanan berhasil diperbarui'}), 200


def hapus(id_jenis):
    jenis_makanan = JenisMakanan.query.get_or_404(id_jenis)
    db.session.delete(jenis_makanan)
    db.session.commit()
    return jsonify({'message': 'Jenis makanan berhasil dihapus'}), 200
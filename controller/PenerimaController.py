from flask import request, jsonify
from models.PenerimaDonasiModel import PenerimaDonasi
from app import db
from sqlalchemy.sql import func

def tambah():
    try:
        data = request.get_json()
        penerima_baru = PenerimaDonasi(
            nama=data.get("nama"),
            kontak=data.get("kontak"),
            deskripsi=data.get("deskripsi"),
            alamat=data.get("alamat"),
            latitude=data.get("latitude"),
            longtitude=data.get("longtitude"),
        )
        db.session.add(penerima_baru)
        db.session.commit()

        return jsonify({"message": "Penerima donasi berhasil ditambahkan", "id_penerima": penerima_baru.id_penerima}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def baca():
    penerima_list = PenerimaDonasi.query.all()
    result = [
        {
            "id_penerima": penerima.id_penerima,
            "nama": penerima.nama,
            "kontak": penerima.kontak,
            "deskripsi": penerima.deskripsi,
            "alamat": penerima.alamat,
            "latitude": penerima.latitude,
            "longtitude": penerima.longtitude,
            "created_at": penerima.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": penerima.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
        }
        for penerima in penerima_list
    ]
    return jsonify(result), 200

def bacaTiapId(id_penerima):
    penerima = PenerimaDonasi.query.get(id_penerima)
    if not penerima or penerima.deleted_at is not None:
        return jsonify({"error": "Penerima donasi tidak ditemukan"}), 404

    return jsonify({
        "id_penerima": penerima.id_penerima,
        "nama": penerima.nama,
        "kontak": penerima.kontak,
        "deskripsi": penerima.deskripsi,
        "alamat": penerima.alamat,
        "latitude": penerima.latitude,
        "longtitude": penerima.longtitude,
        "created_at": penerima.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        "updated_at": penerima.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
    }), 200

def update(id_penerima):
    penerima = PenerimaDonasi.query.get(id_penerima)
    if not penerima or penerima.deleted_at is not None:
        return jsonify({"error": "Penerima donasi tidak ditemukan"}), 404

    try:
        data = request.get_json()
        penerima.nama = data.get("nama", penerima.nama)
        penerima.kontak = data.get("kontak", penerima.kontak)
        penerima.deskripsi = data.get("deskripsi", penerima.deskripsi)
        penerima.alamat = data.get("alamat", penerima.alamat)
        penerima.latitude = data.get("latitude", penerima.latitude)
        penerima.longtitude = data.get("longtitude", penerima.longtitude)

        db.session.commit()
        return jsonify({"message": "Penerima donasi berhasil diperbarui"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def hapus(id_penerima):
    penerima = PenerimaDonasi.query.get(id_penerima)
    if not penerima or penerima.deleted_at is not None:
        return jsonify({"error": "Penerima donasi tidak ditemukan"}), 404

    try:
        penerima.deleted_at = func.now()
        db.session.commit()
        return jsonify({"message": "Penerima donasi berhasil dihapus"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


from flask import jsonify, request
import jwt
from datetime import datetime
from app import db
from models.jenisModel import JenisMakanan
import os,json
from werkzeug.utils import secure_filename
from models.DonasiModel import Donasi 
from models.barang_donasi_model import BarangDonasi  
from models.GaleriMakananModel import GaleriMakanan
from models.usersModel import User 

SECRET_KEY = "modriks"  
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_current_user():
    auth_header = request.headers.get("Authorization")
    print("Auth Header:", auth_header) 

    if not auth_header:
        return None

    try:
        token = auth_header.split(" ")[1]  
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        print("Decoded Token:", decoded_token) 
        return decoded_token.get("sub")
    except jwt.ExpiredSignatureError:
        print("JWT Error: Token Expired")
        return None
    except jwt.InvalidTokenError:
        print("JWT Error: Invalid Token")
        return None


# def tambah():
#     data = request.form.to_dict()  
#     files = request.files.getlist('galeri_makanan')  

#     nama = data.get('nama')
#     deskripsi = data.get('deskripsi')
#     alamat = data.get('alamat')
#     latitude = data.get("latitude")
#     longtitude = data.get("longtitude")
#     id_user = get_current_user()
    
#     if not id_user:
#         return jsonify({"error": "User not authenticated"}), 401

#     try:
#         user = User.query.get(id_user)
#         user.poin += 2
#         db.session.commit()

#         donasi_baru = Donasi(
#             nama=nama,
#             deskripsi=deskripsi,
#             id_user=id_user,
#             id_program=None,
#             alamat=alamat,
#             latitude=latitude,
#             longtitude=longtitude,
#             status=data.get("status", "Proses"),
#             tanggal=datetime.now(),
#             id_penerima=None,
#             created_at=datetime.now(),
#             updated_at=datetime.now()
#         )
        
#         db.session.add(donasi_baru)
#         db.session.flush()  

#         id_donasi = donasi_baru.id_donasi
#         barang_donasi_list = []

#         for barang in eval(data.get("barang_donasi", "[]")):
#             barang_obj = BarangDonasi(
#                 id_donasi=id_donasi,
#                 nama_makanan=barang.get("nama_makanan"),
#                 id_jenis=barang.get("id_jenis"),
#                 jumlah_porsi=barang.get("jumlah_porsi"),
#                 deskripsi=barang.get("deskripsi"),
#                 batas_waktu_konsumsi=barang.get("batas_waktu_konsumsi"),
#                 created_at=datetime.now(),
#                 updated_at=datetime.now()
#             )
#             db.session.add(barang_obj)
#             db.session.flush()

#             galeri_list = []
#             for file in files:
#                 if file and allowed_file(file.filename):
#                     filename = secure_filename(file.filename)
#                     file_path = os.path.join(UPLOAD_FOLDER, filename)
#                     file.save(file_path)

#                     galeri_obj = GaleriMakanan(
#                         id_barang=barang_obj.id_barang_donasi,
#                         url=file_path,
#                         created_at=datetime.now(),
#                         updated_at=datetime.now()
#                     )
#                     db.session.add(galeri_obj)
#                     galeri_list.append({"id_barang": barang_obj.id_barang_donasi, "url": file_path})

#             barang_donasi_list.append({
#                 "id_barang_donasi": barang_obj.id_barang_donasi,
#                 "nama_makanan": barang_obj.nama_makanan,
#                 "id_jenis": barang_obj.id_jenis,
#                 "jumlah_porsi": barang_obj.jumlah_porsi,
#                 "deskripsi": barang_obj.deskripsi,
#                 "batas_waktu_konsumsi": barang_obj.batas_waktu_konsumsi,
#                 "galeri_makanan": galeri_list
#             })

#         db.session.commit()  

#         response_data = {
#             "message": "Donasi berhasil ditambahkan",
#             "data": {
#                 "id_donasi": id_donasi,
#                 "nama": donasi_baru.nama,
#                 "deskripsi": donasi_baru.deskripsi,
#                 "id_user": donasi_baru.id_user,
#                 "status": donasi_baru.status,
#                 "tanggal": donasi_baru.tanggal.strftime("%Y-%m-%d %H:%M:%S"),
#                 "barang_donasi": barang_donasi_list
#             }
#         }

#         return jsonify(response_data), 201

#     except Exception as e:
#         db.session.rollback()
#         return jsonify({"error": str(e)}), 500
# def tambah():
#     data = request.form.to_dict()
#     files = request.files.getlist('galeri_makanan')

#     nama = data.get('nama')
#     deskripsi = data.get('deskripsi')
#     alamat = data.get('alamat')
#     latitude = data.get("latitude")
#     longitude = data.get("longitude")
#     id_user = get_current_user()
    
#     if not id_user:
#         return jsonify({"error": "User not authenticated"}), 401

#     try:
#         user = User.query.get(id_user)
#         user.poin += 2
#         db.session.commit()

#         donasi_baru = Donasi(
#             nama=nama,
#             deskripsi=deskripsi,
#             id_user=id_user,
#             alamat=alamat,
#             latitude=latitude,
#             longitude=longitude,
#             status=data.get("status", "Proses"),
#             tanggal=datetime.now(),
#             created_at=datetime.now(),
#             updated_at=datetime.now()
#         )
        
#         db.session.add(donasi_baru)
#         db.session.flush()
#         id_donasi = donasi_baru.id_donasi

#         barang_donasi_list = []

#         for barang in eval(data.get("barang_donasi", "[]")):
#             barang_obj = BarangDonasi(
#                 id_donasi=id_donasi,
#                 nama_makanan=barang.get("nama_makanan"),
#                 id_jenis=barang.get("id_jenis"),
#                 jumlah_porsi=barang.get("jumlah_porsi"),
#                 deskripsi=barang.get("deskripsi"),
#                 batas_waktu_konsumsi=barang.get("batas_waktu_konsumsi"),
#                 created_at=datetime.now(),
#                 updated_at=datetime.now()
#             )
#             db.session.add(barang_obj)
#             db.session.flush()
#             db.session.refresh(barang_obj) 
#             galeri_list = []
#             for file in files:
#                 if file and allowed_file(file.filename):
#                     filename = secure_filename(file.filename)
#                     file_path = os.path.join(UPLOAD_FOLDER, filename)
#                     file.save(file_path)
#                     file_url = f"/static/uploads/{filename}"

#                     galeri_obj = GaleriMakanan(
#                         id_barang=barang_obj.id_barang_donasi,
#                         url=file_url,
#                         created_at=datetime.now(),
#                         updated_at=datetime.now()
#                     )
#                     db.session.add(galeri_obj)
#                     galeri_list.append({"id_barang": barang_obj.id_barang_donasi, "url": file_url})

#             barang_donasi_list.append({
#                 "id_barang_donasi": barang_obj.id_barang_donasi,
#                 "nama_makanan": barang_obj.nama_makanan,
#                 "id_jenis": barang_obj.id_jenis,
#                 "jumlah_porsi": barang_obj.jumlah_porsi,
#                 "deskripsi": barang_obj.deskripsi,
#                 "batas_waktu_konsumsi": barang_obj.batas_waktu_konsumsi,
#                 "galeri_makanan": galeri_list
#             })

#         db.session.commit()

#         response_data = {
#             "message": "Donasi berhasil ditambahkan",
#             "data": {
#                 "id_donasi": id_donasi,
#                 "nama": donasi_baru.nama,
#                 "deskripsi": donasi_baru.deskripsi,
#                 "id_user": donasi_baru.id_user,
#                 "status": donasi_baru.status,
#                 "tanggal": donasi_baru.tanggal.strftime("%Y-%m-%d %H:%M:%S"),
#                 "barang_donasi": barang_donasi_list
#             }
#         }

#         return jsonify(response_data), 201

#     except Exception as e:
#         db.session.rollback()
#         return jsonify({"error": str(e)}), 500
def tambah():
    data = request.form.to_dict()
    files = request.files  # semua file akan dimapping dari field yang bernama galeri_makanan_0[], galeri_makanan_1[] dst

    nama = data.get('nama')
    deskripsi = data.get('deskripsi')
    alamat = data.get('alamat')
    latitude = data.get("latitude")
    longitude = data.get("longitude")
    id_user = get_current_user()

    if not id_user:
        return jsonify({"error": "User not authenticated"}), 401

    try:
        # Tambahkan poin ke user
        user = User.query.get(id_user)
        if user:
            user.poin += 2
            db.session.commit()

        # Buat Donasi
        donasi_baru = Donasi(
            nama=nama,
            deskripsi=deskripsi,
            id_user=id_user,
            alamat=alamat,
            latitude=latitude,
            longitude=longitude,
            status=data.get("status", "Proses"),
            tanggal=datetime.now(),
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        db.session.add(donasi_baru)
        db.session.flush()
        id_donasi = donasi_baru.id_donasi

        barang_donasi_list = []

        # Barang Donasi dan Galeri
        barang_donasi_raw = json.loads(data.get("barang_donasi", "[]"))
        for index, barang in enumerate(barang_donasi_raw):
            barang_obj = BarangDonasi(
                id_donasi=id_donasi,
                nama_makanan=barang.get("nama_makanan"),
                id_jenis=barang.get("id_jenis"),
                jumlah_porsi=barang.get("jumlah_porsi"),
                deskripsi=barang.get("deskripsi"),
                batas_waktu_konsumsi=barang.get("batas_waktu_konsumsi"),
                created_at=datetime.now(),
                updated_at=datetime.now()
            )
            db.session.add(barang_obj)
            db.session.flush()
            db.session.refresh(barang_obj)

            galeri_list = []

           
            galeri_key = f'galeri_makanan_{index}'
            file_list = request.files.getlist(galeri_key)
            
            print(f"[DEBUG] Cek file key: {galeri_key}")
            print(f"[DEBUG] Dapet file list: {file_list}")

            for file in file_list:
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file_path = os.path.join(UPLOAD_FOLDER, filename)
                    file.save(file_path)
                    file_url = f"/static/uploads/{filename}"

                    galeri_obj = GaleriMakanan(
                        id_barang=barang_obj.id_barang_donasi,
                        url=file_url,
                        created_at=datetime.now(),
                        updated_at=datetime.now()
                    )
                    db.session.add(galeri_obj)

                    galeri_list.append({
                        "id_barang": barang_obj.id_barang_donasi,
                        "url": file_url
                    })

            barang_donasi_list.append({
                "id_barang_donasi": barang_obj.id_barang_donasi,
                "nama_makanan": barang_obj.nama_makanan,
                "id_jenis": barang_obj.id_jenis,
                "jumlah_porsi": barang_obj.jumlah_porsi,
                "deskripsi": barang_obj.deskripsi,
                "batas_waktu_konsumsi": barang_obj.batas_waktu_konsumsi,
                "galeri_makanan": galeri_list
            })

        db.session.commit()

        return jsonify({
            "message": "Donasi berhasil ditambahkan",
            "data": {
                "id_donasi": id_donasi,
                "nama": donasi_baru.nama,
                "deskripsi": donasi_baru.deskripsi,
                "status": donasi_baru.status,
                "tanggal": donasi_baru.tanggal.strftime("%Y-%m-%d %H:%M:%S"),
                "barang_donasi": barang_donasi_list
            }
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
def baca():
    donasi_list = Donasi.query.all()
    result = []

    for donasi in donasi_list:
        barang_donasi = BarangDonasi.query.filter_by(id_donasi=donasi.id_donasi).all()
        barang_list = []

        for barang in barang_donasi:
            galeri_makanan = GaleriMakanan.query.filter_by(id_barang=barang.id_barang_donasi).all()
            galeri_list = [{"id_barang": galeri.id_barang, "url": galeri.url} for galeri in galeri_makanan]

            barang_list.append({
                "id_barang_donasi": barang.id_barang_donasi,
                "nama_makanan": barang.nama_makanan,
                "id_jenis": barang.id_jenis,
                "jumlah_porsi": barang.jumlah_porsi,
                "deskripsi": barang.deskripsi,
                "batas_waktu_konsumsi": barang.batas_waktu_konsumsi,
                "galeri_makanan": galeri_list
            })

        result.append({
            "id_donasi": donasi.id_donasi,
            "nama": donasi.nama,
            "deskripsi": donasi.deskripsi,
            "id_user": donasi.id_user,
            "status": donasi.status,
            "tanggal": donasi.tanggal.strftime("%Y-%m-%d %H:%M:%S"),
            "barang_donasi": barang_list
        })

    return jsonify({"message": "Data Donasi", "data": result}), 200


def update(id_donasi):
    data = request.get_json()
    donasi = Donasi.query.get(id_donasi)

    if not donasi:
        return jsonify({"error": "Donasi tidak ditemukan"}), 404

    donasi.nama = data.get("nama", donasi.nama)
    donasi.deskripsi = data.get("deskripsi", donasi.deskripsi)
    donasi.status = data.get("status", donasi.status)
    donasi.updated_at = datetime.now()

    db.session.commit()

    return jsonify({"message": "Donasi berhasil diperbarui", "data": {
        "id_donasi": donasi.id_donasi,
        "nama": donasi.nama,
        "deskripsi": donasi.deskripsi,
        "status": donasi.status
    }}), 200

def delete_donasi(id_donasi):
    donasi = Donasi.query.get(id_donasi)

    if not donasi:
        return jsonify({"error": "Donasi tidak ditemukan"}), 404

    # Hapus barang donasi terkait
    barang_donasi = BarangDonasi.query.filter_by(id_donasi=id_donasi).all()
    for barang in barang_donasi:
        GaleriMakanan.query.filter_by(id_barang=barang.id_barang_donasi).delete()
        db.session.delete(barang)

    db.session.delete(donasi)
    db.session.commit()

    return jsonify({"message": "Donasi berhasil dihapus"}), 200


def riwayatDonasi():
    id_user = get_current_user()
    if not id_user:
        return jsonify({"error": "User not authenticated"}), 401
    
    try:
        status = request.args.get("status")
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 5))

        donasi_l = Donasi.query.filter_by(id_user=id_user)

        if status:
            donasi_l = Donasi.query.filter_by(status=status)
        
        pagination = donasi_l.order_by(Donasi.tanggal.desc()).paginate(page=page, per_page=limit, error_out=False)
        donasi_list = pagination.items

        hasil = []

        for donasi in donasi_list:
            barang_list = []
            for barang in BarangDonasi.query.filter_by(id_donasi=donasi.id_donasi).all():
                galeri = GaleriMakanan.query.filter_by(id_barang=barang.id_barang_donasi).all()
                galeri_urls = [g.url for g in galeri]

                barang_list.append({
                    "id_barang_donasi": barang.id_barang_donasi,
                    "nama_makanan": barang.nama_makanan,
                    "id_jenis": barang.id_jenis,
                    "jumlah_porsi": barang.jumlah_porsi,
                    "deskripsi": barang.deskripsi,
                    "batas_waktu_konsumsi": barang.batas_waktu_konsumsi,
                    "galeri_makanan": galeri_urls
                })

            hasil.append({
                "id_donasi": donasi.id_donasi,
                "nama": donasi.nama,
                "deskripsi": donasi.deskripsi,
                "alamat": donasi.alamat,
                "latitude": donasi.latitude,
                "longitude": donasi.longitude,
                "status": donasi.status,
                "tanggal": donasi.tanggal.strftime("%Y-%m-%d %H:%M:%S"),
                "barang_donasi": barang_list
            })

        return jsonify({
            "riwayat_donasi": hasil,
            "page": page,
            "limit": limit,
            "total": pagination.total,
            "pages": pagination.pages
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500



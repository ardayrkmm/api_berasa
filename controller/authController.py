from datetime import datetime,timedelta  
import random
from flask_bcrypt import generate_password_hash
from flask import jsonify, request
from flask_mail import Message
from flask_jwt_extended import create_access_token
from app import bcrypt, db, mail
from models.usersModel import User
from werkzeug.utils import secure_filename
import os
UPLOAD_FOLDER = 'static/profil'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def register():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data["password"]).decode("utf-8")
    verification_code = str(random.randint(100000, 999999))
    expiration_time = datetime.utcnow() + timedelta(seconds=600)  # Kode valid 30 detik

    new_user = User(
        nama=data["nama"],
        email=data["email"],
        password=hashed_password,
        nomer_telepon=data["nomer_telepon"],
        alamat=data.get("alamat", ""),
        verification_code=verification_code,
        verification_expiry=expiration_time,
        is_active=True,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    db.session.add(new_user)
    db.session.commit()

    msg = Message("Kode Verifikasi", sender="emailkamu@gmail.com", recipients=[data["email"]])
    msg.body = f"Kode verifikasi Anda: {verification_code}. Berlaku selama 30 detik."
    mail.send(msg)

    return jsonify({
        "message": "Selamat udah buat akun,silah cek email untuk verifikasi",
        "user": new_user.ubahKejson()
    }), 201




def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()

    if user and bcrypt.check_password_hash(user.password,data['password']):
        if not user.is_verified:
            return jsonify({"message": "Akun belum diverifikasi!, silahkan verifikasi dahulu ya"}), 403
        
        token = create_access_token(identity=user.id)
        return jsonify({"token": token, "user": user.ubahKejson()}), 200
    
    return jsonify({"message": "Email atau password salah!"}), 401


def verifikasiEmail():
    data = request.get_json()
    user = User.query.filter_by(email=data["email"], verification_code=data["code"]).first()

    if user:
        if datetime.utcnow() > user.verification_expiry:
            return jsonify({"message": "Kode verifikasi kadaluarsa!"}), 400

        user.is_verified = True
        user.verification_code = None
        user.verification_expiry = None
        user.updated_at = datetime.utcnow()
        db.session.commit()
        return jsonify({"message": "Akun berhasil diverifikasi"}), 200
    
    return jsonify({"message": "Kode verifikasi salah!"}), 400
def MintaRequestReset():
    data = request.get_json()
    user = User.query.filter_by(email=data["email"]).first()

    if user:
        reset_code = str(random.randint(100000, 999999))
        user.verification_code = reset_code
        user.verification_expiry = datetime.utcnow() + datetime.timedelta(minutes=5)  # Kode valid 5 menit
        db.session.commit()

        msg = Message("Reset Password Code", sender="emailkamu@gmail.com", recipients=[data["email"]])
        msg.body = f"Kode reset password Anda: {reset_code}. Berlaku selama 5 menit."
        mail.send(msg)

        return jsonify({"message": "Kode reset password dikirim ke email"}), 200
    
    return jsonify({"message": "Email tidak ditemukan!"}), 404

def kodeReset():
    data = request.get_json()
    user = User.query.filter_by(email=data["email"], verification_code=data["code"]).first()

    if user:
        if datetime.utcnow() > user.verification_expiry:
            return jsonify({"message": "Kode reset kadaluarsa!"}), 400
        return jsonify({"message": "Kode benar, silakan reset password"}), 200
    
    return jsonify({"message": "Kode salah!"}), 400

def ubahPassword():
    data = request.get_json()
    user = User.query.filter_by(email=data["email"], verification_code=data["code"]).first()

    if user:
        if datetime.utcnow() > user.verification_expiry:
            return jsonify({"message": "Kode reset kadaluarsa!"}), 400

        hashed_password = bcrypt.generate_password_hash(data["new_password"]).decode("utf-8")
        user.password = hashed_password
        user.verification_code = None
        user.verification_expiry = None
        user.updated_at = datetime.utcnow()
        db.session.commit()

        return jsonify({"message": "Password berhasil direset, silakan login"}), 200
    
    return jsonify({"message": "Kode salah!"}), 400




def update_user(user):
    data = request.form

    if "nama" in data:
        user.nama = data["nama"]
    if "email" in data:
        user.email = data["email"]
    if "nomer_telepon" in data:
        user.nomer_telepon = data["nomer_telepon"]
    if "alamat" in data:
        user.alamat = data["alamat"]

  
    if 'img_profil' in request.files:
        file = request.files['img_profil']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)
            user.img_profil = filename  

    db.session.commit()
    return jsonify({"message": "Profil berhasil diperbarui"}), 200

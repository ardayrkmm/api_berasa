from datetime import datetime,timedelta  
import random
from flask_bcrypt import generate_password_hash
from flask import jsonify, request
from flask_mail import Message
from flask_jwt_extended import create_access_token
from app import bcrypt, db, mail
from models.usersModel import User


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

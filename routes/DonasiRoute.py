from flask import Blueprint
from controller.donasiController import tambah,baca, riwayatDonasi

donasi_bp = Blueprint("donasi", __name__)

donasi_bp.route("/tambah", methods=["POST"])(tambah)
donasi_bp.route("/baca", methods=["GET"])(baca)
donasi_bp.route("/riwayat", methods=["GET"])(riwayatDonasi)


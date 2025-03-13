from flask import Blueprint
from controller.donasiController import tambah,baca

donasi_bp = Blueprint("donasi", __name__)

donasi_bp.route("/tambah", methods=["POST"])(tambah)
donasi_bp.route("/baca", methods=["GET"])(baca)


from flask import Blueprint
from controller.jenisController import tambah, hapus, edit, baca

jenis_bp = Blueprint("jenis", __name__)

jenis_bp.route("/tambah", methods=["POST"])(tambah)
jenis_bp.route("/hapus", methods=["DELETE"])(hapus)
jenis_bp.route("/edit", methods=["UPDATE"])(edit)
jenis_bp.route("/baca", methods=["GET"])(baca)

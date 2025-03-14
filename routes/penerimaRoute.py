from flask import Blueprint
from controller.PenerimaController import baca, bacaTiapId, hapus, tambah, update

penerima_bp = Blueprint("penerima_bp", __name__)

penerima_bp.route("/tambah", methods=["POST"])(tambah)
penerima_bp.route("/baca", methods=["GET"])(baca)
penerima_bp.route("/bacaId/<id_penerima>", methods=["GET"])(bacaTiapId)
penerima_bp.route("/update/<id_penerima>", methods=["PUT"])(update)
penerima_bp.route("/hapus/<id_penerima>", methods=["DELETE"])(hapus)

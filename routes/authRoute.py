from flask import Blueprint
from controller.authController import register, login, verifikasiEmail, ubahPassword,MintaRequestReset, kodeReset, update_user

auth_bp = Blueprint("auth", __name__)

auth_bp.route("/register", methods=["POST"])(register)
auth_bp.route("/verify-email", methods=["POST"])(verifikasiEmail)
auth_bp.route("/login", methods=["POST"])(login)
auth_bp.route("/mintaKode", methods=["POST"])(MintaRequestReset)
auth_bp.route("/kodeVerifikasi", methods=["POST"])(kodeReset)
auth_bp.route("/resetpassword", methods=["POST"])(ubahPassword)
auth_bp.route("/updateProfil", methods=["PUT"])(update_user)

# ⚙️ Berasa API - Backend System

**Berasa API** adalah sistem backend berbasis RESTful API yang mengelola seluruh logika bisnis dan data untuk aplikasi **Berasa (Berbagi Rasa)**. Dibangun menggunakan framework Flask, API ini bertanggung jawab atas manajemen pengguna, pengolahan data donasi, tracking transparansi, dan kalkulasi lokasi terdekat.

---

## ✨ Fitur Backend

* **🔐 Authentication & Authorization**: Sistem login dan manajemen hak akses menggunakan JWT (JSON Web Token).
* **📦 Donation Management**: Endpoint untuk membuat, memperbarui, dan mengelola status donasi makanan.
* **🕵️ Transparency Tracking**: Sistem pencatatan riwayat (log) setiap perubahan status donasi untuk menjamin akuntabilitas.
* **📍 Geolocation Service**: Endpoint untuk menghitung jarak antara lokasi donatur dengan titik penerima donasi terdekat menggunakan rumus *Haversine*.
* **📊 Data Reporting**: Menyediakan data statistik donasi yang berhasil tersalurkan.

---

## 🛠️ Teknologi yang Digunakan

* **Language**: [Python](https://www.python.org/)
* **Framework**: [Flask](https://flask.palletsprojects.com/)
* **Database**: MySQL / PostgreSQL
* **ORM**: [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/) (Untuk manajemen database)
* **Authentication**: PyJWT
* **Documentation**: Postman / Swagger

---

## 🚀 Cara Menjalankan API Secara Lokal

1.  **Clone repository**:
    ```bash
    git clone [https://github.com/ardayrkmm/berasa-api.git](https://github.com/ardayrkmm/berasa-api.git)
    ```
2.  **Masuk ke folder proyek**:
    ```bash
    cd berasa-api
    ```
3.  **Buat Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    ```
4.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
5.  **Konfigurasi Database**:
    Sesuaikan `config.py` atau `.env` dengan kredensial database Anda.
6.  **Jalankan API**:
    ```bash
    python app.py
    ```

---

## 👤 Developer

Proyek backend ini dikembangkan sepenuhnya secara mandiri oleh:

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/ardayrkmm">
        <img src="https://github.com/ardayrkmm.png" width="100px;" alt="Arda"/><br />
        <sub><b>Arda</b></sub>
      </a>
    </td>
  </tr>
</table>

---

## 🎯 Tujuan Pengembangan

* Membangun sistem backend yang scalable untuk mendukung aplikasi mobile Berasa.
* Memastikan keamanan data donatur dan penerima donasi.
* Mengimplementasikan REST API yang rapi sesuai standar industri.

---

## 📄 Lisensi

Proyek ini dibuat untuk keperluan **edukasi dan pengembangan**. Penggunaan dan modifikasi diperbolehkan dengan mencantumkan sumber.

# ⚙️ Berasa API – Backend System

**Berasa API** is a RESTful backend system that manages all business logic and data for the **Berasa (Berbagi Rasa)** application. Built using the Flask framework, this API is responsible for user management, donation data processing, transparency tracking, and nearest-location calculations.

---

## ✨ Backend Features

* **🔐 Authentication & Authorization**: Login system and access control using JWT (JSON Web Token).
* **📦 Donation Management**: Endpoints to create, update, and manage the status of food donations.
* **🕵️ Transparency Tracking**: A logging system that records every change in donation status to ensure accountability.
* **📍 Geolocation Service**: Endpoints to calculate the distance between donor locations and the nearest donation recipient points using the *Haversine* formula.
* **📊 Data Reporting**: Provides statistical data on successfully distributed donations.

---

## 🛠️ Technologies Used

* **Language**: [Python](https://www.python.org/)
* **Framework**: [Flask](https://flask.palletsprojects.com/)
* **Database**: MySQL / PostgreSQL
* **ORM**: [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/) (For database management)
* **Authentication**: PyJWT
* **Documentation**: Postman / Swagger

---

## 🚀 How to Run the API Locally

1. **Clone the repository**:
    ```bash
    git clone https://github.com/ardayrkmm/berasa-api.git
    ```
2. **Navigate to the project folder**:
    ```bash
    cd berasa-api
    ```
3. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    ```
4. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
5. **Database Configuration**:
    Adjust `config.py` or `.env` with your database credentials.
6. **Run the API**:
    ```bash
    python app.py
    ```

---

## 👤 Developer

This backend project was fully developed independently by:

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

## 🎯 Development Objectives

* Build a scalable backend system to support the Berasa mobile application.
* Ensure data security for donors and donation recipients.
* Implement a clean, industry-standard REST API.

---

## 📄 License

This project was created for **educational and development** purposes. Use and modification are permitted with proper attribution.

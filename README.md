# 🌐 Website Si Panda - Sistem Informasi Hewan Dilindungi

**Si Panda Web** adalah platform berbasis browser yang dikembangkan menggunakan framework Flask. Website ini berfungsi sebagai pusat informasi, pemetaan, dan sistem pelaporan hewan dilindungi di Indonesia, dengan dukungan Kecerdasan Buatan (AI) untuk identifikasi spesies secara otomatis.

---

## ✨ Fitur Utama (Web Version)

* **🗺️ Interactive Conservation Map**: Peta interaktif menggunakan integrasi API untuk menunjukkan lokasi pusat konservasi dan taman nasional di seluruh Indonesia.
* **📢 Dashboard Lapor**: Sistem formulir pelaporan yang memungkinkan masyarakat mengunggah laporan pelanggaran terhadap satwa dilindungi.
* **🧠 AI Species Identification**: Fitur unggah foto di mana sistem akan memproses gambar menggunakan model **CNN (Convolutional Neural Network)** di sisi server untuk mengidentifikasi jenis hewan.
* **📖 Ensiklopedia Digital**: Katalog lengkap mengenai informasi, status kelangkaan, dan fakta unik hewan endemik Indonesia.

---

## 🛠️ Teknologi yang Digunakan

* **Backend**: [Flask (Python)](https://flask.palletsprojects.com/)
* **Frontend**: HTML5, CSS3, JavaScript (Bootstrap/Tailwind)
* **Artificial Intelligence**: [TensorFlow/Keras](https://www.tensorflow.org/) (Untuk implementasi Model CNN)
* **Database**: SQLite / PostgreSQL (Untuk menyimpan data laporan dan informasi hewan)
* **API**: REST API untuk komunikasi data dengan layanan eksternal.

---

## 🚀 Cara Menjalankan Website Secara Lokal

1.  **Clone repository**:
    ```bash
    git clone [https://github.com/username-kamu/si-panda-flask.git](https://github.com/username-kamu/si-panda-flask.git)
    ```
2.  **Masuk ke folder proyek**:
    ```bash
    cd si-panda-flask
    ```
3.  **Buat Virtual Environment (Opsional tapi disarankan)**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Untuk Linux/Mac
    venv\Scripts\activate     # Untuk Windows
    ```
4.  **Install Library yang dibutuhkan**:
    ```bash
    pip install -r requirements.txt
    ```
5.  **Jalankan Server Flask**:
    ```bash
    python app.py
    ```
6.  Buka browser dan akses `http://127.0.0.1:5000`.

---

## 👥 Contributors

Tim pengembang utama yang berkolaborasi dalam proyek website ini:

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/ardayrkmm">
        <img src="https://github.com/ardayrkmm.png" width="100px;" alt="Arda"/><br />
        <sub><b>Arda</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/gmcbjorjka">
        <img src="https://github.com/gmcbjorjka.png" width="100px;" alt="Teguh"/><br />
        <sub><b>Teguh</b></sub>
      </a>
    </td>
  </tr>
</table>

---

## 🎯 Tujuan Pengembangan Website

* Memanfaatkan framework Flask untuk integrasi model AI Python yang lebih *seamless*.
* Menyediakan platform edukasi publik mengenai kekayaan fauna Indonesia.
* Membangun sistem pelaporan berbasis web yang aman dan mudah digunakan.

---

## 📄 Lisensi

Proyek ini dibuat untuk keperluan **edukasi dan pengembangan**. Penggunaan dan modifikasi diperbolehkan dengan mencantumkan sumber asli proyek ini.

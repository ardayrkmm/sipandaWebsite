# 🌐 Si Panda Website – Protected Wildlife Information System

**Si Panda Web** is a browser-based platform developed using the Flask framework. This website serves as a central hub for information, mapping, and reporting of protected wildlife in Indonesia, with Artificial Intelligence (AI) support for automatic species identification.

---

## ✨ Key Features (Web Version)

* **🗺️ Interactive Conservation Map**: An interactive map using API integration to display the locations of conservation centers and national parks across Indonesia.
* **📢 Reporting Dashboard**: A reporting form system that allows the public to submit reports related to violations involving protected wildlife.
* **🧠 AI Species Identification**: A photo upload feature where the system processes images using a **CNN (Convolutional Neural Network)** model on the server side to identify animal species.
* **📖 Digital Encyclopedia**: A comprehensive catalog containing information, conservation status, and unique facts about Indonesia’s endemic wildlife.

---

## 🛠️ Technologies Used

* **Backend**: [Flask (Python)](https://flask.palletsprojects.com/)
* **Frontend**: HTML5, CSS3, JavaScript (Bootstrap/Tailwind)
* **Artificial Intelligence**: [TensorFlow/Keras](https://www.tensorflow.org/) (For CNN model implementation)
* **Database**: SQLite / PostgreSQL (For storing report data and wildlife information)
* **API**: REST API for data communication with external services.

---

## 🚀 How to Run the Website Locally

1. **Clone the repository**:
    ```bash
    git clone https://github.com/username-kamu/si-panda-flask.git
    ```
2. **Navigate to the project folder**:
    ```bash
    cd si-panda-flask
    ```
3. **Create a Virtual Environment (Optional but recommended)**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/Mac
    venv\Scripts\activate     # For Windows
    ```
4. **Install required libraries**:
    ```bash
    pip install -r requirements.txt
    ```
5. **Run the Flask server**:
    ```bash
    python app.py
    ```
6. Open a browser and access `http://127.0.0.1:5000`.

---

## 👥 Contributors

The core development team collaborating on this website project:

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

## 🎯 Website Development Objectives

* Utilize the Flask framework for seamless integration of Python-based AI models.
* Provide a public education platform highlighting Indonesia’s rich wildlife biodiversity.
* Build a secure and user-friendly web-based reporting system.

---

## 📄 License

This project was created for **educational and development** purposes. Use and modification are permitted with proper attribution to the original project.

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input
import numpy as np
import os
import logging
from PIL import Image

# Load model sekali di awal
MODEL_PATH = 'app/Controllers/deteksi3_kategorikal.h5'
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f'Model file tidak ditemukan di {MODEL_PATH}')
model = load_model(MODEL_PATH)  # Model di-cache

# Setup logging
logging.basicConfig(level=logging.INFO)

def crop_center(image_path, target_size=(224, 224)):
    """Crop the center part of the image to fit the target size."""
    img = Image.open(image_path)
    
    # Menghitung area crop dari tengah
    width, height = img.size
    target_width, target_height = target_size
    
    left = (width - target_width) / 2
    top = (height - target_height) / 2
    right = (width + target_width) / 2
    bottom = (height + target_height) / 2

    # Crop gambar dari tengah
    img = img.crop((left, top, right, bottom))
    
    # Convert image ke numpy array
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    return img_array

# def deteksi(file_path):
#     """
#     Memproses gambar dan melakukan prediksi menggunakan model yang telah dilatih.
#     """
#     input_size = (224, 224)

#     # Validasi format file
#     if not file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
#         raise ValueError("Format file tidak didukung. Harus PNG atau JPG.")

#     try:
#         # Preprocessing gambar
#         img = image.load_img(file_path, target_size=input_size)
#         img_array = image.img_to_array(img)
#         img_array = np.expand_dims(img_array, axis=0)
#         img_array /= 255.0
#     except Exception as e:
#         raise ValueError(f'Gagal memproses gambar: {str(e)}')

#     # Prediksi dengan model
#     try:
#         predictions = model.predict(img_array)

#         # Logika berdasarkan probabilitas tertinggi (confidence)
#         confidence = np.max(predictions)  # Ambil confidence tertinggi
#         predicted_class = "Dilindungi" if confidence >= 0.5 else "Tidak Dilindungi"

#         # Probabilitas untuk semua kelas
#         class_indices = {0: 'Tidak Dilindungi', 1: 'Dilindungi'}
#         probabilities = {class_indices[i]: float(pred) for i, pred in enumerate(predictions[0])}
#     except Exception as e:
#         raise ValueError(f'Hasil prediksi tidak valid: {str(e)}')

#     # Logging untuk debugging
#     logging.info(f'File: {file_path}, Confidence: {confidence}, Hasil: {predicted_class}, Probabilitas: {probabilities}')
#     return predicted_class, probabilities

species_info = {
     "Badak Jawa": {
        "status": "DILINDUNGI",
        "latin_name": "Rhinoceros sondaicus",
        "habitat": "Hutan hujan tropis di Jawa Barat",
        "description": "Badak Jawa adalah salah satu spesies badak yang paling terancam punah di dunia. Saat ini hanya ditemukan di Taman Nasional Ujung Kulon, Banten."
    },
    "Beruang madu": {
        "status": "DILINDUNGI",
        "latin_name": "Ursus malayanus",
        "habitat": "Hutan tropis di Asia Tenggara",
        "description": "Beruang madu adalah spesies beruang yang terancam punah, dengan ciri khas bulu leher yang berbentuk sabuk berwarna kuning keemasan."
    },
    "Burung Cendrawasih": {
        "status": "DILINDUNGI",
        "latin_name": "Paradisaeidae",
        "habitat": "Hutan hujan tropis Papua dan sekitarnya",
        "description": "Burung cendrawasih terkenal karena keindahan bulu-bulunya yang memukau, dan menjadi simbol keanekaragaman hayati Indonesia."
    },
    "Burung Maleo": {
        "status": "DILINDUNGI",
        "latin_name": "Macrocephalon maleo",
        "habitat": "Hutan tropis Sulawesi",
        "description": "Burung Maleo adalah spesies burung endemik Sulawesi yang terkenal dengan cara bertelurnya yang unik, yaitu dengan cara menanamkan telur ke dalam pasir panas."
    },
    "Harimau Sumatra": {
        "status": "DILINDUNGI",
        "latin_name": "Panthera tigris sumatrae",
        "habitat": "Hutan tropis Sumatra",
        "description": "Harimau Sumatra adalah subspesies harimau yang hanya ditemukan di pulau Sumatra dan saat ini terancam punah akibat perusakan habitat."
    },
    "Komodo": {
        "status": "DILINDUNGI",
        "latin_name": "Varanus komodoensis",
        "habitat": "Pulau Komodo, Flores, dan sekitarnya",
        "description": "Komodo adalah kadal terbesar di dunia yang hanya ditemukan di beberapa pulau di Indonesia. Spesies ini dikenal karena kekuatan dan kemampuan berburu yang luar biasa."
    },
    "Macan Tutul Jawa": {
        "status": "DILINDUNGI",
        "latin_name": "Panthera pardus melas",
        "habitat": "Hutan tropis di Jawa",
        "description": "Macan Tutul Jawa adalah subspesies harimau tutul yang hanya ditemukan di pulau Jawa, Indonesia, dan terancam punah karena perusakan habitat."
    },
    "Merak Hijau": {
        "status": "DILINDUNGI",
        "latin_name": "Pavo muticus",
        "habitat": "Hutan tropis Asia Tenggara",
        "description": "Merak Hijau adalah burung besar dengan bulu ekor yang indah, ditemukan di hutan tropis di Asia Tenggara, dan termasuk dalam spesies yang dilindungi."
    },
    "Orangutan Kalimantan": {
        "status": "DILINDUNGI",
        "latin_name": "Pongo pygmaeus",
        "habitat": "Hutan tropis Kalimantan",
        "description": "Orangutan Kalimantan adalah spesies primata yang hanya ditemukan di pulau Kalimantan. Mereka sangat terancam punah akibat deforestasi dan perburuan."
    },
    "Trenggiling": {
        "status": "DILINDUNGI",
        "latin_name": "Manis javanica",
        "habitat": "Hutan tropis di Asia Tenggara",
        "description": "Trenggiling adalah mamalia yang memiliki sisik keras dan sering diburu untuk perdagangan ilegal. Mereka termasuk dalam spesies yang dilindungi di banyak negara."
    },
    "Ayam": {
        "status": "TIDAK TERDAFTAR",
        "latin_name": "Gallus gallus domesticus",
        "habitat": "Di domestikasi di berbagai wilayah dunia",
        "description": "Ayam adalah hewan ternak yang sangat umum, dipelihara untuk diambil telurnya atau dagingnya."
    },
    "Burung Bangau": {
        "status": "TIDAK TERDAFTAR",
        "latin_name": "Grus grus",
        "habitat": "Dataran rendah dengan padang rumput atau rawa",
        "description": "Burung Bangau adalah burung besar yang ditemukan di Eropa dan Asia, dan biasanya hidup di kawasan rawa atau dataran rendah."
    },
    "Burung Perkutut": {
        "status": "TIDAK TERDAFTAR",
        "latin_name": "Geopelia striata",
        "habitat": "Area terbuka dengan semak-semak atau hutan kecil",
        "description": "Burung Perkutut adalah spesies burung kecil yang banyak dipelihara di Indonesia, dikenal karena suaranya yang merdu."
    },
    "Ikan Cupang": {
        "status": "TIDAK TERDAFTAR",
        "latin_name": "Betta splendens",
        "habitat": "Danau atau sungai kecil di Asia Tenggara",
        "description": "Ikan Cupang adalah ikan air tawar yang populer di kalangan penggemar akuarium karena warna yang cerah dan perilaku agresifnya."
    },
    "Ikan Koi": {
        "status": "TIDAK TERDAFTAR",
        "latin_name": "Cyprinus rubrofuscus",
        "habitat": "Kolam dan danau di Asia",
        "description": "Ikan Koi adalah jenis ikan hias yang berasal dari Jepang, dikenal dengan warna-warnanya yang cerah dan digunakan untuk memperindah taman atau kolam."
    },
    "Tokek": {
        "status": "TIDAK TERDAFTAR",
        "latin_name": "Gekko gecko",
        "habitat": "Pohon dan dinding rumah di daerah tropis",
        "description": "Tokek adalah jenis reptil yang banyak ditemukan di Asia Tenggara, dikenal karena suara khasnya yang keras dan kemampuannya untuk merayap di permukaan vertikal."
    },
    "Cicak": {
        "status": "TIDAK TERDAFTAR",
        "latin_name": "Lacertilia",
        "habitat": "Di dinding atau tanaman dalam rumah atau luar ruangan",
        "description": "Cicak adalah reptil kecil yang sering ditemukan di rumah atau gedung, dikenal karena kemampuan melompat dan menempel pada permukaan vertikal."
    },
    "Kambing": {
        "status": "TIDAK TERDAFTAR",
        "latin_name": "Capra aegagrus hircus",
        "habitat": "Berbagai habitat yang telah dibudidayakan oleh manusia",
        "description": "Kambing adalah hewan ternak yang sering digunakan untuk diambil daging, susu, dan kulitnya."
    },
    "Kerbau": {
        "status": "TIDAK TERDAFTAR",
        "latin_name": "Bubalus bubalis",
        "habitat": "Padang rumput dan daerah berair",
        "description": "Kerbau adalah hewan ternak yang banyak digunakan dalam pertanian, terutama untuk membajak sawah."
    },
    "Sapi": {
        "status": "TIDAK TERDAFTAR",
        "latin_name": "Bos taurus",
        "habitat": "Di domestikasi di berbagai wilayah dunia",
        "description": "Sapi adalah hewan ternak yang dipelihara untuk diambil daging, susu, dan kulitnya."
    }
}
class_names = list(species_info.keys())  # Daftar nama spesies

def deteksi(image_path):
    try:
        # 1. Load dan Preprocessing Gambar
        img = image.load_img(image_path, target_size=(224, 224))
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # 2. Prediksi Gambar
        predictions = model.predict(img_array)  # Hasil probabilitas
        predicted_class = np.argmax(predictions, axis=1)[0]

        # Validasi indeks prediksi dengan daftar class_names
        if predicted_class >= len(class_names):
            return {
                "error": "Predicted class index out of range.",
                "predicted_class_index": predicted_class
            }

        predicted_label = class_names[predicted_class]

        # 3. Ambil Informasi Spesies dari species_info
        species_data = species_info.get(predicted_label, {
            "status": "Tidak Diketahui",
            "latin_name": "Tidak Diketahui",
            "habitat": "Tidak Diketahui",
            "description": "Tidak ada deskripsi yang tersedia."
        })

        # 4. Hasil Output
        return {
            "predicted_label": predicted_label,
            "confidence": round(float(predictions[0][predicted_class]), 4),
            "species_info": species_data
        }

    except Exception as e:
        # Penanganan error jika ada masalah saat proses prediksi
        return {
            "error": str(e),
            "message": "Terjadi kesalahan saat memproses gambar."
        }
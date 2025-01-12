import os
import uuid
from flask import jsonify, render_template, request, redirect, url_for, flash, session, Blueprint
from flask_jwt_extended import jwt_required
from app import app
from werkzeug.utils import secure_filename
from app.Controllers.LaporController import delete_laporan_by_id, laporApiF, laporF, laporan_page, update_status, cobaUpdate
from app.Controllers.ScanController import deteksi
from app.Controllers.beritaController import BacaDataBerita, delete_berita_by_id, get_news, tambahBerita, updateBerita, detailBerita
from app.models import Comment, Lapor, User, HewanModel, BalaiKonservasi, Berita
from app.Controllers.Chatbot import chat
from app.Controllers.authController import data_user, delete_user_by_id, edit_pengguna, hapusakun, loginF, registerF, profilF,bacaUser, registerApi,loginApi, request_reset_password, reset_password,reset_password_api,req_api_pass, role_required, updateProfilApi
from app.Controllers.Balaikonservasi import BacaDataBalai, BacaDataBalaiApi, deleteBalaiKonservasi, detailBalai, editDatabalais,tambahDataBalai,balai_terdekat,halamanDataBalai, pencarianB
from app.Controllers.HewanController import bacaDataHewan,bacaDataHewanApi, cariDataHewanApi, deleteDataHewan,detailHewans, halamanDataHewan, tambahDataHewan, tambahDataHewanApi, ambilDataDariKategori, updateDataHewan
from app.Controllers.Kategori import buatKategori, bacaData,bacaDataApi, updateData, updateDataApi, deleteDataApi,deleteData
from app.Controllers.sentimenController import tambahKomen,tambahKomenApi

@app.route('/register', methods=['GET', 'POST'])
def register():
    return registerF()
@app.route('/api/register', methods=['POST'])
def registerApis():
    return registerApi()

@app.route('/api/chatbot', methods=['POST'])
def halamanChatApi():
    return chat()

@app.route('/api/login', methods=[ 'POST'])
def loginApis():
    return loginApi()

@app.route('/login', methods=['GET', 'POST'])
def login():
   return loginF()

@app.route('/profil', methods=['GET', 'POST'])
def profil():
    return profilF()

@app.route('/detailberita/<int:id_berita>', methods=['GET'])
def pindahHalamanBerita(id_berita):
    return detailBerita(id=id_berita)

@app.route('/logout')
def logout():
    session.clear()
    flash('Kamu telah logout.', 'success')
    return redirect(url_for('login'))

@app.route('/scan', methods=['GET', 'POST'])
def halamanScan():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Tidak ada file yang dipilih.', 'error')
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            flash('Nama file kosong.', 'error')
            return redirect(request.url)

        upload_folder = os.path.join(os.getcwd(), './app/static/uploads')
        os.makedirs(upload_folder, exist_ok=True)
        filename = f"{uuid.uuid4().hex}_{secure_filename(file.filename)}"
        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)
        
        try:
            result = deteksi(file_path)  
            
            session['result'] = {
                'image_path': filename,
                'predicted_label': result['predicted_label'],
                'confidence': result['confidence'],
                'species_info': result.get('species_info', None)
            }
        except Exception as e:
            flash(f'Error saat prediksi: {str(e)}', 'error')
            return redirect(request.url)

        # Redirect ke halaman hasil tanpa mengirim data melalui URL
        return redirect(url_for('halamanHasil'))

    return render_template('scan.html')

@app.route('/api/scan', methods=['GET', 'POST'])
def halamanScanApi():
    if 'file' not in request.files:
        return jsonify({'error': 'Tidak ada file yang dipilih.'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Nama file kosong.'}), 400

    try:
        # Buat folder untuk menyimpan file jika belum ada
        upload_folder = os.path.join(os.getcwd(), './app/static/uploads')
        os.makedirs(upload_folder, exist_ok=True)

        # Simpan file dengan nama unik
        filename = f"{uuid.uuid4().hex}_{secure_filename(file.filename)}"
        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)

        # Lakukan prediksi
        result = deteksi(file_path)  # Fungsi deteksi harus sudah didefinisikan

        # Format respons JSON
        response = {
            'image_path': f'/static/uploads/{filename}',  # URL untuk akses file
            'predicted_label': result['predicted_label'],
            'confidence': result['confidence'],
            'species_info': result.get('species_info', None)
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({'error': f'Error saat prediksi: {str(e)}'}), 500

@app.route('/api/komen', methods=['POST'])
def apiKomen():
    return tambahKomenApi()
@app.route('/api/hapusAkun/<int:id>', methods=['DELETE'])
def hapusAkunApi(id):
    return hapusakun(id)

@app.route('/hasil')
def halamanHasil():
    result = session.get('result')
    if not result:
        flash('Tidak ada hasil untuk ditampilkan.', 'error')
        return redirect(url_for('halamanScan'))
    file_url =result['image_path']
    return render_template('hasil.html', result=result, file_url=file_url)

# @app.route('/detailhewan/<string:id_hewan>',methods=['GET'])
# def pindahHalaman(id_hewan):
#     return detailHewans(id_hewan)

@app.route('/detailhewan/<string:id_hewan>', methods=['GET'])
def pindahHalaman(id_hewan):
    hewan = HewanModel.query.filter_by(id_hewan=id_hewan).first()
    
    if hewan is None:
        flash('Hewan tidak ditemukan', 'error')
        return redirect(url_for('halamanDataHewan')) 
    
    url_gambar = url_for('static', filename='gambarUser/' + hewan.url_gambar)
    
    return render_template('DetailHewan.html', hewans=hewan, url_gambar=url_gambar)

# @app.route('/detailbalai/<string:id_balaikonservasi>', methods=['GET'])
# def pindahHalamanBalai(id_balaikonservasi):
#     return detailBalai(id_balaikonservasi)

@app.route('/detailbalai/<string:id_balaikonservasi>', methods=['GET'])
def pindahHalamanBalai(id_balaikonservasi):
    balai = BalaiKonservasi.query.filter_by(id_balaikonservasi=id_balaikonservasi).first()
    
    if balai is None:
        flash('Balai Konservasi tidak ditemukan', 'error')
        return redirect(url_for('halamanDataBalai'))  
    
    url_gambar = url_for('static', filename='gambarUser/' + balai.gambarbalai)
    
    return render_template('detailbalai.html', balai=balai, url_gambar=url_gambar)

@app.route('/lapor', methods=['GET', 'POST'])
def lapor():
    return laporF()

@app.route('/api/lapor', methods=['POST'])
def laporApi():
    return laporApiF()

@app.route('/')
def home():
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        hewans = HewanModel.query.all()
        balais = BalaiKonservasi.query.all()
        news = get_news()
        return render_template('home.html', user=user, hewans=hewans, balais=balais, news=news)
    else:
        hewans = HewanModel.query.all()
        balais = BalaiKonservasi.query.all()
        news = get_news()
        return render_template('home.html', hewans=hewans, balais=balais, news=news)


@app.route('/admin')
@role_required(['super_admin', 'pihak_berwajib'])
def admin():
    positive_count = Comment.query.filter_by(sentiment="Positive").count()
    negative_count = Comment.query.filter_by(sentiment="Negative").count()

    # Ambil data komentar berdasarkan sentimen
    positive_comments = Comment.query.filter_by(sentiment="Positive").all()
    negative_comments = Comment.query.filter_by(sentiment="Negative").all()

    return render_template(
        './admin/pages/dashboard.html',
        positive=positive_count,
        negative=negative_count,
        positive_comments=positive_comments,
        negative_comments=negative_comments
    )


@app.route('/comment/add', methods=['POST'])
def komenTambah():
    return tambahKomen()
    
#route kategori Api
@app.route('/admin/api/kategori', methods=['GET'])
def kategoriApi():
    return bacaDataApi()
@app.route('/admin/kategori/tambah', methods=['GET','POST'])
@role_required(['super_admin', 'pihak_berwajib'])
def kategoriTambah():
    return buatKategori()
@app.route('/admin/kategori/delete/<string:id_kategori>', methods=['GET', 'DELETE'])
@role_required(['super_admin', 'pihak_berwajib'])
def hapusKategori(id_kategori):
    return deleteData(id_kategori)
@app.route('/admin/api/kategori/delete/<string:id_kategori>', methods=['DELETE'])
def hapusKategoriApi(id_kategori):
    return deleteDataApi(id_kategori)
@app.route('/admin/kategori/update/<string:id_kategori>', methods=['GET', 'POST'])
@role_required(['super_admin', 'pihak_berwajib'])
def kategoriUpdate(id_kategori):
    return updateData(id_kategori)
@app.route('/admin/api/kategori/update/<string:id_kategori>', methods=['GET', 'PUT'])
def kategoriUpdateApi(id_kategori):
    return updateDataApi(id_kategori)
@app.route('/admin/kategori')
@role_required(['super_admin', 'pihak_berwajib'])
def kategori():
    return bacaData()


#hewan
@app.route('/admin/hewan')
@role_required(['super_admin', 'pihak_berwajib'])
def hewan():
    return bacaDataHewan()
@app.route('/admin/api/hewan/kategori/<string:id_kategori>', methods=["GET"])
def hewanKategori(id_kategori):
    return ambilDataDariKategori(id_kategori)
@app.route('/admin/api/hewan', methods=['GET'])
def hewanApi():
    return bacaDataHewanApi()
@app.route('/admin/hewan/tambah',methods=['GET', 'POST'])
@role_required(['super_admin', 'pihak_berwajib'])
def tambahHewan():
    return tambahDataHewan()
@app.route('/admin/api/hewan/tambah',methods=['POST'])
def tambahHewanApi():
    return tambahDataHewanApi()

@app.route('/admin/hewan/edit/<string:id_hewan>', methods=['GET', 'POST'])
@role_required(['super_admin', 'pihak_berwajib'])
def editHewans(id_hewan):
    return updateDataHewan(id_hewan)

@app.route('/admin/hewan/delete/<string:id_hewan>', methods=['POST'])
@role_required(['super_admin', 'pihak_berwajib'])
def deleteHewan(id_hewan):
    return deleteDataHewan(id_hewan)

@app.route('/admin/hewan/cari', methods=['GET'])
@role_required(['super_admin', 'pihak_berwajib'])
def cari_hewan():
    return cariDataHewanApi()

@app.route('/admin/balaikonservasi')
@role_required(['super_admin', 'pihak_berwajib'])
def balaiKonservasi():
    return BacaDataBalai()

@app.route('/admin/api/balaikonservasi',  methods=['GET'])
def balaiKonservasiApi():
    return BacaDataBalaiApi()

@app.route('/admin/balaikonservasi/tambah', methods=['GET','POST'])
@role_required(['super_admin', 'pihak_berwajib'])
def tambahDatabalais():
    return tambahDataBalai()

@app.route('/admin/balaikonservasi/update/<string:id_balaikonservasi>', methods=['GET', 'POST'])
@role_required(['super_admin', 'pihak_berwajib'])
def editbalai(id_balaikonservasi):
    return editDatabalais(id_balaikonservasi)

@app.route('/admin/balaikonservasi/delete/<string:id_balaikonservasi>', methods=['POST'])
@role_required(['super_admin', 'pihak_berwajib'])
def deletebalai(id_balaikonservasi):
    return deleteBalaiKonservasi(id_balaikonservasi)

@app.route('/admin/api/bacauser', methods=['GET'])
def bcauserapi():
    return bacaUser()

#Laporan
@app.route('/admin/laporan')
@role_required(['super_admin', 'pihak_berwajib'])
def laporan():
    return laporan_page()

@app.route('/admin/laporan/delete/<int:laporan_id>', methods=['POST'])
def delete_laporan(laporan_id):
    return delete_laporan_by_id(laporan_id)

@app.route('/admin/update', methods=['POST'])
@role_required(['super_admin', 'pihak_berwajib'])
def update_status_route():
    return update_status()
@app.route('/update_status', methods=['POST'])
@role_required(['super_admin', 'pihak_berwajib'])
def update_status():
    return cobaUpdate()
@app.route('/reset-password', methods=['GET', 'POST'])
def requestResetPassword():
    return request_reset_password()

@app.route('/reset-password/<string:token>', methods=['GET', 'POST'])
def resetPassword(token):
    return reset_password(token)

@app.route('/cobahalaman', methods=['GET'])
def cobaBalais():
    return render_template('cobabalai.html')

@app.route('/HalamanDataBalai', methods=['GET'])
def dataHalaman():
    return halamanDataBalai()

@app.route('/HalamanDataHewan', methods=['GET'])
def halamanHewan():
    return halamanDataHewan()

@app.route('/api/pencarian/balai', methods=['GET'])
def pencarianDataBalai():
    return pencarianB()

@app.route('/api/pencarian/hewan', methods=['GET'])
def pencarianDataHewan():
    return cariDataHewanApi()

@app.route('/cobabalai', methods=['GET'])
def cobaBalai():
    return pencarianB()

@app.route('/api/token/resetpassword', methods=['POST'])
def mintaToken():
    return req_api_pass()

@app.route('/api/resetpassword', methods=['POST'])
def resetPassApi():
    return reset_password_api()
@app.route('/api/profil/update', methods=['POST'])
def updateProfilRes():
    return updateProfilApi()

@app.route('/api/chatbot/mobile', methods=['POST'])
def ApiChatbotMobile():
    return chat()


#berita
@app.route('/admin/berita', methods=['GET'])
def Berita():
    return BacaDataBerita()
@app.route('/admin/berita/tambah', methods=['GET', 'POST'])
def create_berita():
    return tambahBerita()
@app.route('/admin/berita/update/<int:berita_id>', methods=['GET', 'POST'])
def update_berita(berita_id):
    return updateBerita(berita_id)
@app.route('/admin/berita/delete/<int:berita_id>', methods=['POST'])
def delete_berita(berita_id):
    return delete_berita_by_id(berita_id)

#pengguna
@app.route('/admin/pengguna')
@role_required(['super_admin', 'pihak_berwajib'])
def pengguna():
    return data_user()
@app.route('/admin/pengguna/update/<int:user_id>', methods=['GET', 'POST'])
@role_required(['super_admin', 'pihak_berwajib'])
def editDataPengguna(user_id):
    return edit_pengguna(user_id)
@app.route('/admin/user/delete/<int:user_id>', methods=['POST'])
@role_required(['super_admin', 'pihak_berwajib'])
def delete_user(user_id):
    return delete_user_by_id(user_id)

@app.route('/chatbot')
def halamanChat():
    return render_template('chat.html')

@app.route('/lapor')
def halamanLapor():
    return render_template('lapor.html')
@app.route('/detail')
def halamanDetail():
    return render_template('detail.html')
from app import db,bcrypt
from datetime import date, datetime
from enum import Enum
import uuid

class StatusEnum(Enum):
    sedang_di_proses = "sedang_di_proses"
    selesai_di_proses = "selesai_di_proses"

class RoleEnum(Enum):
    user = "user"
    pihak_berwajib = "pihak_berwajib"
    super_admin = "super_admin"
    
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    nama = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, nullable=True)
    no_telp = db.Column(db.Integer(), unique=True)
    img_profil = db.Column(db.String(255), nullable=True)
    password = db.Column(db.String(255), unique=True, nullable=False)
    role = db.Column(db.Enum(RoleEnum), nullable=False, default=RoleEnum.user)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)  
    deleted_at = db.Column(db.DateTime, nullable=True)
    def tojson(self):
        return {
            "id": self.id,
            "nama": self.nama,
            
        }
    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
    def __repr__(self):
        return f"User('{self.email}', '{self.nama}','{self.role}')"

class cobabalai(db.Model):
    __tablename__ = 'cobabalai'
    id = db.Column(db.Integer, primary_key=True)
    nama_balai = db.Column(db.String(255))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    alamat = db.Column(db.Text)
    kontak = db.Column(db.String(100))


class HewanModel(db.Model):
    __tablename__ = 'hewan'
    id_hewan = db.Column(db.String(3), primary_key=True, default=lambda: str(uuid.uuid4())[:3])
    nama = db.Column(db.String(255), nullable=True)
    nama_latin = db.Column(db.String(255), nullable=True)
    deskripsi = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(20), nullable=True)
    populasi = db.Column(db.Integer, nullable=True)
    habitat = db.Column(db.String(255), nullable=True)
    url_gambar = db.Column(db.String(255), nullable=True)
    id_kategori = db.Column(db.String(1), db.ForeignKey('kategori.id_kategori'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, nullable=True)

    kategori = db.relationship("Kategori", back_populates="hewan")
    ciri_ciri = db.relationship("CiriCiriModel", back_populates="hewan", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id_hewan,
            "nama": self.nama,
            "nama_latin": self.nama_latin,
            "deskripsi": self.deskripsi,
            "status": self.status,
            "populasi": self.populasi,
            "habitat": self.habitat,
            "url_gambar": self.url_gambar,
            "kategori": self.kategori.to_dict() if self.kategori else None,
            "ciri_ciri": [ciri.to_dict() for ciri in self.ciri_ciri]  
        }

class CiriCiriModel(db.Model):
    __tablename__ = 'ciri_ciri'
    id_ciri =  db.Column(db.String(3), primary_key=True, default=lambda: str(uuid.uuid4())[:3])
    id_hewan = db.Column(db.String(3), db.ForeignKey('hewan.id_hewan'), nullable=False)
    ciri = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, nullable=True)
    hewan = db.relationship("HewanModel", back_populates="ciri_ciri")
    
    def to_dict(self):
        return {
            "id_ciri": self.id_ciri,
            "id_hewan": self.id_hewan,
            "ciri": self.ciri,
        }


class BalaiKonservasi(db.Model):
    __tablename__ = 'balaikonservasi'
    id_balaikonservasi = db.Column(db.String(3), primary_key=True,default=lambda: str(uuid.uuid4())[:3])
    nama_balai =db.Column(db.String(255), nullable=True)
    deskripsi =db.Column(db.String(255), nullable=True)
    provinsi =db.Column(db.String(255), nullable=True)
    gambarbalai =db.Column(db.String(255), nullable=True)
    alamat =db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    deleted_at = db.Column(db.DateTime, nullable=True)

    def ubahJson(self):
        return {
            "id_balaikonservasi": self.id_balaikonservasi,
            "nama_balai": self.nama_balai,
            "deskripsi": self.deskripsi,
            "provinsi": self.provinsi,
            "gambarbalai": self.gambarbalai,
            "alamat": self.alamat,
           
        }
class Kategori(db.Model):
    __tablename__ = 'kategori'
    id_kategori = db.Column(db.String(3), primary_key=True, default=lambda: str(uuid.uuid4())[:3])
    nama_kategori = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)  
    deleted_at = db.Column(db.DateTime, nullable=True)
    def to_dict(self):
        return {
            "id_kategori": self.id_kategori,
            "nama_kategori": self.nama_kategori
        }
    hewan = db.relationship("HewanModel", back_populates="kategori")

class Lapor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama_lapor = db.Column(db.String(255), nullable=False)
    nomer_hp = db.Column(db.String(15), nullable=False)
    alamat = db.Column(db.Text, nullable=False)
    maps = db.Column(db.String(255), nullable=False)
    keterangan = db.Column(db.Text, nullable=False)
    status = db.Column(db.Enum(StatusEnum), nullable=False, default=StatusEnum.sedang_di_proses)
    file_url = db.Column(db.String(255), nullable=True)  # Kolom baru untuk URL gambar

    def update_status(self, new_status):
        valid_status = [status.value for status in StatusEnum]
        if new_status in valid_status:
            self.status = StatusEnum(new_status)
        else:
            raise ValueError("Invalid status value")

    def to_dict(self):
        return {
            "id": self.id,
            "nama_lapor": self.nama_lapor,
            "nomer_hp": self.nomer_hp,
            "alamat": self.alamat,
            "maps": self.maps,
            "keterangan": self.keterangan,
            "status": self.status.value,
            "file_url": self.file_url, 
        }
    
class Berita(db.Model):
    __tablename__ = 'berita'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    judul = db.Column(db.String(255), nullable=False)
    tanggal = db.Column(db.Date, nullable=False, default=date.today)
    konten = db.Column(db.Text, nullable=False)
    gambar = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f"<Berita {self.id} - {self.judul}>"

    def to_dict(self):
        return {
            "id": self.id,
            "judul": self.judul,
            "tanggal": self.tanggal.strftime('%Y-%m-%d') if self.tanggal else None,
            "konten": self.konten,
            "gambar": self.gambar
        }
    
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    sentiment = db.Column(db.String(10), nullable=False)
    

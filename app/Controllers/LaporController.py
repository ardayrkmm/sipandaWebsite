from flask import render_template, request, redirect, url_for, flash, session, Blueprint, jsonify
from app import app, db, bcrypt  
from app.models import Lapor, StatusEnum

def laporF():
    if request.method == 'POST':
        # Ambil data dari form
        nama_lapor = request.form.get('nama_lapor')
        nomer_hp = request.form.get('nomer_hp')
        alamat = request.form.get('alamat')
        maps = request.form.get('maps')
        keterangan = request.form.get('keterangan')
        file_url = request.form.get('file_url')  

        # Status default
        status = StatusEnum.sedang_di_proses.value

        laporan = Lapor(
            nama_lapor=nama_lapor,
            nomer_hp=nomer_hp,
            alamat=alamat,
            maps=maps,
            keterangan=keterangan,
            file_url=file_url,  # Simpan file_url
            status=status
        )

        db.session.add(laporan)
        db.session.commit()

        flash("Laporan berhasil disimpan!", "success")
        return redirect(url_for('home'))

    file_url = request.args.get('file_url')  

    return render_template('lapor.html', file_url=file_url)

def laporApiF():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Data tidak valid"}), 400

    nama_lapor = data.get('nama_lapor')
    nomer_hp = data.get('nomer_hp')
    alamat = data.get('alamat')
    maps = data.get('maps')
    keterangan = data.get('keterangan')
    status = data.get('status', StatusEnum.sedang_di_proses.value)  
    file_url = request.form.get('file_url')

    # Validasi status jika disediakan
    if status not in [e.value for e in StatusEnum]:
        return jsonify({"error": "Status tidak valid"}), 400

    laporan = Lapor(
        nama_lapor=nama_lapor,
        nomer_hp=nomer_hp,
        alamat=alamat,
        maps=maps,
        file_url=file_url,
        keterangan=keterangan,
        status=status
    )
    db.session.add(laporan)
    db.session.commit()

    return jsonify({
        "message": "Laporan berhasil disimpan",
        "data": {
            "id": laporan.id,
            "nama_lapor": nama_lapor,
            "nomer_hp": nomer_hp,
            "alamat": alamat,
            "maps": maps,
            "keterangan": keterangan,
            "file_url": file_url,
            "status": status
        }
    }), 201

def laporan_page():
    """Halaman untuk menampilkan semua data laporan."""
    laporan_data = Lapor.query.all()
    laporan_proses = Lapor.query.filter_by(status=StatusEnum.sedang_di_proses.value).count()
    laporan_selesai = Lapor.query.filter_by(status=StatusEnum.selesai_di_proses.value).count()
    return render_template(
        'admin/pages/Laporan.html', 
        laporan_data=laporan_data, 
        laporan_proses=laporan_proses, 
        laporan_selesai=laporan_selesai
    )


def update_status():
    """Fungsi untuk memperbarui status laporan."""
    laporan_id = request.form.get('id')
    status = request.form.get('status')

    if not laporan_id or not status:
        flash("ID laporan atau status tidak ditemukan.", 'danger')
        return redirect(url_for('laporan'))

    laporan = Lapor.query.get(laporan_id)
    if not laporan:
        flash("Laporan tidak ditemukan.", 'danger')
        return redirect(url_for('laporan'))

    # Validasi status
    valid_statuses = [e.value for e in StatusEnum]
    if status not in valid_statuses:
        flash("Status tidak valid.", 'danger')
        return redirect(url_for('laporan'))

    # Update status laporan
    laporan.status = status
    db.session.commit()
    flash(f"Status laporan berhasil diubah menjadi '{status}'.", 'success')
    return redirect(url_for('laporan'))

def delete_laporan_by_id(laporan_id):
    laporan = Lapor.query.get_or_404(laporan_id)

    try:
        db.session.delete(laporan)  # Hapus laporan dari database
        db.session.commit()  # Simpan perubahan ke database
        flash('Laporan berhasil dihapus.', 'success')  # Tampilkan pesan sukses
    except Exception as e:
        db.session.rollback()  # Batalkan perubahan jika terjadi kesalahan
        flash(f'Terjadi kesalahan saat menghapus laporan: {e}', 'danger')  # Tampilkan pesan error

    return redirect(url_for('laporan'))

def cobaUpdate():
    data = request.json  # Mengambil data JSON dari fetch
    laporan_id = data.get('id')
    new_status = data.get('status')

    # Update laporan berdasarkan ID di database Anda
    laporan = Lapor.query.get(laporan_id)
    if laporan:
        laporan.status = new_status
        db.session.commit()
        return jsonify({'success': True, 'message': 'Status berhasil diperbarui!'})
    return jsonify({'success': False, 'message': 'Laporan tidak ditemukan!'})
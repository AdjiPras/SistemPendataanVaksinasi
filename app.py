from flask import Flask, request, jsonify, render_template, json, redirect, redirect, url_for, session, make_response
from flask_mongoengine import MongoEngine #ModuleNotFoundError: No module named 'flask_mongoengine' = (venv) C:\flaskmyproject>pip install flask-mongoengine
# from datetime import datetime
from models import MModel
from time import sleep
# from database import dbBrainly
# from pymongo import MongoClient

# import pymongo
# import datetime 
# import config2

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["brainlydb"]

application = Flask(__name__)
application.config['SECRET_KEY'] = 'sfh7^erw9*(%sadHGw%R'

# today = datetime.today()
model = MModel()
html_source = ''
 
app = Flask(__name__)
# app.config['MONGODB_SETTINGS'] = {
#     'db': 'brainlydb',
#     'host': 'localhost',
#     'port': 27017
# }
# db = MongoEngine()
# db.init_app(app)

# ======================================================================================================= 
# Index
@application.route('/')
def index():
	if 'data_nama' in session:
		# current_time_date = today.strftime("%B %d, %Y")
		data_nama = session['data_nama']
		return render_template('index_vaksin.html', data_nama=data_nama)
	return render_template('form_login.html')

# login	
@application.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		if model.authenticate(username, password):
			data_nama = model.getUserForSession(username)
			session['data_nama'] = data_nama
			return redirect(url_for('index'))
		msg = 'Username / Password Salah.'
		return render_template('form_login.html', msg=msg)
	return render_template('form_login.html')

# Logout	
@application.route('/logout')
def logout():
	session.pop('data_nama', '')
	return redirect(url_for('index'))

# ============================ Data Vaksinasi (Semua) ===================================================
# Menampilkan Data User
@application.route('/user')
def user():
    if 'data_nama' in session:
        data_nama = session['data_nama']
        nama = data_nama[1]
        container_user = [] 
        container_user = model.selectUser()
        return render_template('user.html', container_user=container_user, data_nama=data_nama)
    return render_template('form_login.html')

# Tambah Data User
@application.route('/insert_user', methods=['GET', 'POST'])
def insert_user():
	if 'data_nama' in session:
		if request.method == 'POST':
			ktp = request.form['ktp']
			username = request.form['username']
			password = request.form['password']
			nama = request.form['nama']
			no_telp = request.form['no_telp']
			email = request.form['email']
			tipe_akses = request.form['tipe_akses']
			data_u = (ktp, username, password, nama, no_telp, email, tipe_akses)
			model.insertUser(data_u)
			return redirect(url_for('user'))
		else:
			data_nama = session['data_nama']
			return render_template('insert_user.html', data_nama=data_nama)
	return render_template('form_login.html')

# Update Data User
@application.route('/update_user/<ktp>')
def update_user(ktp):
	if 'data_nama' in session:
		data_usr = model.getUserbyNo(ktp)
		data_nama = session['data_nama']
		return render_template('edit_user.html', data_usr=data_usr, data_nama=data_nama)
	return redirect(url_for('login')) 
    
@application.route('/update_usr', methods=['GET', 'POST'])
def update_usr():
    if 'data_nama' in session:
        ktp = request.form['ktp']
        username = request.form['username']
        password = request.form['password']
        nama = request.form['nama']
        no_telp = request.form['no_telp']
        email = request.form['email']
        tipe_akses = request.form['tipe_akses']
        data_usr = (ktp, username, password, nama, no_telp, email, tipe_akses)
        model.updateUser(data_usr)
        return redirect(url_for('user'))
    return render_template('form_login.html')

# Menghapus Data User
@application.route('/delete_user/<ktp>')
def delete_user(ktp):
    if 'data_nama' in session:
        model.deleteUser(ktp)
        return redirect(url_for('user'))
    return render_template('form_login.html')

# ============================ Data Vaksinasi (Semua) ===================================================
# Menampilkan Data Vaksin
@application.route('/vaksin')
def vaksin():
    if 'data_nama' in session:
        data_nama = session['data_nama']
        nama = data_nama[1]
        container_vaksin = [] 
        container_vaksin = model.selectVaksin()
        return render_template('vaksin.html', container_vaksin=container_vaksin, data_nama=data_nama)
    return render_template('form_login.html')

# Menambahakan Data Vaksin
@application.route('/insert_vaksin', methods=['GET', 'POST'])
def insert_vaksin():
	if 'data_nama' in session:
		if request.method == 'POST':
			ktp = request.form['ktp']
			nama = request.form['nama']
			jenis_kelamin = request.form['jenis_kelamin']
			agama = request.form['agama']
			kota_lahir = request.form['kota_lahir']
			tanggal_lahir = request.form['tanggal_lahir']
			kelurahan = request.form['kelurahan']
			kecamatan = request.form['kecamatan']
			kabupaten_kota = request.form['kabupaten_kota']
			provinsi = request.form['provinsi']
			no_telepon = request.form['no_telepon']
			jenis_vaksin = request.form['jenis_vaksin']
			lokasi_vaksin = request.form['lokasi_vaksin']
			jenis_dosis = request.form['jenis_dosis']
			data_v = (ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, jenis_dosis)
			model.insertVaksin(data_v)
			return redirect(url_for('vaksin'))
		else:
			data_nama = session['data_nama']
			return render_template('insert_vaksin.html', data_nama=data_nama)
	return render_template('form_login.html')

# Update Data Vaksin
@application.route('/update_vaksin/<ktp>')
def update_vaksin(ktp):
	if 'data_nama' in session:
		data_vk = model.getVaksinbyNo(ktp)
		data_nama = session['data_nama']
		return render_template('edit_vaksin.html', data_vk=data_vk, data_nama=data_nama)
	return redirect(url_for('login')) 
    
@application.route('/update_vk', methods=['GET', 'POST'])
def update_vk():
    if 'data_nama' in session:
        ktp = request.form['ktp']
        nama = request.form['nama']
        jenis_kelamin = request.form['jenis_kelamin']
        agama = request.form['agama']
        kota_lahir = request.form['kota_lahir']
        tanggal_lahir = request.form['tanggal_lahir']
        kelurahan = request.form['kelurahan']
        kecamatan = request.form['kecamatan']
        kabupaten_kota = request.form['kabupaten_kota']
        provinsi = request.form['provinsi']
        no_telepon = request.form['no_telepon']
        jenis_vaksin = request.form['jenis_vaksin']
        lokasi_vaksin = request.form['lokasi_vaksin']
        jenis_dosis = request.form['jenis_dosis']
        tipe_akses = request.form['tipe_akses']
        data_vk = (ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, jenis_dosis, tipe_akses)
        model.updateVaksin(data_vk)
        return redirect(url_for('vaksin'))
    return render_template('form_login.html')

# Delete Data Vaksin
@application.route('/delete_vaksin/<ktp>')
def delete_vaksin(ktp):
    if 'data_nama' in session:
        model.deleteVaksin(ktp)
        return redirect(url_for('vaksin'))
    return render_template('form_login.html')

# ============================ Dosis Vaksin ===================================================
@application.route('/dosis_pertama')
def dosis_pertama():
    if 'data_nama' in session:
        data_nama = session['data_nama']
        username = data_nama[1]
        container_dosis_pertama = [] 
        container_dosis_pertama = model.selectDosisPertama()
        return render_template('dosis_pertama.html', container_dosis_pertama=container_dosis_pertama, data_nama=data_nama)
    return render_template('form_login.html')

@application.route('/dosis_kedua')
def dosis_kedua():
    if 'data_nama' in session:
        data_nama = session['data_nama']
        username = data_nama[1]
        container_dosis_kedua = [] 
        container_dosis_kedua = model.selectDosisKedua()
        return render_template('dosis_kedua.html', container_dosis_kedua=container_dosis_kedua, data_nama=data_nama)
    return render_template('form_login.html')

@application.route('/booster_pertama')
def booster_pertama():
    if 'data_nama' in session:
        data_nama = session['data_nama']
        username = data_nama[1]
        container_booster_pertama = [] 
        container_booster_pertama = model.selectBoosterPertama()
        return render_template('booster_pertama.html', container_booster_pertama=container_booster_pertama, data_nama=data_nama)
    return render_template('form_login.html')

@application.route('/dbooster_kedua')
def booster_kedua():
    if 'data_nama' in session:
        data_nama = session['data_nama']
        username = data_nama[1]
        container_booster_kedua = [] 
        container_booster_kedua = model.selectBoosterKedua()
        return render_template('booster_kedua.html', container_booster_kedua=container_booster_kedua, data_nama=data_nama)
    return render_template('form_login.html')


# ============================ LAPORAN ===================================================
@application.route('/laporan')
def laporan():
    if 'data_nama' in session:
        data_nama = session['data_nama']
        nama = data_nama[1]
        container_laporan = [] 
        container_laporan = model.selectLaporan()
        return render_template('laporan.html', container_laporan=container_laporan, data_nama=data_nama)
    return render_template('form_login.html')

@application.route('/insert_laporan', methods=['GET', 'POST'])
def insert_laporan():
	if 'data_nama' in session:
		if request.method == 'POST':
			ktp = request.form['ktp']
			nama = request.form['nama']
			laporan = request.form['laporan']
			tanggal_lapor = request.form['tanggal_lapor']
			status = "-"
			data_lp = (ktp, nama, laporan, tanggal_lapor, status)
			model.insertLaporan(data_lp)
			return redirect(url_for('laporan'))
		else:
			data_nama = session['data_nama']
			return render_template('insert_laporan.html', data_nama=data_nama)
	return render_template('form_login.html')

@application.route('/update_laporan/<ktp>')
def update_laporan(ktp):
	if 'data_nama' in session:
		data_lap = model.getLaporanbyNo(ktp)
		data_nama = session['data_nama']
		return render_template('edit_laporan.html', data_lap=data_lap, data_nama=data_nama)
	return redirect(url_for('login'))

@application.route('/update_lp', methods=['GET', 'POST'])
def update_lp():
    if 'data_nama' in session:
        ktp = request.form['ktp']
        nama = request.form['nama']
        laporan = request.form['laporan']
        tanggal_lapor = request.form['tanggal_lapor']
        status = request.form['status']
        data_lap = (nama, laporan, tanggal_lapor, status, ktp)
        model.updateLaporan(data_lap)
        return redirect(url_for('laporan'))
    return render_template('form_login.html')

@application.route('/delete_laporan/<ktp>')
def delete_laporan(ktp):
    if 'data_nama' in session:
        model.deleteLaporan(ktp)
        return redirect(url_for('laporan'))
    return render_template('form_login.html')

if __name__ == '__main__':
    application.run(debug=True)
import pymysql
import config2

db = cursor = None

class MModel:
	def __init__ (self, no=None, nama=None, no_telp=None):
		self.no = no
		self.nama = nama
		self.no_telp = no_telp
		
	def openDB(self):
		global db, cursor
		db = pymysql.connect(
			host=config2.DB_HOST,
			user=config2.DB_USER,
			password=config2.DB_PASSWORD,
			database=config2.DB_NAME)
		cursor = db.cursor()

	def closeDB(self):
		global db, cursor
		db.close()

	# validasi login dengan table data_pengguna.
	def authenticate(self, ktp=None, nama=None):
		self.openDB()
		cursor.execute("SELECT COUNT(*) FROM data_vaksinasi WHERE ktp = '%s' AND nama = '%s'" % (ktp, nama))
		count_account = (cursor.fetchone())[0]
		self.closeDB()
		return True if count_account>0 else False

# ========================= Data vaksinasi (Semua) ================================
	def selectData(self):
		self.openDB()
		cursor.execute("SELECT ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses FROM `data_vaksinasi` ORDER BY nama ASC")
		container_vaksin = []
		for ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses in cursor.fetchall():
			container_vaksin.append((ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses))
		self.closeDB()
		return container_vaksin

	def getDataForSession(self, nama):
		self.openDB()
		cursor.execute("SELECT ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses FROM data_vaksinasi WHERE nama='%s'" % nama)
		data_nama = cursor.fetchone()
		return data_nama

	def insertData(self, data_v):
		self.openDB()
		cursor.execute("INSERT INTO data_vaksinasi (ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses) VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % data_v)
		db.commit()
		self.closeDB()

	def updateData(self, data_vk):
		self.openDB()
		cursor.execute("UPDATE data_vaksinasi SET nama='%s', jenis_kelamin='%s', agama='%s', kota_lahir='%s', tanggal_lahir='%s', kelurahan='%s', kecamatan='%s', kabupaten_kota='%s', provinsi='%s', no_telepon='%s', jenis_vaksin='%s', lokasi_vaksin='%s', dosis_pertama='%s', dosis_kedua='%s', tipe_akses='%s' WHERE ktp='%s'" % data_vk)
		db.commit()
		self.closeDB()

	def getDatabyNo(self, ktp):
		self.openDB()
		cursor.execute("SELECT ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses FROM data_vaksinasi WHERE ktp='%s'" % ktp)
		data_vk = cursor.fetchone()
		return data_vk

	def deleteData(self, ktp):
		self.openDB()
		cursor.execute("DELETE FROM data_vaksinasi WHERE ktp='%s'" % ktp)
		db.commit()
		self.closeDB()

# ========================= SLEMAN ================================
	def selectSleman(self):
		self.openDB()
		cursor.execute("SELECT ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses FROM `data_vaksinasi` WHERE kabupaten_kota='sleman' ORDER BY nama ASC")
		container_sleman = []
		for ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses in cursor.fetchall():
			container_sleman.append((ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses))
		self.closeDB()
		return container_sleman

	def getSlemanForSession(self, nama):
		self.openDB()
		cursor.execute("SELECT ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses FROM data_vaksinasi WHERE nama='%s'" % nama)
		data_nama = cursor.fetchone()
		return data_nama

# ========================= BANTUL ================================
	def selectBantul(self):
		self.openDB()
		cursor.execute("SELECT ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses FROM `data_vaksinasi` WHERE kabupaten_kota='bantul' ORDER BY nama ASC")
		container_bantul = []
		for ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses in cursor.fetchall():
			container_bantul.append((ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses))
		self.closeDB()
		return container_bantul

	def getBantulForSession(self, nama):
		self.openDB()
		cursor.execute("SELECT ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses FROM data_vaksinasi WHERE nama='%s'" % nama)
		data_nama = cursor.fetchone()
		return data_nama

# ========================= KOTA YOGYAKARTA ================================
	def selectKotaYogyakarta(self):
		self.openDB()
		cursor.execute("SELECT ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses FROM `data_vaksinasi` WHERE kabupaten_kota='kota yogyakarta' ORDER BY nama ASC")
		container_kota_yogyakarta = []
		for ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses in cursor.fetchall():
			container_kota_yogyakarta.append((ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses))
		self.closeDB()
		return container_kota_yogyakarta

	def getKotaYogyakartaForSession(self, nama):
		self.openDB()
		cursor.execute("SELECT ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses FROM data_vaksinasi WHERE nama='%s'" % nama)
		data_nama = cursor.fetchone()
		return data_nama

# ========================= GUNUNG KIDUL ================================
	def selectGunungKidul(self):
		self.openDB()
		cursor.execute("SELECT ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses FROM `data_vaksinasi` WHERE kabupaten_kota='gunung kidul' ORDER BY nama ASC")
		container_gunung_kidul = []
		for ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses in cursor.fetchall():
			container_gunung_kidul.append((ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses))
		self.closeDB()
		return container_gunung_kidul

	def getGunungKidulForSession(self, nama):
		self.openDB()
		cursor.execute("SELECT ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses FROM data_vaksinasi WHERE nama='%s'" % nama)
		data_nama = cursor.fetchone()
		return data_nama

# ========================= KULON PROGO ================================
	def selectKulonProgo(self):
		self.openDB()
		cursor.execute("SELECT ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses FROM `data_vaksinasi` WHERE kabupaten_kota='kulon progo' ORDER BY nama ASC")
		container_kulon_progo = []
		for ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses in cursor.fetchall():
			container_kulon_progo.append((ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses))
		self.closeDB()
		return container_kulon_progo

	def getKulonProgoForSession(self, nama):
		self.openDB()
		cursor.execute("SELECT ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses FROM data_vaksinasi WHERE nama='%s'" % nama)
		data_nama = cursor.fetchone()
		return data_nama

# ========================= NGANJUK ================================
	def selectNganjuk(self):
		self.openDB()
		cursor.execute("SELECT ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses FROM `data_vaksinasi` WHERE kabupaten_kota='nganjuk' ORDER BY nama ASC")
		container_nganjuk = []
		for ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses in cursor.fetchall():
			container_nganjuk.append((ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses))
		self.closeDB()
		return container_nganjuk

	def getNganjukForSession(self, nama):
		self.openDB()
		cursor.execute("SELECT ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses FROM data_vaksinasi WHERE nama='%s'" % nama)
		data_nama = cursor.fetchone()
		return data_nama

# ========================= SURABAYA ================================
	def selectSurabaya(self):
		self.openDB()
		cursor.execute("SELECT ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses FROM `data_vaksinasi` WHERE kabupaten_kota='surabaya' ORDER BY nama ASC")
		container_surabaya = []
		for ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses in cursor.fetchall():
			container_surabaya.append((ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses))
		self.closeDB()
		return container_surabaya

	def getSurabayaForSession(self, nama):
		self.openDB()
		cursor.execute("SELECT ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses FROM data_vaksinasi WHERE nama='%s'" % nama)
		data_nama = cursor.fetchone()
		return data_nama

# ========================= PURWOREJO ================================
	def selectPurworejo(self):
		self.openDB()
		cursor.execute("SELECT ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses FROM `data_vaksinasi` WHERE kabupaten_kota='purworejo' ORDER BY nama ASC")
		container_purworejo = []
		for ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses in cursor.fetchall():
			container_purworejo.append((ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses))
		self.closeDB()
		return container_purworejo

	def getPurworejoForSession(self, nama):
		self.openDB()
		cursor.execute("SELECT ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses FROM data_vaksinasi WHERE nama='%s'" % nama)
		data_nama = cursor.fetchone()
		return data_nama

# ========================= SEMARANG ================================
	def selectSemarang(self):
		self.openDB()
		cursor.execute("SELECT ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses FROM `data_vaksinasi` WHERE kabupaten_kota='semarang' ORDER BY nama ASC")
		container_semarang = []
		for ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses in cursor.fetchall():
			container_semarang.append((ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses))
		self.closeDB()
		return container_semarang

	def getSemarangForSession(self, nama):
		self.openDB()
		cursor.execute("SELECT ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses FROM data_vaksinasi WHERE nama='%s'" % nama)
		data_nama = cursor.fetchone()
		return data_nama

# ========================= BANDUNG ================================
	def selectBandung(self):
		self.openDB()
		cursor.execute("SELECT ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses FROM `data_vaksinasi` WHERE kabupaten_kota='bandung' ORDER BY nama ASC")
		container_bandung = []
		for ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses in cursor.fetchall():
			container_bandung.append((ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses))
		self.closeDB()
		return container_bandung

	def getBandungForSession(self, nama):
		self.openDB()
		cursor.execute("SELECT ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses FROM data_vaksinasi WHERE nama='%s'" % nama)
		data_nama = cursor.fetchone()
		return data_nama

# ========================= KAB BANDUNG ================================
	def selectKabBandung(self):
		self.openDB()
		cursor.execute("SELECT ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses FROM `data_vaksinasi` WHERE kabupaten_kota='kabupaten bandung' ORDER BY nama ASC")
		container_kab_bandung = []
		for ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses in cursor.fetchall():
			container_kab_bandung.append((ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses))
		self.closeDB()
		return container_kab_bandung

	def getKabBandungForSession(self, nama):
		self.openDB()
		cursor.execute("SELECT ktp, nama, jenis_kelamin, agama, kota_lahir, tanggal_lahir, kelurahan, kecamatan, kabupaten_kota, provinsi, no_telepon, jenis_vaksin, lokasi_vaksin, dosis_pertama, dosis_kedua, tipe_akses FROM data_vaksinasi WHERE nama='%s'" % nama)
		data_nama = cursor.fetchone()
		return data_nama

# ========================= Data Laporan ================================
	def selectLaporan(self):
		self.openDB()
		cursor.execute("SELECT ktp, nama, text_laporan, tanggal_lapor, status FROM `data_lapor` ORDER BY nama ASC")
		container_laporan = []
		for ktp, nama, text_laporan in cursor.fetchall():
			container_laporan.append((ktp, nama, text_laporan, tanggal_lapor, status))
		self.closeDB()
		return container_laporan

	def getLaporanForSession(self, nama):
		self.openDB()
		cursor.execute("SELECT container_laporan FROM data_lapor WHERE nama='%s'" % nama)
		data_nama = cursor.fetchone()
		return data_nama

	def insertLaporan(self, data_lp):
		self.openDB()
		cursor.execute("INSERT INTO data_lapor (ktp, nama, text_laporan, tanggal_lapor, status) VALUES('%s', '%s', '%s', '%s', '%s')" % data_lp)
		db.commit()
		self.closeDB()
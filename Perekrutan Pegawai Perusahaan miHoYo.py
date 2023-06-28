import json, os, time

userdata = "userdata.json"

def clean() :
    os.system('cls')

def readJson() :
    try:
        with open(userdata, 'r') as x :
            data = json.load(x)
        return data
    except FileNotFoundError :
        nulldata = []
        with open(userdata, 'w') as x :
            json.dump(nulldata, x, indent=4)
        return nulldata
def writeJson(data) :
    with open(userdata, 'w') as x :
        json.dump(data, x, indent=4)

    
def main() :
    clean()
    print("""
                                        =======================
                                             Selamat Datang 
                                        =======================
Silahkan mendaftar bila belum mempunyai akun.
Bila sudah, silahkan melanjutkan proses pendaftaran karyawan baru
 Ketik opsi yang tersedia [1/2]
 1. Login
 2. Daftar""")
    choice = input("Opsi : ")
    if choice == '1' :
        signin()
    elif choice == '2':
        signup()
    else:
        main()

def signin() :
    clean()
    print("\--Login Akun--/")
    username = input("username : ")
    password = input("password : ")
    user = readJson()
    if len(user) != 0 :
        status_signin = False
        for row in user :
            if row["username"] == username and row["password"] == password :
                status_signin = True
    else :
        print("Belum ada akun terdaftar, silahkan daftar terlebih dahulu.")
        time.sleep(3)
        main()
    
    if status_signin :
        print("berhasil login!")
        time.sleep(1)
        print("silahkan lanjut ke proses pendaftaran!")
        time.sleep(2.4)
        reg()
    else :
        print("login gagal.")
        time.sleep(1.5)
        print("Mohon masukkan username dan password kembali dengan benar.")
        time.sleep(2.4)
        signin()

def signup() :
    clean()
    print("\--Daftar Akun --/")
    username = input("username : ")
    password = input("password : ")
    password2 = input("ketik ulang password : ")
    if password2 == password :
        user = readJson()
        data_baru = {
            "username" : username,
            "password" : password
        }
        user.append(data_baru)
        writeJson(user)
        print("berhasil mendaftar!")
        time.sleep(2)
        print("silahkan login dan lanjutkan proses pendaftaran")
        time.sleep(2)
        main()
    else :
        print("password tidak sesuai, silahkan ketika ulang password dengan benar dan sesuai.")
        time.sleep(3)
        signup()

def reg():
    clean()
    print("""
                                        =======================
                                          R E G I S T R A S I 
                                        =======================
Selamat datang di laman pendaftaran. Anda bisa mengecek akun yang sudah terdaftar dan anda bisa melanjutkan proses pendaftaran
 Ketik opsi yang tersedia [1/2]
 1. Lanjut ke sesi pendaftaran identitas
 2. Cek akun yang sudah terdaftar""")
    choice = input("Opsi : ")
    if choice == '1' :
        pass
    elif choice == '2':
        check()
    else :
        reg()

def check():
    clean()
    with open(userdata, 'r') as x :
        data = json.load(x)
        counter = 0
        for x in data :
            counter += 1
            print("akun ke-" + str(counter), ":", x["username"])
            time.sleep(1.1)
        print("berikut adalah akun yang sudah terdaftar")
        time.sleep(1.5)
        input("ketik apapun untuk kembali : ")
        reg()

if __name__ == "__main__" :
    main()

identitas = "identitas.json"

def readJson() :
    try:
        with open(identitas, 'r') as x :
            data = json.load(x)
        return data
    except FileNotFoundError :
        nulldata = []
        with open(identitas, 'w') as x :
            json.dump(nulldata, x, indent=4)
        return nulldata
def writeJson(data) :
    with open(identitas, 'w') as x :
        json.dump(data, x, indent=4)

print("memasuki proses pengisian identitas...")
time.sleep(3)

def identity():
    clean()
    print("silahkan isi identitas anda dengan detail dan benar.")
    nama = input("nama : ")
    jenis_kelamin = input("jenis kelamin [pria/wanita] : ")
    tanggal_lahir = str(input("tempat tanggal lahir [ex. Jember, 17-05-02] : "))
    warga = input("kewarganegaraan : ")
    hp = str(input("nomor hp : "))
    email = input("alamat email : ")
    alamat = input("alamat rumah : ")
    pendidikan = input("pendidikan [SMA/S1/S2/S3] : ")
    agama = input("agama : ")
    user = readJson()
    data_baru = {
        "nama" : nama,
        "jenis kelamin" : jenis_kelamin,
        "tanggal lahir" : tanggal_lahir,
        "warga" : warga,
        "hp" : hp,
        "email" : email,
        "alamat" : alamat,
        "pendidikan" : pendidikan,
        "agama" : agama,
    }
    choice = input("apakah anda yakin semua sudah terisi dengan benar? [ya/tidak] : ")
    if choice == "ya" :
        user.append(data_baru)
        writeJson(user)
        print("data identitas berhasil disimpan!")
        time.sleep(2)
        print("silahkan lanjut ke sesi selanjutnya")
        time.sleep(2.5)
        clean()
    elif choice == "tidak" :
        print("memuat ulang pengisian identitas..")
        time.sleep(1)
        print("silahkan isi data identitas kembali dengan benar.")
        time.sleep(2.4)
        identity()

if __name__ == "__main__" :
    identity()

print("akan memulai sesi pertanyaan..")
time.sleep(1.2)
print("mohon tunggu sejenak..")
time.sleep(2.4)
clean()

yes = []
no = []

print("\--Pertanyaan Seleksi--/")
print("apakah anda mengetahui tentang perusahaan miHoYo?")
q1 = input("jawab [ya/tidak] : ")
print("apakah anda memiliki pengalaman bermain game dari miHoYo?")
q2 = input("jawab [ya/tidak] : ")
print("apakah anda pernah memiliki pengalaman kerja di perusahaan yang sejenis dengan perusahaan miHoYo sebelumnya?")
q3 = input("jawab [ya/tidak] : ")

if q1 == "ya" :
    yes.append(q1)
elif q1 == "tidak" :
    no.append(q1)

if q2 == "ya" :
    yes.append(q2)
elif q2 == "tidak" :
    no.append(q2)

if q3 == "ya" :
    yes.append(q3)
elif q3 == "tidak" :
    no.append(q3)

if len(yes) >= 2 :
    print("selamat, anda lolos dan layak untuk memasuki sesi wawancara")
    time.sleep(2)
    print("sebelum memasuki sesi wawancara, akan ditampilkan peraturan pekerjaan selama menjadi karyawan di perushaan kami")
    time.sleep(3.2)
    print("menampilkan peraturan..")
    time.sleep(2)
elif len(no) >= 2 :
    print("mohon maaf, anda tidak lolos karena kurang layak untuk melanjutkan ke sesi wawancara")
    time.sleep(3)
    print("silahkan mencoba lagi lain waktu")
    time.sleep(2)
    main()

def rule():
    clean()
print("""
                                        =======================
                                           P E R A T U R A N 
                                        =======================
Silahkan baca peraturan dan simak dengan teliti.
a. Pegawai tidak diperbolehkan untuk mengajukan pengunduran diri pada 1 tahun pertama kerja;
b. Mentaati disiplin dasar yang meliputi :
    • Mentaati jam kerja dan mengisi daftar hadir/tab RFID;
    • Mentaati penggunaan pakaian kerja dan atribut yang telah ditentukan;
    • Bersikap dan bertingkah laku simpatik, sopan santun dalam melaksanakan tugas;
c. Mengutamakan kepentingan Negara, Pemerintah, Perusahaan diatas kepentingan golongan atau pribadi;
d. Menjunjung tinggi kehormatan dan martabat Pegawai, Perusahaan, Pemerintah, dan Negara;
e. Menyimpan rahasia Jabatan, Perusahaan, Pemerintah dan Negara dengan sebaik-baiknya;
f. Melakukan tugas kedinasan dengan penuh kesadaran, tanggungjawab, jujur, tertib, cermat dan bersemangat untuk kepentingan Perusahaan;
g. Memelihara keutuhan, kekompakan, persatuan dan kesatuan sesama Pegawai;
h. Melaporkan kepada atasannya, apabila mengetahui ada Pegawai yang melakukan pelanggaran atau merugikan Perusahaan;
i. Menggunakan, memelihara dan mengamankan barang-barang milik Negara, Pemerintah, Perusahaan dengan sebaik-baiknya sesuai dengan kewarganegaraannya;
j. Memberikan pelayanan dengan sebaik-baiknya sesuai dengan bidang tugasnya masing-masing dan selalu berusaha untuk meningkatkan tercapainya sasaran pelayanan;
k. Bertindak dan bersikap tegas, adil dan bijaksana;
l. Membimbing, membina, dan memotivasi bawahan dalam melaksanakan tugas serta meningkatkan prestasi;
m. Saling menghormati sesama Pegawai dalam melaksanakan ibadah sesuai agama/kepercayaan masing-masing;
n. Selalu tanggap terhadap keluhan dan perkembangan dalam pelayanan;
o. Melaporkan secara tertulis setiap penambahan / pengurangan anggota keluarga, sertifikat pelatihan, ijazah pendidikan dan informasi lain yang dianggap perlu;
p. Mengembangkan diri untuk meningkatkan pengetahuan;
q. Setiap Pegawai yang mangkir wajib dilaporkan oleh atasan langsung Pegawai yang bersangkutan.""")
print("----------------------------------------------------")
choice = input("apakah anda menyanggupi untuk mematuhi semua peraturan diatas? [ya/tidak] : ")
if choice == "ya" :
    print("baik, akan memasuki sesi wawancara")
    time.sleep(1)
    print("mohon tunggu sejenak..")
    time.sleep(3)
    clean()
elif choice == "tidak" :
    print("dimengerti, semoga menemukan pekerjaan yang lebih cocok dengan anda")
    time.sleep(2)
    print("akan kembali ke laman utama..")
    time.sleep(3)
    main()

yes = []
no = []

print("\--Wawancara--/")
print("Apakah Anda Bersedia Jika Diminta Bekerja Lembur?")
q1 = input("jawab [ya/tidak] : ")
print("Apakah Anda Bersedia Jika Ditempatkan di Luar Kota?")
q2 = input("jawab [ya/tidak] : ")
print("Apakah Anda Bersedia Jika Menerima Tanggung Jawab yang Lebih Besar?")
q3 = input("jawab [ya/tidak] : ")
print("Apakah Anda mampu bekerja di bawah tekanan?")
q4 = input("jawab [ya/tidak] : ")
print("Apakah Anda mampu untuk bekerja dengan seseorang yang memiliki sifat berbeda?")
q5 = input("jawab [ya/tidak] : ")
print("Apakah Anda mampu menjaga hubungan yang baik dengan rekan kerja? ")
q6 = input("jawab [ya/tidak] : ")
print("Apakah Anda sudah melamar pekerjaan di perusahaan lain?")
q7 = input("jawab [ya/tidak] : ")
print("Apakah Anda yakin pekerjaan ini akan sesuai dengan apa yang anda inginkan?")
q8 = input("jawab [ya/tidak] : ")
print("Apakah Anda pernah mendapat sebuah prestasi atau pencapaian besar terkait pekerjaan anda sebelum ini?")
q9 = input("jawab [ya/tidak] : ")
print("Apakah Anda benar-benar mampu untuk mematuhi peraturan yang telah dibuat oleh perusahaan?")
q10 = input("jawab [ya/tidak] : ")
print("Apakah Anda siap menerima konsekuensi apabila telah melanggar peraturan? ")
q11 = input("jawab [ya/tidak] : ")
print("Menurut Mantan Atasan Anda, Apakah Kekurangan Diri Anda yang Harus Diperbaiki?")
q12 = input("jawab [ya/tidak] : ")
print("Berapa Gaji yang Diinginkan?")
q13 = input("jawab [sesuai standar/sepantasnya] : ")

if q1 == "ya" :
    yes.append(q1)
elif q1 == "tidak" :
    no.append(q1)

if q2 == "ya" :
    yes.append(q2)
elif q2 == "tidak" :
    no.append(q2)

if q3 == "ya" :
    yes.append(q3)
elif q3 == "tidak" :
    no.append(q3)

if q4 == "ya" :
    yes.append(q4)
elif q4 == "tidak" :
    no.append(q4)

if q5 == "ya" :
    yes.append(q5)
elif q5 == "tidak" :
    no.append(q5)

if q6 == "ya" :
    yes.append(q6)
elif q6 == "tidak" :
    no.append(q6)

if q7 == "ya" :
    yes.append(q7)
elif q7 == "tidak" :
    no.append(q7)

if q8 == "ya" :
    yes.append(q8)
elif q8 == "tidak" :
    no.append(q8)

if q9 == "ya" :
    yes.append(q9)
elif q9 == "tidak" :
    no.append(q9)

if q10 == "ya" :
    yes.append(q10)
elif q10 == "tidak" :
    no.append(q10)

if q11 == "ya" :
    yes.append(q11)
elif q11 == "tidak" :
    no.append(q11)

if q12 == "ya" :
    yes.append(q12)
elif q12 == "tidak" :
    no.append(q12)

if q13 == "sesuai standar" :
    yes.append(q13)
elif q13 == "sepantasnya" :
    no.append(q13)

x = len(yes) / 13
y = len(no) / 13

if x >= 0.5 :
    print("selamat, anda lolos dari sesi wawancara!")
    time.sleep(2)
    print("silahkan hubungi CP kami di lembar output lembar penerimaan karyawan. Selamat datang di miHoYo")
    time.sleep(3.2)
    clean()
elif y >= 0.5 :
    print("mohon maaf, anda tidak lolos dari sesi wawancara.")
    time.sleep(2.2)
    print("jangan putus semangat, anda bisa mencoba lain waktu!")
    time.sleep(2)
    print("akan kembali ke laman utama..")
    time.sleep(2)
    main()

print("sebelum lanjut, silahkan isi identitas kembali dengan benar!")
time.sleep(2)

def idt() :
    clean()
    print("(perhatikan besar-kecil huruf, harus sesuai dengan identitas yang diisi diawal)")
    time.sleep(2.5) 
    nama = input("nama : ")
    jenis_kelamin = input("jenis kelamin [pria/wanita] : ")
    tanggal_lahir = str(input("tempat tanggal lahir [ex. Jember, 17-05-02] : "))
    warga = input("kewarganegaraan : ")
    hp = str(input("nomor hp : "))
    email = input("alamat email : ")
    alamat = input("alamat rumah : ")
    pendidikan = input("pendidikan [SMA/S1/S2/S3] : ")
    agama = input("agama : ")
    idty = readJson()
    if len(idty) != 0 :
        status_idt = False
        for row in idty :
            if row["nama"] == nama and row["jenis kelamin"] == jenis_kelamin and row["tanggal lahir"] == tanggal_lahir and row["warga"] == warga and row["hp"] == hp and row["email"] == email and row["alamat"] == alamat and row["pendidikan"] == pendidikan and row["agama"] == agama :
                status_idt = True
    else :
        pass
    
    if status_idt :
        print("identitas sesuai")
        time.sleep(1)
        print("mengeprint output lembar penerimaan karyawan..")
        time.sleep(3)
        clean()
    else :
        print("identitas tidak sesuai")
        time.sleep(1.5)
        print("mohon isi identitas dengan sebenar-benarnya dan pastikan isi sesuai persis dengan identitas yang sudah diisi saat pendaftaran.")
        time.sleep(4)
        idt()

if __name__ == "__main__" :
    idt()

print("""
                        ======================================
                        Output Lembar Penerimaan Karyawan Baru
                        ======================================""")
print("Dengan ini menerangkan bahwa yang bersangkutan dibawah ini:")
with open(identitas, 'r') as x :
    data = json.load(x)
    for x in data :
        print("Nama     :", x["nama"])
        print("E-Mail   :", x["email"])
        print("Alamat   :", x["alamat"])
print("Kami nyatakan bahwa saudara", x["nama"], "benar-benar menjadi karyawan tetap di Perusahaan miHoYo. Dan yang bersangkutan benar adalah karyawan tetap sampai sekarang.")
print("TTD. Kepala Perusahaan ")

os.remove("identitas.json")
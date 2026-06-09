# solverganjil.py : Nikko Puzzle (Ganjil)
 
Repository ini berisi program bot otomatis (solver) berbasis Python yang dirancang khusus untuk menyelesaikan challenge Nikko Puzzle Ganjil `nikko_puzzle_ganjil_windows_x86_zip` . Program ini terhubung langsung ke server challenge melalui koneksi socket dan menjawab 100 soal secara otomatis dalam batas waktu 1 detik per soal.

---

## Analisis Soal

Setelah menjalankan challenge, saya mengamati bahwa setiap soal berisi deretan angka yang dipisahkan tanda koma.

Tugas utama adalah menentukan berapa jumlah bilangan genap dan berapa jumlah bilangan ganjil pada setiap soal.

Karena challenge terdiri dari 100 soal dengan batas waktu yang sangat singkat, saya memutuskan membuat program python otomatis (solverganjl.py) yang dapat:

- menerima soal dari server
- memproses angka secara otomatis
- menghitung jumlah genap dan ganjil
- mengirim jawaban kembali ke server

---

## Fitur-fitur utama Solverganjil.py

- **Auto Onboarding:**
   Bot mendeteksi permintaan data dari server dan mengirimkan Nama & NIM secara otomatis tanpa input manual
- **Real-time Socket Connection:**
  Program terhubung langsung ke server menggunakan koneksi TCP melalui HOST dan PORT yang disesuaikan setiap user membuka terminal
- **Automatic Number Parser:**
  Bot memisahkan deretan angka dari soal menggunakan tanda koma, termasuk angka negatif
- **Modulo-based Classifier:**
  Menggunakan operator modulo % untuk menentukan genap/ganjil setiap angka secara instan
- **Sub-1-Second Response Rate:**
  Jawaban dikirim dalam waktu kurang dari 1 detik per soal sehingga lolos dari batas waktu challenge

  ---

## Logika Penentuan Genap & Ganjil
Bot berhasil menyelesaikan challenge hingga server mengembalikan pesan keberhasilan (congratulation), logika program yang saya gunakan sebagai berikut:

           genap = 0
            for x in angka:
              if x % 2 == 0:
                genap = genap + 1

           ganjil = len(angka) - genap
            
Contoh dengan soal `3564,2555,7624,8901`:

| Angka | Operasi | Hasil |
|-------|---------|-------|
| 3564 | 3564 % 2 = 0 | Genap |
| 2555 | 2555 % 2 = 1 | Ganjil |
| 7624 | 7624 % 2 = 0 | Genap |
| 8901 | 8901 % 2 = 1 | Ganjil |

**Jawaban dikirim:** `2|2`= 2 genap dan 2 ganjil

---

## Implementasi program python solverganjil.py

1. Jalankan file challenge, pilih Mode 1

2. Catat PORT yang muncul di terminal, contoh: nc 127.0.0.1 50822

   Selalu cek dan ganti PORT di file solverganjil.py  

3. Jalankan bot:

   `python solverganjil.py`

4. Hasil

    Bot berhasil menyelesaikan 100 soal berturut-turut tanpa gagal dalam batas waktu 1 detik per soal. Sebagai bukti penyelesaian, server menampilkan pesan:

    `Congratulation you solve the game yeay! please send congratulation.nikko ke hi@nikko.id ya!`

    File congratulation juga otomatis muncul di dalam ZIP challenge setelah bot berhasil menyelesaikan semua soal.


import socket
import time

HOST = "127.0.0.1"
PORT = 50763

NAMA = "rischa sulistya agustin"
NIM = "241080200005"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

buffer = ""
sudah_onboarding = False

while True:
    data = sock.recv(4096)

    if not data:
        break

    teks = data.decode(errors="ignore")
    print(teks, end="")

    buffer += teks

    if not sudah_onboarding and "onboarding" in buffer.lower():
        time.sleep(0.1)
        sock.sendall((NAMA + "\n").encode())
        time.sleep(0.1)
        sock.sendall((NIM + "\n").encode())

        print("\n[+] Nama dan NIM berhasil dikirim\n")

        sudah_onboarding = True
        buffer = ""
        continue

    if "Jawaban" in buffer:

        baris_soal = ""

        for baris in buffer.splitlines():
            if "," in baris:
                baris_soal = baris
                break

        if baris_soal:
            angka = []

            for x in baris_soal.split(","):
                x = x.strip()
                try:
                    angka.append(int(x))
                except:
                    pass

            genap = sum(1 for x in angka if x % 2 == 0)
            ganjil = len(angka) - genap
            jawaban = f"{genap}|{ganjil}\n"

            print("[KIRIM]", jawaban.strip())
            sock.sendall(jawaban.encode())

        buffer = ""

sock.close()
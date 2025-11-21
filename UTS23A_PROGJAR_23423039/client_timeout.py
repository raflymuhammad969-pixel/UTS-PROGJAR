
import socket

HOST = "127.0.0.1"
PORT = 5050

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 1. Timeout saat connect (3 detik)
client.settimeout(3)

print("Mencoba menghubungi server...")

try:
    client.connect((HOST, PORT))
    print("Berhasil terhubung!\n")
except socket.timeout:
    print("Koneksi timeout! (Saat connect)")
    exit()
except Exception as e:
    print("Error:", e)
    exit()

# 2. Timeout saat menerima data (2 detik)
client.settimeout(2)

try:
    client.send(b"Tes Koneksi Timeout")

    try:
        data = client.recv(1024)
        print("Balasan:", data.decode())
    except socket.timeout:
        print("Koneksi timeout! (Saat menerima data)")

except Exception as e:
    print("Error:", e)

client.close()

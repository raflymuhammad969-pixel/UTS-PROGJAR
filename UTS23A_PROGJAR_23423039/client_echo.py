
import socket

HOST = "127.0.0.1"
PORT = 5050

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

pesan = "Tes Koneksi"
client.sendall(pesan.encode())

balasan = client.recv(1024).decode()
print("Balasan dari server:", balasan)

client.close()

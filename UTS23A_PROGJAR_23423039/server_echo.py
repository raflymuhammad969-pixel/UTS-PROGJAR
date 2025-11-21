
import socket

HOST = "0.0.0.0"
PORT = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"Server berjalan di port {PORT} ...")

conn, addr = server.accept()
print(f"Terhubung dengan client: {addr}")

while True:
    data = conn.recv(1024)
    if not data:
        break

    print("Pesan diterima dari client:", data.decode())

    # kirim kembali ke client (echo)
    conn.sendall(data)

conn.close()
server.close()

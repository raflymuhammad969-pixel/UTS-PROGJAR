
import socket
import threading

HOST = "127.0.0.1"
PORT = 6060

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Chat Server berjalan...")

clients = []

def broadcast(pesan):
    for c in clients:
        try:
            c.send(pesan)
        except:
            pass

def handle_client(conn, addr):
    print(f"Terhubung dengan {addr}")
    clients.append(conn)

    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            broadcast(data)
        except:
            break

    conn.close()
    clients.remove(conn)
    print(f"{addr} terputus")

while True:
    conn, addr = server.accept()
    threading.Thread(target=handle_client, args=(conn, addr)).start()

import socket
import threading

HOST = "127.0.0.1"
PORT = 6060

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def terima():
    while True:
        try:
            data = client.recv(1024).decode()
            if data:
                print("Pesan:", data)
        except:
            break

threading.Thread(target=terima, daemon=True).start()

while True:
    pesan = input("")
    client.send(pesan.encode())

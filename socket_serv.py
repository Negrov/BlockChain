import socket


sock = socket.socket()
sock.bind(('localhost', 8080))
sock.listen(2)
conn, address = sock.accept()
data = ""


while True:
    text = conn.recv(2048)

    if not text:
        break

    data += text.decode("utf-8")

data = data.encode("utf-8")

conn.close()

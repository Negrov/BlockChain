import socket
import users_db


class Server:

    def __init__(self):
        self.suck = socket.socket()
        self.suck.bind(('localhost', 8080))
        self.suck.listen(2)
        self.conn, self.address = self.suck.accept()
        users_db.users.append(self.conn, self.address)

    def start_listening(self):
        data = ""
        while True:
            text = self.conn.recv(2048)
            if not text:
                break
            data += text.decode("utf-8")
        data = data.encode("utf-8")
        self.conn.close()

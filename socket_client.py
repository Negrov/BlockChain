import socket


class Client:
    def __init__(self):
        self.data = ''

    def input_data(self, text: str):
        text = text.encode('utf-8')
        sock = socket.socket()
        sock.connect(('localhost', 8080))
        last = 0

        for i in range(0, len(text), 524):

            sock.send(text[i:i + 524])
            last = i

        sock.send(text[last:])

        self.data = sock.recv(2048).decode('utf-8')

        sock.close()

    def output_data(self) -> str:
        return self.data

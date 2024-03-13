from time import time
from hashlib import sha256


class Block:

    def __init__(self, timestamp=None, data=None):
        self.timestamp = timestamp or time()
        self.data = [] if data is None else data
        self.difficulty = 1  # Количество символов в хеше
        self.prevHash = None  # Хеш предыдущего блока
        self.nonce = 0
        self.hash = self.gethash()  # хеш блока

    def gethash(self) -> str:

        hashik = sha256()
        hashik.update(str(self.prevHash).encode('utf-8'))
        hashik.update(str(self.timestamp).encode('utf-8'))
        hashik.update(str(self.data).encode('utf-8'))
        hashik.update(str(self.nonce).encode('utf-8'))

        return hashik.hexdigest()

    def mine(self, difficulty) -> None:

        while self.hash[:difficulty] != '0' * difficulty:  # Пока хеш не будет начинаться со строки 0 * difficulty

            self.nonce += 1  # Новый nonce
            self.hash = self.gethash()  # Хешируем nonce

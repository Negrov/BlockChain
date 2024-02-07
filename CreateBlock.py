from time import time
from hashlib import sha256


class Block:

    def __init__(self, timestamp=None, data=None):
        self.timestamp = timestamp or time()
        self.data = [] if data is None else data
        self.hash = self.gethash()  # хеш блока
        self.prevHash = None  # Хеш предыдущего блока

    def gethash(self) -> str:
        hashik = sha256()
        hashik.update(str(self.prevHash).encode('utf-8'))
        hashik.update(str(self.timestamp).encode('utf-8'))
        hashik.update(str(self.data).encode('utf-8'))
        return hashik.hexdigest()

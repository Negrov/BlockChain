from time import time
from CreateBlock import Block


class Blockchain:

    def __init__(self):
        self.chain = [Block(str(int(time())))]  # Создание первичного блока

    def getlastblock(self):
        return self.chain[len(self.chain) - 1]  #

    def addblock(self, block):
        block.prevHash = self.getlastblock().hash  # Хеш предыдущего блока
        block.hash = block.gethash()  # хеш этого блока
        self.chain.append(block)  # Добавление нового блока в список блоков

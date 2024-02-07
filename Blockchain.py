from time import time
from CreateBlock import Block


class Blockchain:

    def __init__(self):
        self.chain = [Block(str(int(time())))]  # Создание первичного блока

    def getlastblock(self) -> Block:
        return self.chain[len(self.chain) - 1]  # Последний блок в списке блоков

    def addblock(self, block) -> None:
        block.prevHash = self.getlastblock().hash  # Хеш предыдущего блока
        block.hash = block.gethash()  # хеш этого блока
        block.mine(block.difficulty)
        self.chain.append(block)  # Добавление нового блока в список блоков

    def examination(self) -> bool:
        for i in range(1, len(self.chain)):  # Проверка блоков
            current_block = self.chain[i]
            prev_block = self.chain[i - 1]

            # Проверка
            if (current_block.hash != current_block.gethash() or
                    prev_block.hash != current_block.prevHash):
                return False

        return True

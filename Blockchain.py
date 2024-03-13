import json
from time import time
from CreateBlock import Block


class Blockchain:

    def __init__(self):
        self.chain = [Block(str(int(time())))]  # Создание первичного блока
        self.difficulty = 1
        self.blockTime = 30000

    def get_last_block(self) -> Block:
        return self.chain[len(self.chain) - 1]  # Последний блок в списке блоков

    def add_block(self, block) -> None:
        block.prevHash = self.get_last_block().hash  # Хеш предыдущего блока
        block.hash = block.gethash()  # хеш этого блока
        block.mine(block.difficulty)
        self.chain.append(block)  # Добавление нового блока в список блоков
        self.difficulty += (-1, 1)[int(time()) - int(self.get_last_block().timestamp) < self.blockTime]

    def examination(self) -> bool:
        for i in range(1, len(self.chain)):  # Проверка блоков
            current_block = self.chain[i]
            prev_block = self.chain[i - 1]

            # Проверка
            if (current_block.hash != current_block.gethash() or
                    prev_block.hash != current_block.prevHash):
                return False

        return True

    def __repr__(self):
        return json.dumps([{'data': item.data, 'timestamp': item.timestamp, 'nonce': item.nonce, 'hash': item.hash,
                            'prevHash': item.prevHash} for item in self.chain], indent=4)

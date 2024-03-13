import Blockchain
import CreateBlock
from time import time


def main():

    june = Blockchain.Blockchain()
    june.add_block(CreateBlock.Block(str(int(time())), {"from": "june", "to": "jack", "amount": 10000}))
    print(june)


if __name__ == '__main__':
    main()

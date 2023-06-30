import hashlib




class Block:
    prev_block = 0
    prev_hash = "0" * 64

    def __init__(self,data:str):
        self.block = Block.prev_block + 1 
        Block.prev_block = self.block
        self.nonce = 1
        self.data = data
        self.prev = Block.prev_hash 
        Block.prev_hash = self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha256(str(str(self.block + self.nonce ) + self.data + self.prev).encode()).hexdigest()


    def __repr__(self):
        return f"Block( block={self.block}, nonce={self.nonce}, data={self.data}, prev={self.prev}, hash={self.calculate_hash()} )"
    
    def mine(self,difficulty:int):
        while True:
            if self.calculate_hash()[:difficulty] == "0"* difficulty:
                return self.calculate_hash()
            self.nonce += 1
            continue
            
class BlockChain:
    def __init__(self):
        self.blockchain = []




block_1 = Block("messiye",)
block_2 = Block("ronaldo")
block_3 = Block("sterling")

blockchain = BlockChain()
blockchain.blockchain.append(block_1)
blockchain.blockchain.append(block_2)
blockchain.blockchain.append(block_3)


# print(blockchain)
print(repr(block_1))
print(repr(block_2))
print(repr(block_3))

# print(block_1.mine(5))

# print(repr(block_1))
# print(repr(block_2))
# print(repr(block_3))






# mine()
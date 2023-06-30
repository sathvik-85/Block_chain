import hashlib




class Block:
    prev_block = 0
    prev_hash = "0" * 64

    def __init__(self,nonce:int,data:str):
        self.block = Block.prev_block + 1 
        Block.prev_block = self.block
        self.nonce = nonce
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
            


block_1 = Block(1,"messiywerwerdasd",)
block_2 = Block(1,"ronaldo")
block_3 = Block(1,"sterling")
block_4 = Block(1,"cassady")
block_5 = Block(1,"cassady")



blockchain = [block_1,block_2,block_3,block_4]



print(repr(block_1))
print(repr(block_2))
print(repr(block_3))
print(repr(block_4))





print(block_1.mine(5))






# mine()
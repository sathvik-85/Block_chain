import hashlib



b_lambda = (lambda x: hashlib.sha256(str(i).encode().hexdigest()))

class Block:
    prev_block = 0

    def __init__(self,nonce:int,data:str):
        self.block = Block.prev_block + 1 
        Block.prev_block = self.block
        self.nonce = nonce
        self.data = data
        self.prev = "0"
        self.hash = hashlib.sha256(str(str(self.block + self.nonce ) + self.data + self.prev).encode()).hexdigest()

    def __repr__(self):
        return f"Block( block={self.block}, nonce={self.nonce}, data={self.data}, prev={self.prev}, hash={self.hash} )"


block_1 = Block(1,"messi",)
block_2 = Block(1,"ronaldo")
block_3 = Block(1,"sterling")
block_4 = Block(1,"cassady")



blockchain = [block_1,block_2,block_3,block_4]

print(repr(block_1))
print(repr(block_2))
print(repr(block_3))
print(repr(block_4))




    




# def mine():
#     for i in range(1000000000000):
#         hash = hashlib.sha256(str(i).encode())
#         hash = hash.hexdigest()
#         print(hash)
#         if hash[:4] == "0000":
#             return hash
#         continue

# mine()
import hashlib

class Block:
    prev_block = 0

    def __init__(self,nonce:int,data:str,hash:str):
        self.block = Block.prev_block + 1 
        Block.prev_block = self.block
        self.nonce = nonce
        self.data = data
        self.prev = 0
        self.hash = hash

    def __repr__(self):
        return f"Block( block={self.block}, nonce={self.nonce}, data={self.data}, prev={self.prev}, hash={self.hash} )"

x = Block(1,"qwerty","qwwqerwerwefwef")
y = Block(1,"qwerty","qwwqerwerwefwef")
z = Block(1,"qwerty","qwwqerwerwefwef")
a = Block(1,"qwerty","qwwqerwerwefwef")

print(repr(x))
print(repr(y))
print(repr(z))
print(repr(a))
    




# def mine():
#     for i in range(1000000000000):
#         hash = hashlib.sha256(str(i).encode())
#         hash = hash.hexdigest()
#         print(hash)
#         if hash[:4] == "0000":
#             return hash
#         continue

# mine()
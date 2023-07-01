import hashlib

class Block:
    block = 0
    prev_hash = "0" * 64

    def __init__(self,data):
        self.block = Block.block + 1
        self.nonce = 1
        self.data = data
        self.prev = Block.prev_hash
        self.calculate_hash()
        Block.block += 1
    

    def __repr__(self):
        return f"Block( block={self.block}, nonce={self.nonce}, data={self.data}, prev={self.prev[:5]}, hash={self.hash[:5]} )"
    
    def calculate_hash(self):
        self.hash = hashlib.sha256(str(str(self.block + self.nonce ) + self.data + self.prev).encode()).hexdigest()
        print(self.block)
        print(self.nonce)
        print(self.data)
        print(self.prev)
        print(self.hash)
    

    
    

class BlockChain:
    def __init__(self):
        self.blockchain = []
    def __repr__(self):
        elements = '\n'.join(str(element) for element in self.blockchain)
        return f"BlockChain:\n{elements}"
    
    def block_update(self,idx,data):
        self.blockchain[idx].data = data 
        self.blockchain[idx].calculate_hash()
        for i in range(idx + 1, len(self.blockchain)):
            self.blockchain[i].prev = self.blockchain[i - 1].hash
            self.blockchain[i].calculate_hash()



b1 = Block("messi")
b2 = Block("ronaldo")
b3 = Block("rajesh")
b4 = Block("raja")



blockchain = BlockChain()
blockchain.blockchain.append(b1)
blockchain.blockchain.append(b2)
blockchain.blockchain.append(b3)
blockchain.blockchain.append(b4)


print(repr(blockchain))                 


blockchain.block_update(1,"pendu")

print()
 

print(repr(blockchain))
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
        Block.prev_hash = self.hash
    

    def __repr__(self):
        return f"Block( block={self.block}, nonce={self.nonce}, data={self.data}, prev={self.prev[:5]}, hash={self.hash[:5]} )"
    
    def calculate_hash(self):
        self.hash = hashlib.sha256(str(str(self.block + self.nonce ) + self.data + self.prev).encode()).hexdigest()
    

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
    
    def mine(self,idx):
        flag = False
        while idx < len(self.blockchain):
            while True:
                self.blockchain[idx].calculate_hash()
                if  self.blockchain[idx].hash[:4] == "0"* 4:
                    flag = True
                    self.block_update(idx,self.blockchain[idx].data)
                    break
                if flag:
                    break
                self.blockchain[idx].nonce += 1
            idx += 1

b1 = Block("messi")
b2 = Block("ronaldo")
b3 = Block("rajesh")
b4 = Block("raja")
b5 = Block("kaja")




blockchain = BlockChain()
blockchain.blockchain.append(b1)
blockchain.blockchain.append(b2)
blockchain.blockchain.append(b3)
blockchain.blockchain.append(b4)
blockchain.blockchain.append(b5)


print(repr(blockchain))                 


# blockchain.block_update(1,"pendu")
# blockchain.block_update(4,"rendu")
blockchain.mine(0)
print()
 

print(repr(blockchain))
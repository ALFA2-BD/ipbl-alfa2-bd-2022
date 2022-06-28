from datetime import datetime
import hashlib
import json
from DTO.BlockDTO import BlockDTO

class BlockChain:

    def __init__(self)->None:
        super().__init__()
        self.chain = []
        self.create_block(
            proof=1, 
            previous_hash='0'
        )
    
    def get_chain_dict(self, *args, **kwargs):

        chain_obj = self.chain
        chain_dict = []

        for block in chain_obj:
            block:BlockChain
            chain_dict.append(block.get_dict())

        return chain_dict
    
    def create_block(self, *args, **kwargs)->None:
        
        proof:int
        previous_hash:str

        proof = kwargs['proof']
        previous_hash = kwargs['previous_hash']

        block = BlockDTO(
            index = len(self.chain) + 1,
            timestamp = str(datetime.now()),
            proof = proof,
            previous_hash = previous_hash
        )

        self.chain.append(block)

        return block
    
    def get_previous_block(self, *args, **kwargs)->BlockDTO:

        return self.chain[-1]
    
    def proof_of_work(self, *args, **kwargs)->int:
        
        previous_proof:str

        previous_proof = kwargs['previous_proof']
        new_proof = 1
        check_proof = False

        while not check_proof:
            dificult_level = str(new_proof**2  - previous_proof**2)
            hash_operation = hashlib.sha256(dificult_level.encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        
        return new_proof
    
    def hash(self, *args, **kwargs)->str:
        
        block:BlockDTO
        block = kwargs['block']

        encoded_block = json.dumps(
            block.get_dict(),
            sort_keys=True
        ).encode()

        return hashlib.sha256(encoded_block).hexdigest()
    
    def is_chain_valid(self, *args, **kwargs)->bool:

        chain:list
        chain = self.chain if 'chain' not in kwargs else kwargs['chain']

        previous_block:BlockDTO
        previous_block = chain[0]
        block_index = 1

        while block_index < len(chain):

            block:BlockDTO
            block = chain[block_index]

            if block.previous_hash != self.hash(block=previous_block):
                return False
            
            previous_proof = previous_block.proof
            proof = block.proof

            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()

            if hash_operation [:4] != '0000':
                return False
            
            previous_block = block
            block_index += 1
        
        return True
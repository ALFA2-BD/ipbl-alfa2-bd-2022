from datetime import datetime
from .BaseDTO import BaseDTO

class BlockDTO(BaseDTO):
    
    index:int
    timestamp:datetime
    proof:int
    previous_hash:str

    def __init__(self, *args, **kwargs) -> None:
        
        self.index = kwargs['index']
        self.timestamp = kwargs['timestamp']
        self.proof = kwargs['proof']
        self.previous_hash = kwargs['previous_hash']

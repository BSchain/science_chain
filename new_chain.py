# -*- coding: utf-8 -*-
# @Time    : 05/01/2018 12:43 PM
# @Author  : 伊甸一点
# @FileName: new_chain.py
# @Software: PyCharm
# @Blog    : http://zpfbuaa.github.io

from time import time
import json
import hashlib as hasher

class Blockchain():
    def __init__(self):
        self.chain_length = self.get_chain_length()
        self.last_block = {}
        self.current_transactions = []
        self.current_diff = self.get_diff()

    def get_chain_length(self): # next_block_index = chain_length + 1 = len(dir) + 1
        return 1
        pass

    def get_last_block(self): # read file and get the last block
        pass

    def get_total_block(self):
        pass

    def get_block_by_height(self): # read file and get one block
        pass

    # we can change diff or create diff rules.
    def get_diff(self): # generate the difficult to mine new block
        pass

    def save_block(self): # when mine one block then update block and store new block to file
        pass

    def get_current_transactions(self): # generate transaction from file
        pass

    @staticmethod
    def hash(block):
        block_str = json.dumps(block, sort_keys=True).encode()
        return hasher.sha256(block_str).hexdigest()

    def generate_new_block(self, proof, previous_hash=None): # generate new block from transaction
        block = {
            'index': self.chain_length + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.last_block),
        }
        # Reset the current list of transactions
        self.current_transactions = []
        self.last_block = block
        self.save_block()
        self.chain_length += 1
        pass

    def proof_of_work(self,last_proof): # proof of work
        proof = 0
        while (self.valid_proof(last_proof, proof,self.current_diff) is False):
            proof = proof + 1
        return proof

    @staticmethod
    def valid_proof(last_proof,proof,diff): # valid proof
        mine = f'{last_proof}{proof}'.encode()
        mine_hash = hasher.sha256(mine).hexdigest()
        diff_str = '0' * diff
        return mine_hash[:diff] == diff_str

        pass





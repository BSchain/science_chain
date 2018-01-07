# -*- coding: utf-8 -*-
# @Time    : 06/01/2018 1:02 PM
# @Author  : 伊甸一点
# @FileName: chain.py
# @Software: PyCharm
# @Blog    : http://zpfbuaa.github.io

from block import *
import requests
from node import *
class Chain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.nodes = set()

    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __ge__(self, other):
        pass

    def __le__(self, other):
        pass

    def is_valid(self):
        return valid_chain(self.chain)
        pass

    def save_chain(self):
        assert os.path.exists(config.BLOCK_SAVE_ROOT), ('blocks save file not exist')
        for index,each_block in enumerate(self.chain):
            block_file = self.get_block_file(index+1)
            f = open(block_file,'w')
            f.write(json.dumps(self.chain))
            f.close()


    def find_block_by_index(self, index):
        assert int(index) > 0, ('index must greater than 0')
        assert int(index) >= int(len(self.chain)), ('index must smaller than chain_length',index,len(self.chain))
        block_file = self.get_block_file(index)
        assert os.path.exists(block_file), (block_file,'not exist')
        with open(block_file, 'r') as f:
            block = json.load(f)
        return block

    @staticmethod
    def get_block_file(index):
        return config.BLOCK_SAVE_ROOT + str(index) + config.BLOCK_SAVE_SUFFIX

    # use a file to store index and hash
    # def find_block_by_hash(self, hash):
    #     pass

    def get_total_chain(self):
        assert os.path.exists(config.BLOCK_SAVE_ROOT), ('blocks file not exist')
        block_list = os.listdir(config.BLOCK_SAVE_ROOT)
        for each_block in block_list:
            index = each_block.split('.')[0]
            assert str(len(self.chain)+1) == str(index), ('lost index',index)
            with open(config.BLOCK_SAVE_ROOT+each_block,'r') as f:
                block = json.load(f)
            self.chain.append(block)

    def add_block(self,block): # save block to file and add block to chain
        block.save_block()
        self.chain.append(block)

    def add_transaction(self,transaction):
        self.current_transactions.append(transaction)

    def reset_transaction(self): # when mining a new block, then empty the current_transaction
        self.current_transactions = []

    def generate_block(self, nonce, prev_hash): # generate according to nonce and prev_hash
        # 1. new block
        # 2. prepare parameters
        # 3. save_block to file
        # 4. add block to chain
        block = Block()
        index = len(self.chain) + 1
        timestamp = time()
        transactions = self.current_transactions
        block.new_block(index,timestamp,prev_hash,transactions,nonce)
        block.save_block()
        self.chain.append(block.to_dict()) # be careful, use to_dict

    def resolve_conflicts(self):
        neighbours = self.nodes
        new_chain = None
        # We're only looking for chains longer than ours
        max_length = len(self.chain)

        # Grab and verify the chains from all the nodes in our network
        for node in neighbours:
            response = requests.get(f'http://{node}/chain') # TODO: need to change with the request

            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']

                # Check if the length is longer and the chain is valid
                if length > max_length and valid_chain(chain):
                    max_length = length
                    new_chain = chain

        # Replace our chain if we discovered a new, valid chain longer than ours
        if new_chain:
            self.chain = new_chain
            return True

        return False
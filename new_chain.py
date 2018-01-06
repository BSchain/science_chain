# -*- coding: utf-8 -*-
# @Time    : 05/01/2018 12:43 PM
# @Author  : 伊甸一点
# @FileName: new_chain.py
# @Software: PyCharm
# @Blog    : http://zpfbuaa.github.io

from time import time
import json
import hashlib as hasher
import os
from urllib.parse import urlparse
from uuid import uuid4
import requests

class Blockchain():
    def __init__(self):
        self.file_init()
        self.chain = []
        self.current_transactions = []
        self.last_block = []
        self.chain_length = 0
        self.last_diff = 5
        self.block_root = "blocks/"
        self.transactions_file = "current_transactions"
        self.nodes = set()

    def genersis_block(self,proof=100,previous_hash='1'):
        first_block = {
            'index': 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash,
        }
        self.save_block(block=first_block)
        return first_block

    def generate_new_block(self, proof, previous_hash=None): # generate new block from transaction
        block = {
            'index': self.chain_length + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.get_last_block()),
        }
        # Reset the current list of transactions
        self.reset_current_transactions()
        self.save_block(block)
        self.last_block = block
        self.chain_length += 1

    def register_node(self,address):
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    def valid_chain(self,chain): # to valid the whole chain
        last_block = chain[0]
        current_index = 1
        while current_index < len(chain):
            block = chain[current_index]
            print(f'{last_block}')
            print(f'{block}')
            print('\n-------------\n')
            if block['previous_hash'] != self.hash(last_block):
                return False
            if not self.valid_proof(last_block['proof'],block['proof']):
                return False
            last_block = block
            current_index +=1
        return True

    def resolve_conflicts(self):
        neighbours = self.nodes
        new_chain = None
        max_length = self.get_chain_length()
        for node in neighbours:
            response = requests.get(f'http://{node}/chain')
            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']

                if length > max_length and self.valid_chain(chain):
                    max_length = length
                    new_chain = chain
        if new_chain:
            self.chain = new_chain
            return True

        return False

    def file_init(self):
        if os.path.exists(self.block_root) == False:
            os.mkdir(self.block_root)
        if os.path.exists(self.transactions_file) == False:
            file = open(self.transactions_file, 'r')
            file.close()

    def get_chain_length(self): # next_block_index = chain_length + 1 = len(dir) + 1
        block_list = os.listdir(self.block_root)
        return len(block_list)

    def get_last_block(self): # read file and get the last block
        with open(self.block_root+str(self.chain_length)) as file_json:
            block = json.load(file_json)
        return block

    def get_whole_chain(self):
        whole_chain = []
        for height in range(self.chain_length):
            with open(self.block_root+str(height+1),'r') as f:
                block = json.load(f)
            whole_chain.append(block)
        return whole_chain

    def get_block_by_height(self,height): # read file and get one block
        block_height = {}
        if os._exists(self.block_root+ str(block_height)) == False or (height > self.chain_length):
            return block_height
        #assert height <= self.chain_length, ("height:",height," chain_length:",self.chain_length)
        with open(self.block_root+height,'r') as f:
            block_height = json.load(f)
        return block_height


    def get_current_diff(self): # generate the difficult to mine new block
        """
        # we can change diff or create diff rules.
        :return:
        """
        return self.last_diff

    def save_block(self,block): # when mine one block then update block and store new block to file
        index = block['index']
        with open(self.block_root+index, 'w') as json_file:
            json_file.write(json.dumps(block))

    def get_current_transactions(self): # generate transaction from file
        with open(self.transactions_file,'r') as f:
            current_transactions = json.load(f)
        return current_transactions

    def reset_current_transactions(self): # empty the old transactions
        with open(self.transactions_file) as file:
            file.truncate()
        self.current_transactions = []

    def store_one_transactions(self,one_transaction):
        with open(self.transactions_file,'a+') as json_file:
            json_file.write(json.dumps(one_transaction))

    def hash(self,block): # get block hash
        block_str = json.dumps(block, sort_keys=True).encode()
        return hasher.sha256(block_str).hexdigest()

    def proof_of_work(self,last_proof): # proof of work
        proof = 0
        while (self.valid_proof(last_proof, proof,self.get_current_diff()) is False):
            proof = proof + 1
        return proof

    @staticmethod
    def valid_proof(last_proof,proof,diff): # valid proof
        mine = f'{last_proof}{proof}'.encode()
        mine_hash = hasher.sha256(mine).hexdigest()
        diff_str = '0' * diff
        return mine_hash[:diff] == diff_str

class Block:
    def __init__(self):
        pass

    def new_block(self,index, proof, transactions, previous_hash, timestamp = None):

        """
        :param index: the block height
        :param proof: the proof to calculate the diff (using proof of work)
        :param transactions: (current_transactions)
        :param previous_hash: using hash(block)
        :param timestamp: time() or using passed parameter
        :return:
        """
        block = {
            'index': index,
            'timestamp': timestamp or time(),
            'proof': proof,
            'transactions' : transactions,
            'previous_hash': previous_hash,
        }
        return block

class Transaction:
    def __init__(self):
        pass

    def new_transaction(self, action=None, buyer=None, seller=None, credit=0, coin_in=None, coin_out=None, fee=0):

        """
        :param action: upload, buy, download, login, recharge, close
        :param buyer:  uuid
        :param seller: uuid
        :param credit: int
        :param coin_in: (should be the previous out)
        :param coin_out:
        :return:
        """
        transaction = {
            'action': action,
            # 'buyer': buyer,
            # 'seller': seller,
            'credir': credit,
            'coin_in': coin_in,
            'coin_out': coin_out,
            'fee': fee,
        }

        return transaction

    def save_transaction_to_file(self):
        pass


"""
how to track the coin flow?
"""
class Coin:
    def __init__(self):
        """
        TODO: need to think more
        """
        self.credit = 0 # total
        self.block_height = 0
        self.credit_left = 0
        self.credit_use = 0
        self.buyer = None
        self.seller = 0


# -*- coding: utf-8 -*-
# @Time    : 06/01/2018 1:02 PM
# @Author  : 伊甸一点
# @FileName: block.py
# @Software: PyCharm
# @Blog    : http://zpfbuaa.github.io

import config
import json
import os
from coin import *
from transaction import *
from time import time
from uuid import uuid4

class Block:
    def __init__(self):
        self.index = None
        self.timestamp = None
        self.prev_hash = None
        self.transactions = None
        self.nonce = None
        # just to calculate the self.hash
        self.hash = None

    def __repr__(self):
        pass

    def __eq__(self,other):
        return self.index == other.index and \
            self.timestamp == other.timestamp and \
            self.prev_hash == other.prev_hash and \
            self.transactions == other.transcations and \
            self.nonce == other.nonce

    def __ne__(self, other_block):
        return self.__eq__(other_block)

    def __gt__(self, other_block):
        return self.index > other_block.index

    def __lt__(self, other_block):
        return self.index < other_block.index

    def self_save(self):
        assert os.path.exists(config.BLOCK_SAVE_ROOT) , ('Blocks save root file not exist')

        save_block_path = config.BLOCK_SAVE_ROOT+ str(self.index) + config.BLOCK_SAVE_SUFFIX
        with open(save_block_path, 'w') as json_file:
            json_file.write(json.dumps(self.to_dict()))

    def to_dict(self):
        block = {
            'index': self.index,
            'timestamp': self.timestamp,
            'prev_hash': self.prev_hash,
            'transactions': self.transactions,
            'nonce': self.nonce,
        }
        return block

    def is_valid(self,prev_block):
        pass

    def new_block(self, index, timestamp, prev_hash, transactions, nonce):
        self.index = index
        self.timestamp = timestamp
        self.prev_hash = prev_hash
        self.transactions = transactions
        self.nonce = nonce

# test block
"""
action = 'buy'
seller = '111111'
buyer = '000000'

coin1 = Coin()
coin1.new_coin(1,1.2,buyer)

coin2 = Coin()
coin2.new_coin(2,2.2,buyer)

coin3 = Coin()
coin3.new_coin(3,3.4,seller)

in_coins = []
in_coins.append(coin1.to_dict())
in_coins.append(coin2.to_dict())

out_coins = []
out_coins.append(coin3.to_dict())

timestamp = time()
credit = 3.4
data_uuid = str(uuid4()).replace('-','')

ts1 = Transaction()
ts1.new_transaction(in_coins, out_coins, timestamp, action, seller, buyer, data_uuid, credit)

ts2 = Transaction()
ts2.new_transaction(in_coins, out_coins, timestamp, action, seller, buyer, data_uuid, credit)


index = 1
timestamp2 = time()
prev_hash = '1'

transactions = []
transactions.append(ts1.to_dict())
transactions.append(ts2.to_dict())
nonce = 100

block = Block()
block.new_block(index, timestamp2, prev_hash, transactions, nonce)
block.self_save()
print(block.to_dict())
"""


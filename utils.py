# -*- coding: utf-8 -*-
# @Time    : 06/01/2018 1:15 PM
# @Author  : 伊甸一点
# @FileName: utils.py
# @Software: PyCharm
# @Blog    : http://zpfbuaa.github.io

# TODO: add some methods to this file!
import json
import hashlib as hasher
from block import *

def hash_block(block): # json block
    block_str = json.dumps(block, sort_keys=True).encode() # here generate the block string
    return str(hasher.sha256(block_str).hexdigest())


def get_diff(block):
    """
    can use different strategy to generate the diff
    :param block:
    :return:
    """
    return 5 # diff now is set to 5


def proof_of_work(last_nonce, diff=5):
    nonce = 0
    while (valid_nonce(last_nonce, nonce, diff) is False):
        nonce = nonce + 1
    return nonce

def valid_nonce(last_nonce, nonce, diff=4):
    mine = f'{last_nonce}{nonce}'.encode()
    mine_hash = hasher.sha256(mine).hexdigest()
    return mine_hash[:diff] == '0' * diff


def valid_chain(chain):
    last_block = chain[0]
    current_index = 1

    while current_index < len(chain):
        block = chain[current_index]
        # print(f'{last_block}')
        # print(f'{block}')
        # print("\n-----------\n")
        # Check that the hash of the block is correct
        print(block['prev_hash'],hash_block(last_block))
        if block['prev_hash'] != hash_block(last_block):
            return False
        print(last_block['nonce'],block['nonce'])
        # Check that the Proof of Work is correct
        if not valid_nonce(last_block['nonce'], block['nonce']):
            print('here!!!')
            return False

        last_block = block
        current_index += 1
    return True

def json_to_bloc(block_json):
    """
    index
    timestamp
    transactions
    prev_hash
    nonce
    :param block_json:
    :return:
    """
    block = Block()
    block.index = block_json['index']
    block.timestamp = block_json['timestamp']
    block.transactions = block_json['transactions']
    block.prev_hash = block_json['prev_hash']
    block.nonce = block_json['nonce']
    # calculate the hash_self
    block.hash_self = hash_block(block_json)
    return block

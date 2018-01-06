# -*- coding: utf-8 -*-
# @Time    : 06/01/2018 1:02 PM
# @Author  : 伊甸一点
# @FileName: block.py
# @Software: PyCharm
# @Blog    : http://zpfbuaa.github.io

from time import time

class Block:
    def __init__(self):
        self.index = None
        self.timestamp = None
        self.prev_hash = None
        self.transactions = None
        self.nonce = None
        self.current_transactions = None

    def __repr__(self):
        pass

    def __eq__(self,other):
        pass

    def __ne__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __lt__(self, other):
        pass

    def self_save(self):
        pass

    def to_dict(self):
        pass

    def is_valid(self):
        pass

    def update_self_hash(self):
        pass

    def new_block(self):
        # TODO: need add parameter!
        pass



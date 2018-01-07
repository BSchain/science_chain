# -*- coding: utf-8 -*-
# @Time    : 06/01/2018 1:11 PM
# @Author  : 伊甸一点
# @FileName: transaction.py
# @Software: PyCharm
# @Blog    : http://zpfbuaa.github.io

class Transaction:
    def __init__(self):
        self.in_coins = None
        self.out_coins = None
        self.timestamp = None
        self.action = None
        self.seller = None
        self.buyer = None
        self.data_uuid = None
        self.credit = None

    def __eq__(self, other_ts):
        return self.in_coins == other_ts.in_coins and \
            self.out_coins == other_ts.out_coins and \
            self.timestamp == other_ts.timestamp and \
            self.action == other_ts.action and \
            self.seller == other_ts.seller and \
            self.buyer == other_ts.buyer and \
            self.data_uuid == other_ts.data_uuid and \
            self.credit == other_ts.credit

    def __ne__(self, other):
        return self.__eq__(other)

    def to_dict(self):
        transaction = {
            'in_coins': self.in_coins,
            'out_coins': self.out_coins,
            'timestamp': self.timestamp,
            'action': self.action,
            'seller': self.seller,
            'buyer': self.buyer,
            'data_uuid': self.data_uuid,
            'credit': self.credit,
        }
        return transaction

    # can change to init value
    def new_transaction(self, in_coins, out_coins, timestamp, action, seller, buyer, data_uuid, credit):

        self.in_coins = in_coins
        self.out_coins = out_coins
        self.timestamp = timestamp
        self.action = action
        self.seller = seller
        self.buyer = buyer
        self.data_uuid = data_uuid
        self.credit = credit



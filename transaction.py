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
        """

        :param in_coins:
        :param out_coins:
        :param timestamp:
        :param action:
        :param seller:
        :param buyer:
        :param data_uuid:
        :param credit:
        :return:
        """
        self.in_coins = in_coins
        self.out_coins = out_coins
        self.timestamp = timestamp
        self.action = action
        self.seller = seller
        self.buyer = buyer
        self.data_uuid = data_uuid
        self.credit = credit

    def valid_transaction(self):
        if self.action == 'upload':
            assert self.timestamp is not None, ('Upload data, timestamp should not be None')
            assert self.buyer is None, ('Upload data, buyer should be None, buyer:',self.buyer)
            assert self.seller is not None, ('Upload data, seller should not be None')
            assert self.in_coins is None, ('Upload data, in_coins should be None, in_coins',self.in_coins)
            assert self.credit >=0, ('Upload data, should have (+) credit reward')
            assert self.out_coins is not None, ('Upload data, out_coins should not be None')
            assert self.out_coins.owner == self.seller, ('Upload data, out_coins owner:',self.out_coins.owner,'seller:',self.seller)
            assert self.out_coins.number_coin == self.credit, ('Upload data, out_coins number_coin:',self.out_coins.number_coin,'credit:',self.credit)
            assert self.data_uuid is not None, ('Upload data, data_uuid should not be None')
            return True
        elif self.action == 'buy': #TODO: need to fix those logist
            pass
        elif self.action == 'login':
            pass
        elif self.action == 'download':
            pass
        else:
            pass

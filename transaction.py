# -*- coding: utf-8 -*-
# @Time    : 06/01/2018 1:11 PM
# @Author  : 伊甸一点
# @FileName: transaction.py
# @Software: PyCharm
# @Blog    : http://zpfbuaa.github.io

class Transaction:
    def __init__(self):
        self.in_address = None
        self.in_coin = None
        self.out_coin = None
        self.timestamp = None
        self.action = None
        self.seller = None
        self.buyer = None
        self.data_uuid = None
        pass

    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass

    def to_dict(self):
        pass

    def new_transaction(self,in_address, in_coin, out_coin, time_stamp, action, seller, buyer, data_uuid):
        """

        :param in_address:
        :param in_coin:
        :param out_coin:
        :param time_stamp:
        :param action:
        :param seller:
        :param buyer:
        :param data_uuid:
        :return:
        """
        # TODO: need to add parameter
        pass

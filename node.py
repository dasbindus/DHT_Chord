__author__ = 'baidong'


class NodeInfo:
    node_id = "-1"
    pass


class Node:
    node_id = "-1"
    data = {}
    finger = []
    predecessor = None

    def __init__(self, node_id=None, fingertable=None):
        self.node_id = node_id
        self.finger = fingertable
        self.data = {}

    def setsuccessor(self, sucessor):
        self.finger = []
        self.finger.insert(0, sucessor)

    def insert_data(self, key, value):
        self.data[key] = value
        print 'Insert data (node_id: %s) [%s]:[%s]' % (self.node_id, key, value)

    def find_data(self, key):
        data = self.data.get(key, None)
        return data

    def __str__(self):
        msg = '==>> I\'m node:%s ' % self.node_id
        if self.predecessor is None:
            msg += 'I have no predecessor '
        else:
            msg += 'Predecessor:%s ' % self.predecessor.node_id
        if self.finger is None or self.finger[0] is None:
            msg += 'I have no successors '
        else:
            msg += 'Sucessor:%s ' % self.finger[0].node_id
        return msg

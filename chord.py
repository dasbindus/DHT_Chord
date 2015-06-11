from node import Node, NodeInfo
from utils import gen_rand_ip, hash_data

__author__ = 'baidong'


NUMBER_OF_NODES = 10

nodes = []

# add node before find(strhash)
def join(strhash=None):
    key = hash_data(gen_rand_ip())
    print("Join with index %s" % key)
    if not len(nodes):
        node = Node(key)
        node.predecessor = node
        node.setsuccessor(node)
        nodes.append(node)
    else:
        # root = find(strhash)
        root = rootnode().predecessor
        print("Root node %s" % root)
        successor = root.finger[0]

        while root != successor and key < successor.node_id:
            print("%s < %s" % (key, successor.node_id))
            successor = successor.finger[0]
        successor = successor.predecessor
        print("Set %s as predecessor of %s" % (key, successor.node_id))

        newnode = Node(key)
        newnode.setsuccessor(successor)
        if successor.predecessor is not None:
            newnode.predecessor = successor.predecessor
            successor.predecessor.setsuccessor(newnode)
            successor.predecessor = newnode
        else:
            # addition of second node in network
            newnode.predecessor = successor
            successor.predecessor = newnode
            successor.setsuccessor(newnode)
        nodes.append(newnode)


# insert data
def insert(strhash, key, data):
    hashkey = hash_data(key)
    print("Hashed key %s" % hashkey)
    root = find(strhash)
    successor = find(strhash).finger[0]
    while root != successor and hashkey < successor.node_id:
        successor = successor.finger[0]
    successor.insert_data(key, data)


# find node
def find(strhash):  # still linear
    for node in nodes:
        if node.node_id == strhash:
            return node
    return None


# find data
def finddata(strhash, key):  # still linear
    root = find(strhash)
    successor = find(strhash).finger[0]
    hashkey = hash_data(key)
    while root != successor and hashkey < successor.node_id:
        successor = successor.finger[0]
    print("searching in %s" % successor.node_id)
    return successor.find_data(key)


# leave network
def leave(strhash):
    pass


def rootnode():
    root = nodes[0]
    while root.node_id < root.finger[0].node_id:
        root = root.finger[0]
    return root.finger[0]


def setupFT():
    root = rootnode()

    print("Root node %s " % root)
    for node in nodes:
        pass
        # node.setupFT(root)


def cwshow():
    node = rootnode()
    print("Root node %s" % node)
    print("Presenting node:%s " % (str(node)))
    node = node.finger[0]
    while node != rootnode():
        print("Presenting node:%s " % (str(node)))
        node = node.finger[0]


def showdependency():
    for index, node in enumerate(nodes):
        print("Presenting nodes[%i]:%s " % (index, str(node)))


if __name__ == '__main__':
    # MAIN PART
    print '\n====================== init:add N1 ====================\n'
    join()

    print '\n====================== add N2 =========================\n'
    join(nodes[0].node_id)
    cwshow()

    print '\n====================== add N3 =========================\n'
    join(nodes[1].node_id)
    cwshow()

    print '\n====================== add (K,V) ======================\n'
    # TODO need to mod 2^m, make sure keys are auto placed.
    insert(nodes[1].node_id, "key", "value")
    # insert(nodes[1].node_id, "key2", "value2")
    # insert(nodes[1].node_id, "key3", "value3")

    print '\n====================== add N4 =========================\n'
    join(nodes[2].node_id)
    cwshow()

    print '\n====================== find data ======================\n'
    print("Data: %s" % str(finddata(nodes[1].node_id, "key")))
    print("Data: %s" % str(finddata(nodes[1].node_id, "key2")))
    print("Data: %s" % str(finddata(nodes[1].node_id, "key3")))

    # join()

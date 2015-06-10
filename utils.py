import hashlib

__author__ = 'baidong'


ctr = 99

def gen_rand_ip():
    global ctr
    ctr += 1
    print 'Createing ip %s' % ('192.168.1.%s' % ctr)
    return '192.168.1.%s' % ctr

def hash_data(msg):
    m = hashlib.sha1(bytes(msg))
    return m.hexdigest()

# for test
print hash_data('asdasd')
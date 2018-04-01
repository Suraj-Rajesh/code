class FOSS(object):

    def __init__(self, ip_addr):
        self.ip_addr = ip_addr
        self.name = 'route'

    def __len__(self):
        return len(self.ip_addr)

if __name__ == '__main__':
    f = FOSS([1,2,3])
    print len(f)
    print f.ip_addr

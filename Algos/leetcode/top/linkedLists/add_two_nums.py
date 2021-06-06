# https://leetcode.com/problems/add-two-numbers/

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def addTwoNums(l1, l2):
    carry = 0
    dummy = Node(0)
    tail = dummy

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        carry, digit = divmod(val1 + val2 + carry, 10)

        # alternately,
        #
        # added = val1 + val2 + carry
        # carry = added // 10
        # digit = added % 10
        #
        # hence the name, divmod() - we do division & mod
        #

        tail.next = Node(digit)
        tail = tail.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None 
    return dummy.next

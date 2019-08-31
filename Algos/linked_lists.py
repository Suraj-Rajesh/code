class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

    def insert(self, data):
        cur = self
        while cur.next is not None:
            cur = cur.next

        cur.next = Node(data)

    def printer(self):
        cur = self
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def reverse(self):
        prev = None
        cur = self

        while cur is not None:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        return prev

    def check_palindrome(self):
        stack = []

        cur = self
        while cur is not None:
            stack.append(cur.data)
            cur = cur.next

        cur = self
        while cur is not None:
            if cur.data != stack.pop():
                return False
            else:
                cur = cur.next
        else:
            return True


    def check_palindrome_2(self):
        odd = False
        slow = self
        fast = self
        prev = None

        while fast.next is not None and fast.next.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if fast.next is None:
            odd = True
            prev.next = None
            mid = slow
            head2 = slow.next
        else:
            mid = None
            head2 = slow.next
            prev = slow
            prev.next = None

        head2 = head2.reverse()

        cur1 = self
        cur2 = head2
        pal = True
        while cur1 is not None:
            if cur1.data != cur2.data:
                pal = False
                break
            else:
                cur1 = cur1.next
                cur2 = cur2.next

        head2 = head2.reverse()
        if odd:
            prev.next = mid
            mid.next = head2
        else:
            prev.next = head2

        return pal

head = Node(1)
head.insert(2)
head.insert(2)
head.insert(3)
print('########')
#head = head.reverse()
#head.printer()
print head.check_palindrome_2()
head.printer()

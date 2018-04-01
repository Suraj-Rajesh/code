class Node(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        elif data > self.data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)

    def search(self, value):
        if self.data == value:
            return True

        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False

        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False


    def inorder(self):
        if self.left:
            self.left.inorder()
        print self.data
        if self.right:
            self.right.inorder()

    def insert_left(self, data):
        if self.left:
            self.left.insert_left(data)
        else:
            self.left = Node(data)

    def insert_right(self, data):
        if self.right:
            self.right.insert_right(data)
        else:
            self.right = Node(data)

    def check_if_bst_1(self, prev=None):
        """Do inorder traversal. If a tree is BST, then inorder traversal 
           should yield ascending order. If not, then tree is not BST"""
        if self.left:
            ret = self.left.check_if_bst(prev)
            # here, need to stop recursion and return only if ret == no.
            # else, we need to continue to recurse
            if ret == 'no':
                return ret

        if prev:
            if self.data > prev:
                prev = self.data
            else:
                return 'no'
        else:
            prev = self.data

        if self.right:
            ret = self.right.check_if_bst(prev)
            # here, need to stop recursion and return only if ret == no.
            # else, we need to continue to recurse
            if ret == 'no':
                return ret

        # after all recursion is done & no 'no' returned, return 'yes'
        return 'yes'


    def check_if_bst_2(self, maximum, minimum):
        left_ret = True
        right_ret = True

        if self.data < maximum and self.data > minimum:
            if self.left:
                left_ret = self.left.check_if_bst_2(self.data, minimum)

            if self.right:
               right_ret = self.right.check_if_bst_2(maximum, self.data)

            return left_ret and right_ret
        else:
            return False


if __name__ == '__main__':
    bst = Node(3)
#    bst.insert(2)
   # bst.inorder()
    bst.insert_left(2)
    bst.insert_right(5)
    bst.inorder()
    print bst.check_if_bst_2(100, 0)
    print bst.search(7)

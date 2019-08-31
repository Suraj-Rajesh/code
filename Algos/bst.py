prev=None

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

    # L N R
    def inorder(self):
        if self.left:
            self.left.inorder()
        print self.data
        if self.right:
            self.right.inorder()

    def inorder_iterative(self):
        # try to see how, recursive LNR is done iteratively
        
        stack = Stack()
        current = self

        # if no Node and stack is empty, it implies nothing to process
        while current is not None or not stack.is_empty():
            # keep on pushing left items to Stack (this is the L in LNR),
            # recursing deeper on the Left
            while current is not None:
                stack.push(current)
                current = current.left
            
            # this is the N in LNR, since we recursed till the end above
            current = stack.pop()
            print current.data

            # this is the R in LNR, meaning, go to right and then again do, LNR
            current = current.right
    
    # N L R
    def preorder(self):
        print self.data
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def preorder_iterative(self):
        # 1. Create stack by adding root element
        # 2. Until stack is empty, do,
        #        - Pop element and print
        #        - (IMPORTANT): Add popped element's right and left(notice the order,
        #           it is right, then left, not left and right) to stack

        # HINT: PREorder. You can think of PRE as something that comes before. So, a
        # normal order is Left then Right. When you see PRE, think, Right, then Left.
        # So, always add Right first and then Left to stack in every iteration.
        stack = Stack()
        stack.push(self)

        while not stack.is_empty():
            popped_node = stack.pop()
            print popped_node.data
            
            # IMPORTANT (see HINT)
            if popped_node.right:
                stack.push(popped_node.right)
                
            # IMPORTANT (see HINT)
            if popped_node.left:
                stack.push(popped_node.left)
    
    
    # L R N
    def postorder(self):
        if self.left:
            self.left.postorder()

        if self.right:
            self.right.postorder()

        print self.data

    def postorder_iterative(self):
        # 1. Create stack by adding root element
        # 2. Until stack is empty, do,
        #        - Pop element and add it to front of result(see HINT below)
        #        - Add popped element's left and right to stack

        # HINT: POSTorder. While POSTing mails, a postman adds your
        # posts to the front of the mailbox. Similarly, while creating the
        # result array, add elements to the front(do not append to the back)
        res_list = []
        stack = Stack()
        stack.push(self)

        while not stack.is_empty():
            popped_node = stack.pop()
            # IMPORTANT (see HINT)
            res_list.insert(0, popped_node.data)

            if popped_node.left:
                stack.push(popped_node.left)

            if popped_node.right:
                stack.push(popped_node.right)

        return res_list
                
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

    def check_if_bst_1(self):
        global prev
        """Do inorder traversal. If a tree is BST, then inorder traversal 
           should yield ascending order. If not, then tree is not BST"""
        if self.left:
            ret = self.left.check_if_bst_1()
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
            ret = self.right.check_if_bst_1()
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


    def range(self, begin, end):
        if self.data > begin:
            if self.left:
                self.left.range(begin, self.data)
        if self.data <= end:
            print self.data
            if self.right:
                self.right.range(self.data, end)

 def is_mirror(tree1, tree2):
    # both trees are None, symmetric
    if tree1 is None and tree2 is None:
        return True

    # one tree exists while the other is None, Assymetric
    if tree1 is None or tree2 is None:
        return False

    # both tree values are same, recurse
    if tree1.data == tree2.data:
        check1 = is_mirror(tree1.left, tree2.right)
        check2 = is_mirror(tree1.right, tree2.left)
        return check1 and check2
    # tree values differ, return False
    else:
        return False

def is_symmetric(tree):
    return is_mirror(tree, tree)

# depth of a tree
def depth(tree):
    if tree is None:
        return 0

    left_depth = depth(tree.left)
    right_depth = depth(tree.right)

    return max(left_depth, right_depth) + 1

def invert(tree):
    if tree is None:
        return

    invert(tree.left)
    invert(tree.right)

    tree.left, tree.right = tree.right, tree.left

if __name__ == '__main__':
    bst = Node(3)
#    bst.insert(2)
   # bst.inorder()
    bst.insert_left(2)
    bst.insert_right(5)
#    bst.inorder()
    bst.range(2,4)

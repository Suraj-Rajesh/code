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
        if self:
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
        if self:
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
        if self:
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

        if minimum < self.data < maximum:
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
    
   
def merge(tree1, tree2):
    if tree1 is None:
        return tree2

    if tree2 is None:
        return tree1

    tree1.data += tree2.data
    tree1.left = merge(tree1.left, tree2.left)
    tree1.right = merge(tree1.left, tree2.right)

    return tree1

#
# Is BST or not
#
def isBSTHelper(root, minval, maxval):
    if root is None:
        return True

    if minval < root.val < maxval:
        return isBSTHelper(root.left, minval, root.val) and isBSTHelper(root.right, root.val, maxval)
    else:
        return False
 
def isBST(root):
    minval, maxval = float('-inf'), float('inf')
    return isBSTHelper(root, minval, maxval)

#
# Inorder successor
#
def minval(node):
    if node is None: return None

    while node.left:
        node = node.left
    return node

def inorder_successor(root, node):
    # if node has right subtree, then inorder successor is min leftmost
    # value of right subtree
    if node.right:
        return minval(node.right)

    # if we reached here, it means node doesn't have right subtree
    
    # set successor to None, as we may not find any successor at all
    # (this happens if node is rightmost node)
    successor = None
    
    # modified search 
    while root is not None:
        # go deep in left subtree, setting & narrowing on successor
        if node.val < root.val:
            successor = root
            node = node.left
        # node is greater than root, then we need to find in right subtree
        elif node.val > root.val:
            node = node.right
        else:
            # its important to break here, as when node == root, we are done,
            # else, this loop doesn't terminate
            break
    return successor

def insert(root, val):
    if root is None:
        return TreeNode(val)

    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    return root

def inorder_successor_2(root, node):
    """in-order successor of a node is one that appears next during in-order traversal"""
    successor = None
    while root:
        #
        # if node value greater or equal to current node, it means, successor
        # is somewhere on the right subtree. Note the >= instead of >
        #
        if node.val >= root.val:
            root = root.right
        #
        # if node value is less than current node, then, current node being greater
        # than this node value is a potential successor. Keep searching on the left
        # subtree
        #
        else:
            successor = root
            root = root.left
    return successor

def lca(root, p, q):
    if root is None:
        return None

    if p.val < root.val and q.val < root.val:
        return lca(root.left, p, q)
    elif p.val > root.val and q.val > root.val:
        return lca(root.right, p, q)
    else:
        #
        # if either of above cases are not hit and we are here, it could be either one of two
        #   
        #   1. root is the LCA, and it cleaves p and q, as in, either
        #        a. p.val < root.val < q.val
        #        b. q.val < root.val < p.val
        #
        #   2. root itself is one of these two nodes, hence this node itself is the LCA, as in, either,
        #        a. root.val == p.val
        #        b. root.val == q.val
        #
        return root

def delete_node(root, val):
    def mintree(node):
        while node.left is not None:
            node = node.left
        return node

    if root is None: return None

    if val < root.val:
        root.left = delete_node(root.left, val)
    elif val > root.val:
        root.right = delete_node(root.right, val)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        # this node has both child's, so find inorder successor
        # note that, this node has a right child, so inorder is just the
        # minimum value of right subtree
        inorder_successor = mintree(root.right)
        root.val = inorder_successor.val
        root.right = delete_node(root.right, inorder_successor.val)
    return root

if __name__ == '__main__':
    bst = Node(3)
#    bst.insert(2)
   # bst.inorder()
    bst.insert_left(2)
    bst.insert_right(5)
#    bst.inorder()
    bst.range(2,4)

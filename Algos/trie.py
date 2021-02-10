#
# What is Trie?
#

# It is a tree-like structure where each node represents a single character of a given string. And unlike binary trees, a node may have more than two children.
#
# Let us analyze an example. We assume that we are starting from scratch, which means we only have an empty root node and nothing else. We start with the word "buy". Our implementation of Trie does not store a character in the root node. So we add the first character, i.e. "b" as a child node of it. We do it as it did not have that character in any of the children. Otherwise, we would have skipped adding the child node and just incremented the counter of the child node,  as we already have it. Then comes the character "u". When adding this character, one thing we must be aware of, is the fact that we need to search whether "u" is present in any child nodes of "b" (our last added node) and not the root. And the same is true for "y".

class TrieNode(object):
    def __init__(self, char):
        self.char = char
        self.children = []
        self.counter = 1
        self.word_finished = False

#
#    The first thing to consider is to how we add new words to a Trie. The add function does exactly that. The way it works is very simple. It takes as an input the root node (the one without any character value assigned to it) and the whole word.
#    1. It then iterates through the word, one character at a time, starting with the first character.
#    2. It checks whether the current "node" (At the beginning of the process which points to root node) has a child node with that character.
#    3. If found, it just increments the counter of that node to indicate that it has got a repeated occurrence of that character.
#    4. If not found then it simply adds a new node as a child of the current node.
#    5. In both cases (4 & 5), it assigns the child node as the "current node" (which means in the next iteration it will start from here) before it starts with the next character of the word.
#    6. One more thing it does also is to mark the end of a word once the whole process is finished. Which means, each leaf node of  the Trie will have word_finished as True.
#
# That is all about adding a word in a Trie.
#

def add(root, word):
    node = root

    for char in word:
        found_in_child = False
        # search for character in child of current node
        for child in node.children:
            if char == child.char:
                child.counter += 1
                # mark as found, so, we need not look for it once
                # we exit this for loop
                found_in_child = True
                # now we need to traverse down through the child node
                node = child
                break

        # not found in children, add new node
        if not found_in_child:
            newnode = TrieNode(char)
            node.children.append(newnode)
            # have to traverse down here, point node to newnode
            node = newnode

    # done adding word
    node.word_finished = True

#
# To search for a prefix
#

#
#    1. It starts with the root node and the prefix to search for.
#    2. It takes one character at a time from the prefix and searches through the children of the "current node" (at the beginning which points to the root node) to find a node containing that character.
#    3. If found, it reassigns that child node as the "current node" (which means in the next iteration step it will start from here)
#    4. If not found then it returns False to indicate that the prefix does not exist.
#

def find_prefix(root, prefix):
    """
    Checks & returns

        1. If the prefix exists in any of the words we added so far
        2. If yes, then how may words actually have the prefix
    """
    if not root.children:
        return (False, 0)

    node = root
    for char in prefix:
        for child in node.children:
            if char == child.char:
                node = child
                # found this char, go to next char in the prefix
                break
        else:
            return (False, 0)

    return (True, node.counter)

if __name__ == '__main__':
    root = TrieNode('*')
    add(root, 'hackathon')
    add(root, 'hack')

    print(find_prefix(root, 'hac'))
    print(find_prefix(root, 'hack'))
    print(find_prefix(root, 'hackathon'))
    print(find_prefix(root, 'ha'))
    print(find_prefix(root, 'h'))
    print(find_prefix(root, 'hacka'))
    print(find_prefix(root, 'uhacka'))
    print(find_prefix(root, 'hammers'))

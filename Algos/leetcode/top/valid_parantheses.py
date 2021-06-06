#
# https://leetcode.com/problems/valid-parentheses/
#

expr = '{3 * [1 + 5(6 + 8) ]}'

braces = {
    '{': '}',
    '[': ']',
    '(': ')'
}

def findBalanced(expr):
    stack = []
    for c in expr:
        if c in '{}[]()':
            if c in braces:
                stack.append(braces[c])
            else:
                if c != stack.pop():
                    return False
    return True if not stack else False


print(findBalanced(expr))

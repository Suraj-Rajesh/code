#
# Pythonic way of iterating over a large file, by reading it chunk by chunk
#

from hashlib import sha256
from functools import partial

#
# KEY POINT
# 

# To call 'iter' over a function, the function needs to take no args.
# But, in our case, we need to iter over the function, f.read(block_size),
# which takes one argument. What do we do?

#
# SOLUTION 1
#

# Use lambda function, and call f.read(block_size) inside the body
# of the lambda function, so,
#
#   lambda : f.read(block_size) 
#
#                ^
#               / \
#               |||
#               ||| 
#
#   def anonymous_lambda_function():
#       return f.read(block_size)
#
#   Now, we can iterate over it. Cool !!

def sha256_file(filename, block_size = 64*1024):
    digest = sha256()

    with open(filename, 'rb') as f:
        for chunk in iter(lambda : f.read(block_size), b''):
            digest.update(chunk)

    print digest.hexdigest()

sha256_file('dummy.txt')

#
# Solution 2:
#

# To convert a function with more args to none or lesser arguments, we can
# use 'partial'.
# 
#  f.read(block_size) <==> partial(f.read, block_size)
#

def new_sha256_file(filename, block_size=64*1024):
    digest = sha256()

    with open(filename, 'rb') as f:
        for chunk in iter(partial(f.read, block_size), b''):
            digest.update(chunk)

    print digest.hexdigest()

new_sha256_file('dummy.txt')

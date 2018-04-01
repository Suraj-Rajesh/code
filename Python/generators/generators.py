# 
# Generators
#

# Any function with a yield becomes a generator

# Useful to generate lazily on the fly rather than create and keep in
# memory like a list. Example below is an infinte number generator.

def no_generator(i = 0):
    while True:
        yield i
        i = i + 1

# using the generator
for no in no_generator(i=5):
    if no < 10:
        print no
    else:
        break

# list comprehension, BAD (creates entire list in memory first)
for item in [x*10 for x in range(5)]:
    print item

# generator expressions, GOOD (generates values on the fly)
for item in (x*10 for x in range(5)):
    print item

# getting sum
res = sum([x + 1 for x in range(5)])
print res

# getting sum, BETTER
res = sum(x + 1 for x in range(5))
print res

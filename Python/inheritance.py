class SuperClass(object):
    def __init__(self, name, *args):
        self.name = 'varun'

class SubClass(SuperClass):

    def __init__(self, name, errno=0):
        self.errno = errno

# Can either use the commented line below (OR) subsequent uncommented line
# to initialize the superclass.
#     SuperClass's __init__ takes, name and *args, so we have to pass, name.
# In addition to name, we can pass other args as well, if we want to. If however,
# SuperClass's  __init__ was, __init__(self, name), then it would have been mandatory
# to only pass name in the below initializations.

#       SuperClass.__init__(self, name)
        super(SubClass, self).__init__(name, errno)


s = SubClass('suraj', errno=1)
print s.name

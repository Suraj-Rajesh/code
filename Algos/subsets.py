s = [1, 2, 3]

class SetOps(object):
    def __init__(self, s):
        self.set = s

    def subsets(self):
        n = len(self.set)

        # each set has 0 to 2^(n - 1) subsets (total of 2^n)
        for i in range(pow(2, n)):
            subset = []

            # this bit masks each of n bits to find which element
            # to be included. 1 -> include, 0 - >exclude
            for j in range(n):
                if i & (1 << j) > 0:
                    subset.append(self.set[j])

            print subset

    def sum_subsets(self):
        sum = 0
        n = len(self.set)

        # the logic is, when we take all subsets, each element appears
        # 2^(n - 1) times
        for elem in self.set:
            sum += pow(2, n - 1)*elem

        return sum


setobj = SetOps(s)
setobj.subsets()
print setobj.sum_subsets()

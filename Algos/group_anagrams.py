from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        hashmap = defaultdict(list)
        for st in strs:
            stsorted = sorted(st)
            hashmap[tuple(stsorted)].append(st)
        return hashmap.values()

        res = []
        for _, val in hashmap.items():
            res.append(val)

        return res


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

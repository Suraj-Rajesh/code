#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
#

def lengthOfLongestNonRepeatSubstring(s):
    maxlen = 0
    begin = end = 0
    seen = set()

    while end < len(s):
        char = s[end]
        #
        # keep adding new chars and expand the window
        #
        if char not in seen:
            seen.add(char)
            maxlen = max(maxlen, end - begin + 1)
            end += 1
        else:
            #
            # shrink the window until char is no more seen
            # note: char = s[end], not s[begin]
            # 
            while char in seen:
                seen.remove(s[begin])
                begin += 1
    return maxlen

def longestNonRepeatSubString(s):
    if not s:
        return ''

    #
    # since string is non-empty & has atleast one char, that one char is can be
    # considered a valid solution, hence, starting, indices with [0, 0]
    #
    indices = [0, 0]
    seen = set()
    begin = end = 0

    while end < len(s):
        char = s[end]
        if char not in seen:
            seen.add(char)
            if end - begin + 1 > indices[1] - indices[0] + 1:
                indices = [begin, end]
            end += 1
        else:
            while char in seen:
                seen.remove(s[begin])
                begin += 1
    return s[indices[0]:indices[1] + 1]

print(longestNonRepeatSubString('abcabcbb'))

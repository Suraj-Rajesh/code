#
# https://leetcode.com/problems/merge-intervals/
#

intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[1, 4], [4, 5]]
intervals = [[1, 4], [2, 3]]

def mergeIntervals(intervals):
    out = []

    # sort by start time
    for start, end in sorted(intervals, key = lambda interval: interval[0]):
        # if out is empty (or) no overlap then just append interval
        if not out or out[-1][1] < start:
            out.append([start, end])
        # there is an overlap, last out end time should be max of itself
        # & current end time. For example, if [[1, 4], [2, 3]]
        # then output should be [[1, 4]], not [[1, 3]]
        else:
            out[-1][1] = max(out[-1][1], end)
    return out

print(mergeIntervals(intervals))

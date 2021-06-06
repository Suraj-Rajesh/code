#
# https://leetcode.com/problems/meeting-rooms-ii/
#

import heapq

intervals = [[0, 30], [5, 10], [15, 20]]
intervals = [[7, 10], [2, 4]]

def num_meetings(interals):
    if not intervals:
        return 0

    intervals.sort(key=lambda interval: interval[0])
    end_times = [intervals[0][1]]
    for interval in intervals[1:]:
        if interval[0] > end_times[0]:
            heapq.heappop(end_times)
        heapq.heappush(end_times, interval[1])
    return len(end_times)

print(num_meetings(intervals))

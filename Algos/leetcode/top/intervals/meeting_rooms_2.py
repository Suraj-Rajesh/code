#
# https://leetcode.com/problems/meeting-rooms-ii/
#

import heapq

intervals = [[0, 30], [5, 10], [15, 20]]
intervals = [[7, 10], [2, 4]]

def minMeetingRooms(intervals):
        if not intervals:
            return 0
        
        BEGIN, END = 0, 1
        
        # sort the meetings in increasing order of their start time
        intervals.sort(key=lambda interval: interval[0])

        # initialize end times priority queue with first meeting
        end_times = [intervals[0][END]]

        # for all remaining meeting rooms
        for i in range(1, len(intervals)):
            # if room due to free up earliest is free, assign that room
            # note, since, end_times is a min heap, first element will be the 
            # smallest element. If meeting begin time is less than this value,
            # then it would be less for all other values in end_times
            if intervals[i][BEGIN] >= end_times[0]:
                # we can use the available meeting room, so pop end time for that
                # meeting room & update new end time
                heapq.heappushpop(end_times, intervals[i][1])
            else:
                # conflict, add new meeting 
                heapq.heappush(end_times, intervals[i][END])
                
            #
            # can also be slightly optimized as
            #
            # if intervals[i][BEGIN] >= end_times[0]:
            #    heapq.heappop(end_times)
            # heapq.heappush(end_times, intervals[i][END])

        # size of the heap gives number of rooms allocated
        return len(end_times)

print(minMeetingRooms(intervals))

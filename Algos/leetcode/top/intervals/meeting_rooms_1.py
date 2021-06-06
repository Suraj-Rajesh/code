#
# https://leetcode.com/problems/meeting-rooms
#

intervals = [[0,30],[5,10],[15,20]]
intervals = [[7,10],[2,4]]

def canAttendMeetings(intervals):
    # sort by start time
    intervals.sort(key = lambda interval: interval[0])
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    return True

print(canAttendMeetings(intervals))

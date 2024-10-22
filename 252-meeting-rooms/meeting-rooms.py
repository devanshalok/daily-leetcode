class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # sort the intervals to get the first time of intervals
        intervals.sort()

        # loop through the intervals 
        for i in range(len(intervals)-1):
            # if the start of the interval is greater than start of next interval, it means the
            # meeting times and overlap and we can return False, otherwise True
            if intervals[i][1]>intervals[i+1][0]:
                return False
        return True



        
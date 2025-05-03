class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda i:i[0])
        answer=[intervals[0]]

        for start,end in intervals[1:]:
            lastEnd=answer[-1][-1]

            if start<=lastEnd:
                answer[-1][1]=max(lastEnd,end)

            else:
                answer.append([start,end])

        return answer

        





   
            

        



        
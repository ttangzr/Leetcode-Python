# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/31 15:38


from typing import List
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # method-1: queue
        # 先考虑早开始的会议
        intervals.sort(key=lambda x: x[0])
        room = [intervals[0][1]]
        for i in range(1, len(intervals)):
            curr_start, curr_end = intervals[i]
            is_empty = False
            # 每次安排都检查是否有空会议室
            for r in range(len(room)):
                room_end = room[r]
                if curr_start >= room_end:
                    room[r] = curr_end
                    is_empty = True
                    break
            if not is_empty:
                room.append(curr_end)
        return len(room)

        # method-2: 最小堆/优先队列
        intervals.sort(key=lambda x: x[0])
        # 先放置end
        room = []
        heapq.heappush(room, intervals[0][1])
        for itv in intervals[1:]:
            # end比start早，说明会议结束，pop
            if room[0] <= itv[0]:
                heapq.heappop(room)
            heapq.heappush(room, itv[1])
        return len(room)


if __name__ == '__main__':
    obj = Solution()
    intervals = [[0, 30], [5, 10], [15, 20]]
    print(obj.minMeetingRooms(intervals))

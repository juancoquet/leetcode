# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/

import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]) -> None:
        self._k = k
        self._heap = nums
        heapq.heapify(self._heap)
        while len(self._heap) > k:
            self.pop()

    def add(self, val: int) -> int:
        if len(self._heap) < self._k:
            heapq.heappush(self._heap, val)
        elif val > self.peek():
            heapq.heappushpop(self._heap, val)
        return self.peek()

    def pop(self) -> int:
        num = self._heap.pop(0)
        heapq.heapify(self._heap)
        return num

    def peek(self) -> int:
        return self._heap[0]

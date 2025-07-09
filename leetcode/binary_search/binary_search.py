from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return _search(nums, target)


def _search(nums: List[int], target: int, offset: int = 0) -> int:
    if not nums:
        return -1
    mid = len(nums) // 2
    if nums[mid] == target:
        return mid + offset
    if nums[mid] > target:
        return _search(nums[:mid], target, offset)
    return _search(nums[mid + 1 :], target, offset + mid + 1)

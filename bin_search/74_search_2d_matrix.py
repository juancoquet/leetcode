class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        top, bot = 0, len(matrix) - 1
        while top <= bot:
            mid = (top + bot) // 2

            if mid == len(matrix) - 1 or matrix[mid][0] <= target < matrix[mid + 1][0]:
                row = matrix[mid]
                l, r = 0, len(row) - 1

                while l <= r:
                    m = (l + r) // 2
                    if row[m] == target:
                        return True
                    elif row[m] > target:
                        r = m - 1
                    else:
                        l = m + 1
                return False

            elif matrix[mid][0] > target:
                bot = mid - 1
            else:
                top = mid + 1

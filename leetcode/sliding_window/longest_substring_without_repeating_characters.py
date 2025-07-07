# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


from typing import Dict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen: Dict[str, int] = {}  # {char: idx}
        l, longest = 0, 0
        for r, char in enumerate(s):
            if char in seen and seen[char] >= l:
                l = seen[char] + 1
            seen[char] = r
            longest = max(longest, r - l + 1)

        return longest

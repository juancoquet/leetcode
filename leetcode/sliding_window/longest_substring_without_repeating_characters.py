# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        l, r = 0, 1
        longest = 0
        while r <= len(s):
            if has_dupes(s[l:r]):
                l += 1
                r += 1
            else:
                longest = max(longest, r - l)
                r += 1
        return longest


def has_dupes(s: str) -> bool:
    return len(set(s)) != len(s)

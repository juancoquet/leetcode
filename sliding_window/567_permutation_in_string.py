# https://leetcode.com/problems/permutation-in-string/description/

import string


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        chars = {ch: 0 for ch in string.ascii_lowercase}
        window_chars = chars.copy()
        for i in range(len(s1)):
            chars[s1[i]] += 1
            window_chars[s2[i]] += 1

        matches = 0
        for ch1, ch2 in zip(chars.values(), window_chars.values()):
            if ch1 == ch2:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            window_chars[s2[l]] -= 1
            if window_chars[s2[l]] == chars[s2[l]] - 1:
                matches -= 1
            elif window_chars[s2[l]] == chars[s2[l]]:
                matches += 1
            l += 1

            window_chars[s2[r]] += 1
            if window_chars[s2[r]] == chars[s2[r]] + 1:
                matches -= 1
            elif window_chars[s2[r]] == chars[s2[r]]:
                matches += 1

        return matches == 26

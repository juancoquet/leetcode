class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1
        for ch in t:
            if ch in counts:
                counts[ch] -= 1
                if counts[ch] == 0:
                    del counts[ch]
            else:
                return False

        if len(list(counts.keys())) > 0:
            return False
        return True

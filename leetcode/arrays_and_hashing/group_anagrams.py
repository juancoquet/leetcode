# https://leetcode.com/problems/group-anagrams/description/
from typing import List

from leetcode.utils import group


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = group(strs, key=lambda s: "".join(sorted(s)))
        return list(groups.values())

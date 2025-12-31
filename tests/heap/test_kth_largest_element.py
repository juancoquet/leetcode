from typing import Self

import pytest
from pydantic import BaseModel, model_validator

from leetcode.heap.kth_lagest_element import KthLargest


class Case(BaseModel):
    k: int
    nums: list[int]
    additions: list[int]
    expected: list[int]

    @model_validator(mode="after")
    def _validate(self) -> Self:
        if self.k < 1:
            raise ValueError("k must be >= 1")
        if not self.additions:
            raise ValueError("additions must not be empty")
        if not self.expected:
            raise ValueError("expected must not be empty")
        if len(self.additions) != len(self.expected):
            raise ValueError("additions and expected must have the same length")
        return self


test_cases = [
    Case(k=3, nums=[4, 5, 8, 2], additions=[3, 5, 10, 9, 4], expected=[4, 5, 5, 8, 8]),
    Case(k=4, nums=[7, 7, 7, 7, 8, 3], additions=[2, 10, 9, 9], expected=[7, 7, 7, 8]),
]


@pytest.mark.parametrize(("tc"), test_cases)
def test_kth_largest(tc: Case) -> None:
    tracker = KthLargest(tc.k, tc.nums)
    for num, exp in zip(tc.additions, tc.expected, strict=True):
        assert tracker.add(num) == exp

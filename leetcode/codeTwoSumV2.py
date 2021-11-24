from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for index, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], index]
        elif num not in seen:
            seen[num] = index

def test_twoSum():
    assert twoSum([2, 7, 5, 11, 15], 7) == [0, 2]
    assert twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert twoSum([3, 3], 6) == [0, 1]
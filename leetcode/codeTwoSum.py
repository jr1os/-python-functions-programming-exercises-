from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    """
    >>> twoSum([2, 7, 11, 15], 9)
    [0, 1]
    >>> twoSum([3, 2, 4], 6)
    [1, 2]
    >>> twoSum([3, 3], 6)
    [0, 1]
    """
    seen = {}
    for index, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], index]
        elif num not in seen:
            seen[num] = index

print(twoSum([2, 7, 5, 11, 15], 26))
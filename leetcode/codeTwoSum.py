from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for index, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], index]
        elif num not in seen:
            seen[num] = index

print(twoSum([2, 7, 5, 11, 15], 26))
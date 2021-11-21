from typing import List

nums = [8, 1, 2, 2, 3] 
"""
>>> smallerNumbersThanCurrent(nums)
[4,0,1,1,3]

"""


def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:
    output = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if j != i and nums[i] > nums[j]:
                count += 1
        output.append(count)
    return output


if __name__ == "__main__":
    print(smallerNumbersThanCurrent(nums))
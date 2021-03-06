# coding: utf-8

'''
Given an array of integers with possible duplicates, randomly output the index of
a given target number. You can assume that the given target number must exist in the array.
Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly.
Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
'''

import random

class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        cnt, res = 1, -1
        nums = self.nums
        for i in range(len(nums)):
            if nums[i] == target:
                if random.randint(0, cnt - 1) == 0:
                    res = i
                cnt += 1
        return res

nums = [1,2,3,3,3]
obj = Solution(nums)
param_1 = obj.pick(3)
print param_1
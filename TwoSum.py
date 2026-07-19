#need to start learning DSA
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            for j in range(1, len(nums)):
                if (i != j):
                    if (nums[i] + nums[j] == target):
                        return [i,j]
                    
class Solution(object):
    def twoSum(self, nums, target):
        freq = {}
        for i in range(len(nums)):
            num1 = target - nums[i]
            num1_ind = freq.get(num1, -1)
            if num1_ind != -1:
                return [num1_ind, i]
            freq[nums[i]] = i
        return []    


        
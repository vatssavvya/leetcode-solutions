class Solution(object):
    def twoSum(self, nums, target):
        dict1 = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            comp_ind = dict1.get(comp)

            if comp_ind is not None:
                return [comp_ind, i]
            dict1[nums[i]] = i
        return []
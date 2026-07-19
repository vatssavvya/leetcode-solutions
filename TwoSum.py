#need to start learning DSA and implement faster solutions
class Solution(object):
    def twoSum(self, nums, target):
        dict1 = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            comp_ind = dict1.get(comp)

            if comp_ind is not None:
                return [i, comp_ind]

        return []
        """ for i in range(len(nums)-1):
            for j in range(1, len(nums)):
                if (i != j):
                    if (nums[i] + nums[j] == target):
                        return [i,j]
        """
class Solution(object):
    def twoSum(self, numbers, target):
        dict1 = {}
        for i in range(len(numbers)):
            comp = target - numbers[i]
            
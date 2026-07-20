class Solution(object):
    def twoSum(self, numbers, target):
        dict1 = {}
        for i in range(len(numbers)):
            comp = target - numbers[i]
            if comp in dict1:
                return [comp.value() + 1, i+1]
            dict1[numbers[i]] = i
        return []
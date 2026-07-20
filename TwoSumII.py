#my version of the two pointer method
class Solution(object):
    def twoSum(self, numbers, target):
        left, right = 0, (len(numbers)-1)
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left+1, right+1]
            elif total > target:
                right -= 1
            else:
                left+=1
        return []

#hash table solution
"""
class Solution(object):
    def twoSum(self, numbers, target):
        dict1 = {}
        for i in range(len(numbers)):
            comp = target - numbers[i]
            if comp in dict1:
                return [dict1[comp] + 1, i+1]
            dict1[numbers[i]] = i
        return []
"""
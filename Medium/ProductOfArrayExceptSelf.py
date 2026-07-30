#fastest solution
class Solution(object):
    def productExceptSelf(self, nums):
        leftArray = []
        rightArray = []
        for i in range(len(nums)):
            


#hard coded solution
"""class Solution(object):
    def productExceptSelf(self, nums):
        answer = []
        for i in range(len(nums)):
            total = 1
            for j in range(len(nums)):
                if j !=i:
                    total *= nums[j]
            answer.append(total)
        return answer """
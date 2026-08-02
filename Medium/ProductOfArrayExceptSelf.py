#fastest solution
class Solution(object):
    def productExceptSelf(self, nums):
        answers = [0] * len(nums)
        leftArray = [1] * len(nums)
        rightArray = [1] * len(nums)
        for i in range(1, len(nums)):
            leftArray[i] = leftArray[i-1] * nums[i-1]
        for i in range(len(nums) - 2, -1, -1):
            rightArray[i] = rightArray[i + 1] * nums[i + 1]
        for i in range(len(nums)):
            answers[i] = leftArray[i] * rightArray[i]
        return answers

#hard coded solutio
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
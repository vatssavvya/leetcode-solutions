class Solution(object):
    def productExceptSelf(self, nums):
        answer = []
        for i in range(len(nums)):
            total = 0
            for j in range(len(nums)):
                if j == i:
                    continue
                else:
                    total *= nums[j]
            answer.append(total)
        return answer    
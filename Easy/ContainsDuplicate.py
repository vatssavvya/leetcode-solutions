#used the set as its the fastest solution, 
class Solution(object):
    def containsDuplicate(self, nums):
       newNums = set(nums)
       return (len(nums) != len(newNums))       

    
#used the set as its the fastest solution, but deprioritize for the 
class Solution(object):
    def containsDuplicate(self, nums):
       newNums = set(nums)
       return (len(nums) != len(newNums))       

    
#optimal solution
class Solution(object):
   def topKFrequent(self, nums, k):
      dict1 = {}
      for num in nums:
         dict1[num] = dict1.get(num, 0) + 1
      

# hard coded solution
"""class Solution(object):
    def topKFrequent(self, nums, k):
      list1 = []
      for i in range(k):
        dict1 = {}
        for i in nums:
            if i not in dict1:
                dict1[i] = 0
            dict1[i] += 1
        maxKey = 0
        maxVal = 0
        for key, value in dict1.items():
           if value > maxVal:
               maxVal = value
               maxKey = key
        while (maxKey in nums):
           nums.remove(maxKey)
        list1.append(maxKey)
      return list1"""
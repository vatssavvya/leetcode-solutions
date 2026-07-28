class Solution(object):
    def topKFrequent(self, nums, k):
        #will finish later before August
      for i in range(k):
        dict1 = {}
        for i in nums:
            if i not in nums:
                dict1[i] = 0
            dict1[i] += 1
        max1 = 0
        for key, value in dict1.items():
           if value > max:
               max = key
            
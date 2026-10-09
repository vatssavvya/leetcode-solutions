class Solution(object):
    def minEatingSpeed(self, piles, h):
       l,r = 0, max(piles)
       while r - l > 1:
          tempPiles = piles[:]
          m = (l + r) // 2
          count = 0
          for i in range(len(tempPiles)):
              var1 = 0
              if tempPiles[i] % m !=0:
                 var1 = 1
              count+=(tempPiles[i]//m + (var1))
          if count > h:
             l = m
          else:
             r = m
       return r


        
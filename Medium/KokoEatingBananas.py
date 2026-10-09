class Solution(object):
    def minEatingSpeed(self, piles, h):
       l,r = 1, max(piles)
       while r - l > 1:
          tempPiles = piles[:]
          m = (l + r) // 2
          count = 0
          for i in range(len(tempPiles)):
            while (tempPiles[i] > 0):
              tempPiles[i] -= m
              count+=1
          if count > h:
             l = m
          else:
             r = m
       return r


        
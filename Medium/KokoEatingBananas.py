class Solution(object):
    def minEatingSpeed(self, piles, h):
       l,r = 1, max(piles)
         while r - l > 1:
            m = (l + r) // 2
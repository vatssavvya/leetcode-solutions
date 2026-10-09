class Solution(object):
    def mySqrt(self, x):
        l,r = 0, x
        while r - l > 1:
            m = (l+r)//2
            if m*m <= x:
                m = l
            else:
                m = r

        

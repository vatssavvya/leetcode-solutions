class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        dict1 = {}
        dict2 = {}
        for i in range(len(s)):
            if s[i] in dict1:

#sorted solution
"""        
class Solution(object):
    def groupAnagrams(self, strs):
        dict1 = {}
        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            if key not in dict1:
                dict1[key] = []
            dict1[key].append(strs[i])
        return list(dict1.values())"""


#hard-coded solution
class Solution(object):
    def groupAnagrams(self, strs):
        dict1 = {}
        for i in range(len(strs)):
            charFreq = [0] * 26
            for char in strs[i]:
                charFreq[char-97]+=1
            key = ""
            for k in range(26):
                if charFreq[k] > 0:
                    key.append(char(i+97) + str(charFreq[k]))
            if key not in dict1:
                dict1[key] = []
            dict1[key].append(strs[i])
        return list(dict1.values())
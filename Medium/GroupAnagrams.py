class Solution(object):
    def groupAnagrams(self, strs):
        dict1 = {}
        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            if key not in dict1:
                dict1[key] = []
            dict1[key].append(strs[i])
        return list(dict1.values())

            
        
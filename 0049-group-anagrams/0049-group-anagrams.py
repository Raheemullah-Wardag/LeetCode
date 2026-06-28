from collections import Counter
class Solution(object):
    def groupAnagrams(self, strs):
        dic={}
        
        for i in strs:
            s = ''.join(sorted(i))
            if s  not in   dic.keys():
                dic[s]=[i]
            else:
                
                dic[s].append(i)
        return list(dic.values())
                










        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
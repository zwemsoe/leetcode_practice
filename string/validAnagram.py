class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        slen = len(s)
        
        if slen != len(t):
            return False
        
        for i in range(slen):
            if s[i] in d1:
                d1[s[i]] += 1
            else:
                d1[s[i]] = 1
                
            if t[i] in d2:
                d2[t[i]] += 1
            else:
                d2[t[i]] = 1
                
        for k, v in d1.items():
            if k in d2:
                if v != d2[k]:
                    return False
            else: 
                return False
        
        return True
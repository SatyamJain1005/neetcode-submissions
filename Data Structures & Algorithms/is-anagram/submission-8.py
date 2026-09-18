class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hash_s = {}
        hash_t = {}

        for i in s:
            if i in hash_s.keys():
                hash_s[i] += 1
            else:
                hash_s[i] = 1

        for i in t:
            if i in hash_t.keys():
                hash_t[i] += 1
            else:
                hash_t[i] = 1

        if hash_s == hash_t:
            return True

        else:
            return False
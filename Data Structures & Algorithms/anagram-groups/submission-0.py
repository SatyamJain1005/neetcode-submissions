class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = {}

        for i in strs:
            a = sorted(i)
            b = ''.join(a)
            if b in out:
                out[b].append(i)
            else:
                out[b] = []
                out[b].append(i)
            
        return list(out.values())
        
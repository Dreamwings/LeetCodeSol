class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = collections.defaultdict(list)
        
        for s in strs:
            w = ''.join(sorted(s))
            d[w].append(s)
        
        return list(d.values())
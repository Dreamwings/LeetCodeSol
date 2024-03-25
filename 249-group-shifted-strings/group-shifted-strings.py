class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        ## S1:
        ## T: O(NK), K is avg string len
        ## S: O(N)
        d = defaultdict(list)
        for s in strings:
            key = []
            for i in range(len(s) - 1):
                # Throw in 26 so that we can normalzie below
                diff = 26 + ord(s[i+1]) - ord(s[i])
                # Wrap around
                # z + 1 = a
                key.append(str(diff % 26))
            d[','.join(key)].append(s)

        return list(d.values())        
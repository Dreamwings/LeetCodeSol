class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        ## S1:
        ## T: O(NK), K is avg string len
        ## S: O(N)

        d = defaultdict(list)

        for s in strings:
            key = []
            for i in range(len(s) - 1):
                # Calculate the relative ord diff between each latter char and the first char
                # Add 26 to make sure the diff is always positive, normalize it with mod 26
                # Note diff is an int in [0, 1, 2, ..., 25]
                diff = (26 + ord(s[i+1]) - ord(s[0])) % 26
                # Wrap around: z + 1 = a
                key.append(str(diff))
            d[','.join(key)].append(s)
        
        return list(d.values())        
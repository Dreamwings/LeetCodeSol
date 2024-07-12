class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        
        ## S1: Union-Find
        ## T: O(2n) + O(n) + O(nα(n)) + O(2mα(n)) ~ O(4n + 2m)
        ## S: O(2n) + O(2n) ~ O(n)

        # Check if sentences are of different lengths, return False directly if they are
        if len(sentence1) != len(sentence2):
            return False
      
        # Initialize the parent list for union-find
        n_pairs = len(similarPairs)
        parent = list(range(n_pairs * 2))
      
        # Union-find find function to find the root of the set to which 'x' belongs
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
      
        # Dictionary to store the mapping from word to its index in the union-find structure
        words2index = {}
        index = 0
        # Iterate over similar pairs and perform union operations
        for a, b in similarPairs:
            # If the word 'a' is not in the dictionary, add it and assign a corresponding index
            if a not in words2index:
                words2index[a] = index
                index += 1
            # If the word 'b' is not in the dictionary, add it and assign a corresponding index
            if b not in words2index:
                words2index[b] = index
                index += 1
            # Link the indices of the two words in the parent array to denote their similarity
            pa, pb = find(words2index[a]), find(words2index[b])
            parent[pa] = pb
      
        # Iterate through the sentences and check if each pair of words is similar
        for x, y in zip(sentence1, sentence2):
            # If the words are identical, continue
            if x == y:
                continue
            # If either word is not in the words2index, or their roots are not the same, return False
            if (x not in words2index or
                    y not in words2index or
                    find(words2index[x]) != find(words2index[y])):
                return False
      
        # If all word pairs are either the same or similar, return True
        return True

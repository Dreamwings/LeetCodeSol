
class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:

        ## S1: DFS Backtracking with Pruning
        # T: O(N!), n is the number of different characters of words and result, N <= 10
        # S: O(N)

        # Basically do a digit-by-digit check between result & added-words.
        # Simulate the adding process of words and backtrack if needed, be careful
        # of all base cases/terminal states. View it as 2-D matrix, each row is 
        # a word and each column is indexing of current word.

        all_words = words + [result]
        start = set()
        for word in all_words:
            if len(word) > 1: # This is important!
                start.add(word[0])
            # Without the > 1 check, it will fail for the example:
            # words = ["A", "B"], result = "A"
        max_len = max(map(len, all_words)) # Max word length
        # Special case: can't add up to result because it's too small
        if len(result) < max_len:
            return False

        def dfs(idx, i, carry, visited, d):
            # idx: index within current word
            # i: index within words list
            # visited: a set, only used for pruning during DFS
            # d: dict, map char to digit 
            
            # base : already checked all digits 
            if idx == max_len:
                return carry == 0
            # sub-base : all words checked, check if the 2 digits matched.
            if i == len(words) + 1:
                sums = sum(d[word[-idx - 1]] if idx < len(word) else 0 for word in words) + carry
                if sums % 10 == d[result[-idx - 1]]:
                    carry = sums // 10
                    return dfs(idx + 1, 0, carry, visited, d)
                return False
            
            # current word is too short, skip to next word
            if (i < len(words) and idx >= len(words[i])):
                return dfs(idx, i + 1, carry, visited, d)
            
            ch = all_words[i][-idx-1]
            if ch in d: # char already mapped, no need to backtrack. 
                return dfs(idx, i + 1, carry, visited, d)
            
            # Backtrack to try all possible digits
            begin = 1 if ch in start else 0
            
            for x in range(begin, 10):
                if x not in visited:
                    visited.add(x)
                    d[ch] = x
                    if dfs(idx, i + 1, carry, visited, d.copy()):
                        return True
                    visited.remove(x)
            return False

        return dfs(0, 0, 0, set(), {})




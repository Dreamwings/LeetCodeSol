class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        
        ## S1: DFS Backtracking
        ## T: O(M * N^2), DFS can traverse up to N elem in worst case, and each call DFS recursively
        ## S: O(N)

        m, n = len(grid), len(grid[0])
        matches = [-1] * n # Array for each girl, to store the index of matched boy
        res = 0
      
        # Helper function to find a match for a person from "boys"
        def dfs_match(i):
            for j, val in enumerate(grid[i]):
                # Check if the current person from "girls" has not been visited and there's a relation
                if val and j not in visited:
                    visited.add(j)
                    # If the person from "girls" is not matched or can be matched to another person
                    if matches[j] == -1 or dfs_match(matches[j]):
                        # Match Boy i with Girl j
                        matches[j] = i
                        return True
            
            return False # Return False if no match is found for i

        # Loop through each person in "boys" to find a matching person in "girls"
        for i in range(m):
            # Set of visited indices in "girls" for the current person from "boys"
            visited = set()
            # If a match is found, increment the total number of invitations
            if dfs_match(i):
                res += 1

        # Return the total number of invitations
        return res

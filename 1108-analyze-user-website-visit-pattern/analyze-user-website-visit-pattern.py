class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        ## S1: Using Combinations
        ## T: O(n log n) + O(n) + O(u * n^3/6) + O(n^3 log n)
        ## S: O(u * n^3/6)

        from itertools import combinations

        # step1 - sorting and keeping the result as lists
        access_log = [t for t in sorted(zip(timestamp, username, website))]

        # step2 - form a dictionary; users as key and website list as value
        user_and_web = defaultdict(list)
        for access_tuple in access_log:
            timestamp, username, website = access_tuple
            user_and_web[username].append(website)
		
		# step3 - form another dictionary where 3-sequence of websites as key and their counts as value
        sequence = defaultdict(int)
        for key in user_and_web:
            if len(user_and_web[key]) >= 3:
                temp = set(combinations(user_and_web[key], r=3))
                for t in temp:
                    sequence[t] += 1
		
        # step4 - sort the sequence dictionary and return only the first element
        return sorted(sequence, key=lambda k: (-sequence[k], k))[0]      


        """
        ## S2: From AlgoMonster
        ## T: O(n log n) + O(n) + O(u * n^3/6) + O(n^3 log n)
        ## S: O(u * n^3/6)

        # Create a dictionary to store the sites visited by each user
        users_visits = defaultdict(list)
        # Sort the data by timestamp and group websites by username
        for user, _, site in sorted(zip(usernames, timestamps, websites), key=lambda x: x[1]):
            users_visits[user].append(site)

        # Counter for tracking the frequency of each 3-sequence pattern
        patterns_count = Counter()

        # Iterate through each user's visited sites
        for sites in users_visits.values():
            number_of_sites = len(sites)
            unique_patterns = set()  # set to store unique 3-sequence patterns
            if number_of_sites > 2:  # Check if user has visited more than 2 sites
                # Generate all possible 3-sequence combinations
                for i in range(number_of_sites - 2):
                    for j in range(i + 1, number_of_sites - 1):
                        for k in range(j + 1, number_of_sites):
                            unique_patterns.add((sites[i], sites[j], sites[k]))
          
            # Update the count of each unique pattern
            for pattern in unique_patterns:
                patterns_count[pattern] += 1
      
        # Sort the patterns first by frequency (descending) and then lexicographically, and return the most common pattern
        return sorted(patterns_count.items(), key=lambda x: (-x[1], x[0]))[0][0]
        """
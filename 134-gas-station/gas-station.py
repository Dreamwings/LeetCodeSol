class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        ## S1: Greedy
        ## T: O(N)
        ## S: O(1)

        tot_gain = 0
        cur_gain = 0
        res = 0
        
        for i in range(len(gas)):
            # gain[i] = gas[i] - cost[i]
            tot_gain += gas[i] - cost[i]
            cur_gain += gas[i] - cost[i]

            # If we meet a "valley", start over from the next station
            # with 0 initial gas.
            if cur_gain < 0:
                cur_gain = 0
                res = i + 1
        
        return res if tot_gain >= 0 else -1


        ## S2: Greedy
        ## T: O(N)
        ## S: O(1)

        n = len(gas)
        start = end = n - 1 # Pointers for traversing the gas stations
        num_visitied = tot_gas = 0 # Counter for stations visited and total balance of gas
      
        while num_visitied < n:
            # Update the total balance by adding current gas and subtracting current cost
            tot_gas += gas[end] - cost[end]
            num_visitied += 1
          
            # Move to the next station, wrapping around if necessary
            end = (end + 1) % n
          
            # While the total balance is negative and we haven't visited all stations
            # move the start index backwards and adjust the balance.
            while tot_gas < 0 and num_visitied < n:
                # Move the start index to the previous station
                start = (start - 1 + n) % n
                # Update the total balance by adding gas and subtracting cost at the new start
                tot_gas += gas[start] - cost[start]
                # Increment the number of stations visited
                num_visitied += 1
      
        # If the total balance is negative, return -1 indicating the circuit cannot be completed,
        # otherwise return the start index
        return -1 if tot_gas < 0 else start
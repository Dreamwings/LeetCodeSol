class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        ## S1: Stack
        ## T: O(N)
        ## S: O(N)

        res = [0] * n  # list to hold the exclusive time for each function.
        stack = []  # stack to keep track of the function call hierarchy, func id.
        curr = -1  # Store a pointer to the current time.
 
        # Process each log entry.
        for log in logs:
            
            x = log.split(':') # Split the string log into 3 parts.
            # The function id and the timestamp, converted to an integer.
            i, t = int(x[0]), int(x[2])

            # If the log entry indicates a start event:
            if x[1] == 'start':                
                if stack: # If there's an ongoing function, update its exclusive time.
                    pre_i = stack[-1]
                    res[pre_i] += t - curr                              
                stack.append(i) # Push the current function onto the stack.
                curr = t # Update the current time to the new start time.
            else:                
                pre_i = stack.pop()  # Pop the last function from the stack.
                res[pre_i] += t + 1 - curr  # Update the exclusive time for this function.              
                # Update the current time to the end time + 1 since the next time unit
                # will indicate the start of the next event.
                curr = t + 1

        return res


        
        ## S2: Stack
        ## T: O(N)
        ## S: O(N)
        
        res = [0] * n
        stack = []
        time = []
        
        for log in logs:
            i, se, t = log.split(':')
            i, t = int(i), int(t)
            
            if se == 'start':
                stack.append(i)
                time.append(t)
            else:
                x = stack.pop()
                tlen = t - time.pop() + 1
                res[x] += tlen
                if stack:
                    res[stack[-1]] -= tlen
        
        return res
    

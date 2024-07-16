class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        
        ## S1:
        ## T: O(log(max(tx - sx, ty - sy)))
        ## S: O(1)

        # Loop to transform the target point back towards the starting point
        while tx > sx and ty > sy and tx != ty:
            # If tx is greater than ty, reduce tx
            if tx > ty:
                # The modulo operation finds how many steps can be taken from ty to reach current tx
                tx %= ty
            # If ty is greater than tx, reduce ty
            else:
                # Likewise, this modulo operation finds the steps from tx to reach current ty
                ty %= tx
      
        # Check if the starting point is reached after breaking out of the loop
        if tx == sx and ty == sy:
            return True
      
        # If only tx matches sx, check if we can reach the target point
        # by repeatedly subtracting sx from ty
        if tx == sx:
            return ty > sy and (ty - sy) % tx == 0
      
        # If only ty matches sy, check if we can reach the target point
        # by repeatedly subtracting sy from tx
        if ty == sy:
            return tx > sx and (tx - sx) % ty == 0
      
        # If neither tx nor ty matches, reaching the target point is not possible
        return False

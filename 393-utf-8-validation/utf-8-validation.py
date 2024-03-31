class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        
        ## S2:

        num_of_bytes = 0

        # Loop through each integer in the data list
        for value in data:
            # If we're in the middle of parsing a valid UTF-8 character
            if num_of_bytes > 0:
                # Check if the first 2 bits are 10, which is a continuation byte
                if value >> 6 != 0b10:
                    # Not a continuation byte, so the sequence is invalid
                    return False
                # We've processed one of the continuation bytes
                num_of_bytes -= 1
            # If we're at the start of a UTF-8 character
            else:
                # Check the first bit; if it's 0, we have a 1-byte character
                if value >> 7 == 0:
                    # Set to 0 as it's a single-byte character
                    num_of_bytes = 0
                # Check the first 3 bits; if they're 110, it's a 2-byte character
                elif value >> 5 == 0b110:
                    # Expecting one more byte for this character
                    num_of_bytes = 1
                # Check the first 4 bits; if they're 1110, it's a 3-byte character
                elif value >> 4 == 0b1110:
                    # Expecting two more bytes for this character
                    num_of_bytes = 2
                # Check the first 5 bits; if they're 11110, it's a 4-byte character
                elif value >> 3 == 0b11110:
                    # Expecting three more bytes for this character
                    num_of_bytes = 3
                else:
                    # The first bits do not match any valid UTF-8 character start
                    return False

        # Check if all characters have been fully processed
        return num_of_bytes == 0

        """

        ## S1:

        n_bytes = 0
        
        for x in data:
            x_bin = bin(x)[2:]  # first 2 bits are '0b'
            n_x_bin = len(x_bin)
            if n_x_bin >= 8:
                x_bin = x_bin[-8:]
            else:
                x_bin = '0' * (8 - n_x_bin) + x_bin
            
            # start processing a new data
            if n_bytes == 0:
                for c in x_bin:
                    if c == '0':
                        break
                    n_bytes += 1
                
                # after processing the first num in data, check if n_bytes is 0, 2, 3 or 4
                # if not, it's not valid
                if n_bytes == 0:  # it's a 1-byte number
                    continue
                
                if n_bytes == 1 or n_bytes > 4:
                    return False
            
            else: # n_bytes is 2, 3 or 4, start processing 2nd number
                if x_bin[:2] != '10':
                    return False
                
            # after each processing, n_bytes decrements by 1 to reflect bytes left
            n_bytes -= 1
        
        return n_bytes == 0

        """
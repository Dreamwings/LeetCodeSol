class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        ## S2:
        ## T: O(N)
        ## S: O(N)

        freq_counter = Counter(nums)
      
        # Find the maximum frequency among all elements
        max_freq = max(freq_counter.values())
      
        # Calculate the sum of elements that have the maximum frequency
        # This is the count of elements that appear the most frequently in the list
        res = sum(f for f in freq_counter.values() if f == max_freq)
      
        return res



        ## S1:
        ## T: O(N)
        ## S: O(N)

        frequencies = {}
        max_frequency = 0
        total_frequencies = 0

        # Find the frequency of each element
        # Determine the maximum frequency
        # Calculate the total frequencies of elements with the maximum frequency
        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1
            frequency = frequencies[num]

            # If we discover a higher frequency element
            # Update max_frequency
            # Re-set totalFrequencies to the new max frequency
            if frequency > max_frequency:
                max_frequency = frequency
                total_frequencies = frequency
            # If we find an element with the max frequency, add it to the total
            elif frequency == max_frequency:
                total_frequencies += frequency

        return total_frequencies
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        
        ## S2: Double Ended Queue
        ## T: O(NlogN)
        ## S: O(N)

        from collections import deque
        q = deque()

        # Sort the deck in descending order 
        for card in sorted(deck, reverse=True):
            # If the deque is not empty, move the last element to the front
            if q: 
                q.appendleft(q.pop())
            # Insert the current card to the front of the deque
            q.appendleft(card)
        
        return list(q)



        ## S1: Two Pointers
        ## T: O(NlogN)
        ## S: O(N)

        n = len(deck)
        res = [0] * n
        skip = False
        deck_idx = 0
        res_idx = 0

        deck.sort()

        while deck_idx < n:
            # There is an available gap in res
            if res[res_idx] == 0:

                # Add a card to res
                if not skip:
                    res[res_idx] = deck[deck_idx]
                    deck_idx += 1

                # Toggle skip to alternate between adding and skipping cards
                skip = not skip

            # Progress to the next index of res array
            res_idx = (res_idx + 1) % n

        return res
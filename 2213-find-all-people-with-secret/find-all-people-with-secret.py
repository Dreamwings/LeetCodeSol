class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        
        ## S2: Sorting + BFS on Time Scale
        ## T: O(MlogM + N + M), N be the number of people, and MMM be the number of meetings.
        ## S: O(M+N)

        # Initialize visited list, setting 0 and firstPerson as True since they know the secret
        visited = [False] * n
        visited[0] = visited[firstPerson] = True

        # Sort meetings by the time (third element in the meeting tuple)
        meetings.sort(key=lambda x: x[2])

        i, m = 0, len(meetings)
      
        # Iterate through sorted meetings
        while i < m:
            # Find the range of meetings happening at the same time
            j = i
            while j + 1 < m and meetings[j + 1][2] == meetings[i][2]:
                j += 1
          
            # Set to store unique participants in meetings happening at the same time
            all_persons = set()
            # Graph representation (adjacency list) for people who meet at the same time
            graph = defaultdict(list)
          
            # Build the set of participants and the graph of graph
            for a, b, _ in meetings[i : j + 1]:
                graph[a].append(b)
                graph[b].append(a)
                all_persons.update([a, b])
          
            # Queue to explore nodes (people) that know the secret
            queue = deque([x for x in all_persons if visited[x]])
          
            # BFS to propagate the secret among those meeting at the same time
            while queue:
                curr = queue.popleft()
                for neighbor in graph[curr]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
          
            # Increment index to the next time slot of meetings
            i = j + 1
      
        return [x for x, knows_secret in enumerate(visited) if knows_secret]

        """

        ## S1: Heap + BFS
        ## T: O((N+M)*log(N+M)+ NM), N be the number of people, and MMM be the number of meetings.
        ## S: O(M+N)

        # For every person, store the time and label of the person met.
        graph = defaultdict(list)
        for x, y, t in meetings:
            graph[x].append((t, y))
            graph[y].append((t, x))

        # Priority Queue for BFS. It stores (time secret learned, person)
        # It pops the person with the minimum time of knowing the secret.
        pq = []
        heappush(pq, (0, 0))
        heappush(pq, (0, firstPerson))

        # Visited array to mark if a person is visited or not.
        # We will mark a person as visited after it is dequeued
        # from the queue.
        visited = [False] * n

        # Do BFS, but pop minimum.
        while pq:
            time, person = heappop(pq)
            if visited[person]:
                continue
            visited[person] = True
            for t, next_person in graph[person]:
                if not visited[next_person] and t >= time:
                    heappush(pq, (t, next_person))

        # Since we visited only those people who know the secret
        # we need to return indices of all visited people.
        return [i for i in range(n) if visited[i]]

        """
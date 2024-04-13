class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        
        from collections import defaultdict

        ## S1: DFS
        ## T: O(N)
        ## S: O(N)

        # Recursive depth-first search function to kill a process and its subprocesses.
        def dfs(process_id: int):
            # Add the current process to the list of killed processes.
            res.append(process_id)
            # Kill all the subprocesses of the current process.
            for subprocess_id in graph[process_id]:
                dfs(subprocess_id)

        # Create a graph using a dictionary where each key is a parent process ID
        # and the value is a list of its child process IDs.
        graph = defaultdict(list)
        for child_pid, parent_pid in zip(pid, ppid):
            graph[parent_pid].append(child_pid)
      
        res = []
        dfs(kill)
        
        return res
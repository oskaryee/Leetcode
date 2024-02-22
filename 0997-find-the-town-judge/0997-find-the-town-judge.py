class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        track = DefaultDict(set)
        arr = [True] * (n + 1)
        
        for i in trust:
            track[i[1]].add(i[0])
            arr[i[0]] = False
            
        for i in range(1, n + 1): # We don't need to check person at position 0
            if arr[i] and len(track[i]) == (n-1):
                return i
            
        return -1        
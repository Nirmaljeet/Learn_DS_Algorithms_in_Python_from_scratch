class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        dp = [[] for i in range(target+1)]    
        
        for c in candidates:
            for i in range(1, target+1):
                if c > i:
                    continue
                elif c == i:
                    dp[i].append([c])
                else:
                    for lst in dp[i-c]:
                        dp[i].append(lst+[c])
                
        return dp[target]

    
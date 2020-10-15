def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0]*(n) for _ in range(n) ]
        
        for i in range(n):
            dp[i][i] = 1

                    
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):                    
                if s[i]==s[j]:
                    dp[i][j] = dp[i+1][j-1]+2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
                    
        return dp[0][-1]

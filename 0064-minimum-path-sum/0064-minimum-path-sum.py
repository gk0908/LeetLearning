class Solution:
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])

        # dp[j] will store the minimum path sum for column j in the current row
        dp = [0] * n
        dp[0] = grid[0][0]

        # Fill first row
        for j in range(1, n):
            dp[j] = dp[j-1] + grid[0][j]

        for i in range(1, m):
            # Update first column for current row
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = grid[i][j] + min(dp[j], dp[j-1])

        return dp[-1]

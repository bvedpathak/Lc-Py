class Solution(object):

    def minPathSum_rec(self, grid):
        def minPathSumRecurrsive(i, j, grid, curr_sum, min_sum):
            if not grid:
                return min_sum
            
            if i == len(grid) or j == len(grid[0]):
                return min_sum
            
            curr_sum += grid[i][j]

            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                min_sum = min(min_sum, curr_sum)
                return min_sum
            
            min_sum = minPathSumRecurrsive(i + 1, j, grid, curr_sum, min_sum)
            min_sum = minPathSumRecurrsive(i, j + 1, grid, curr_sum, min_sum)

            return min_sum
        return(minPathSumRecurrsive(0, 0, grid, 0, float('inf')))
    
    def minPathSum(self, grid):
        if not grid:
            return 0
        
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        dp[0][0] = grid[0][0]
        for i in range(1, len(grid)):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        
        for j in range(1, len(grid[0])):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
        
        return dp[-1][-1]
    
grid = [[1,3,1],
        [1,5,1],
        [4,2,1]]

grid = [[1,2,3],
        [4,5,6]]

grid = [[1]]
print(f"Mininum Path is with recurrsion: {Solution().minPathSum_rec(grid)}")
print(f"Mininum Path is with DP: {Solution().minPathSum(grid)}")



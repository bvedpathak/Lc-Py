# Given a m x n grid filled with non-negative numbers, 
# find a path from top left to bottom right, which minimizes 
# the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.
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
    
    # DP way of solving the same problem. 
    # Time: O(m.n), Space: O(m.n)
    def minPathSum_dp(self, grid):
        if not grid:
            return 0
        
        # Define DP table with 0 first
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        # Define base case for the row 0. It is because there is no other way
        # to reach to these cells so min path includes the simple addition 
        dp[0][0] = grid[0][0]
        for i in range(1, len(grid)):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        
        # Define base case for the col 0. It is because there is no other way
        # to reach to these cells so min path includes the simple addition 
        for j in range(1, len(grid[0])):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        # Iterate and calculate the minimum path calculating min path that exists
        # either from the top or from the left going into the current cell
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
        
        return dp[-1][-1]
    
    # The optimized DP. TimeL O(m.n), Space: O(1)
    def minPathSum(self, grid):
        if not grid: 
            return 0
        prev_row = [grid[0][0]]
        # Base case
        for i in range(1, len(grid[0])):
            prev_row.append(prev_row[i - 1] + grid[0][i])
        
        # Iterate and calculate the minimum path calculating min path that exists
        # either from the top or from the left going into the current cell
        for i in range(1, len(grid)):
            curr_row = [grid[i][0] + prev_row[0]]
            for j in range(1, len(grid[0])):
                curr_row.append(grid[i][j] + min(curr_row[j -1], prev_row[j]))
            prev_row = curr_row
        
        return prev_row[-1]

    
grid = [[1,3,1],
        [1,5,1],
        [4,2,1]]

'''
grid = [[1,2,3],
        [4,5,6]]
'''

grid = [[1,2],
        [1,1]]
#grid = [[1]]
print(f"Mininum Path is with recurrsion: {Solution().minPathSum_rec(grid)}")
print(f"Mininum Path is with recurrsion: {Solution().minPathSum_dp(grid)}")
print(f"Mininum Path is with DP: {Solution().minPathSum(grid)}")

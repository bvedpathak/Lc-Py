# Function to to return Kth top using heap datastructure. The top k define
# by the ascending order (if you want to support kth by descending order then
# just negate before putting in the heapq and negate again while poppig back)
# Time: O(n. log k), Space: O(n)
import heapq
def kth_top(nums, k):
    if not nums:
        return None
    res = list()
    for num in nums:
        heapq.heappush(res, -num)

    return [-heapq.heappop(res) for _ in range(k)]

nums = [1, 3, 4, 5, 2, 0]
k = 3
print(f"\nTop {k} elements in the {nums} are: {kth_top(nums, k)}\n")


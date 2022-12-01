# User function Template for python3


class Solution:
    def MissingNumber(self, array, n):
        sumofArr = 0
        for i in range(len(array)):
            sumofArr += array[i]
            expArr = n*(n+1)/2
            res = expArr-sumofArr
        return int(res)

# {
 # Driver Code Starts
# Initial Template for Python 3


t = int(input())
for _ in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    s = Solution().MissingNumber(a, n)
    print(s)
# } Driver Code Ends

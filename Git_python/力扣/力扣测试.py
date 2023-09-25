def longestPalindrome(s):
    n = len(s)
    if n<=1:
        return s

    dp = [[False] * n for _ in range(n)]
    start=0
    max_length=1

    for i in range(n):
        dp[i][i]=True

    for length in range(2,n+1):
        for i in range(n-length+1):
            j=i+length-1
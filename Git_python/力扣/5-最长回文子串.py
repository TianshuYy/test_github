def longestPalindrome(s):
    n = len(s)
    if n <= 1:
        return s

    dp = [[False] * n for _ in range(n)]
    start = 0
    max_length = 1

    for i in range(n):
        dp[i][i] = True

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]

            if dp[i][j] and length > max_length:
                max_length = length
                start = i

    return s[start:start + max_length]

# 测试示例
s1 = "babad"
s2 = "cbbd"
print(longestPalindrome(s1))  # 输出："bab" 或 "aba"
print(longestPalindrome(s2))  # 输出："bb"

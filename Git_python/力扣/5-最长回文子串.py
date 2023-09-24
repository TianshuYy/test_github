def length_of_longest_substring(s):
    char_index = {}  # 用于记录字符的最后出现位置
    max_length = 0    # 最长子串的长度
    start = 0         # 窗口的起始位置

    for end in range(len(s)):
        if s[end] in char_index and char_index[s[end]] >= start:
            start = char_index[s[end]] + 1  # 更新窗口的起始位置

        char_index[s[end]] = end  # 更新字符的最后出现位置
        max_length = max(max_length, end - start + 1)

    return max_length

s = "abcabcbb"
print(length_of_longest_substring(s))  # 输出: 3
s = "fksef"
def lengthOfLongestSubstring(s):
    list1=[]
    for j in range(len(s)):
        str1 = ''
        for i in s[j:]:
            if i not in str1:
                str1+=i
            else:
                break
        list1.append(str1)
    list2=[]
    for c in list1:
        list2.append(len(c))
    if len(list2)!=0:
        return max(list2)
    else:
        return 0
print(lengthOfLongestSubstring(s))
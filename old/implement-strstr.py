# Implement strStr()
# https://leetcode.com/problems/implement-strstr/


def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """

    match = False
    if len(needle) == 0:
        return 0

    for i in range(len(haystack)):
        if haystack[i] == needle[0]:
            print("do it")




ans = strStr("hello", "ll")
print(ans)


"""
Example input: s = '01001010100100010'
output: 3
"""


def find_substring(s):
    count = 0
    start = False
    max_len = 0
    for i in range(len(s)):
        if start:
            count += 1
        if s[i] == "1":
            if start:
                max_len = max(max_len, count)
                start = False
                count = 0
            else:
                start = True
                count = 1

    return max_len


print(find_substring('01001010100100010'))
print(find_substring('010101'))
print(find_substring('10010101'))


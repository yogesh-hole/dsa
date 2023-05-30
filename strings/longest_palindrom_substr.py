class Solution:
    def check(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True

    def longestPalindrome(self, s: str) -> str:
        max_len = 1
        start = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.check(s, i, j):
                    if j - i + 1 > max_len:
                        max_len = j - i + 1
                        start = i
        return s[start:max_len]


sol = Solution()
print(sol.longestPalindrome("ababd"))

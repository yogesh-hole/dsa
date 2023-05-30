class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not t:
            if not s:
                return True
            return False

        if not s and t:
            return True

        start = 0

        for i in range(len(t)):
            if s[start] == t[i]:
                start += 1
                if start == len(s):
                    return True
        return False


sol = Solution()
print(sol.isSubsequence("b", "abc"))

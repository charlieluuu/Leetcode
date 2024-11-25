class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index = 0
        # Go through each character in `t`
        for char in t:
            # Check if current `s_index` is still within the bounds of `s`
            if s_index < len(s) and s[s_index] == char:
                # Move to the next character in `s`
                s_index += 1
        # Check if all characters in `s` were found in `t` in the correct order
        return s_index == len(s)

if __name__ == '__main__':
    solution = Solution()
    result = solution.isSubsequence("abc", "ahbgdc")
    print(result)
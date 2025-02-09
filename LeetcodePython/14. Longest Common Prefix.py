class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        min_str = min(strs)
        max_str = max(strs)
        k = ""

        for i in range(len(min_str)):
            if (min_str[i] == max_str[i]):
                k += min_str[i]
            else:
                break
        return k


if __name__ == '__main__':
    solution = Solution()
    result = solution.longestCommonPrefix(["flower","flow","flight"])
    print(result)
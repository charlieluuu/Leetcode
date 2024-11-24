class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        else:
            return haystack.index(needle)

if __name__ == '__main__':
    solution = Solution()
    result = solution.strStr("sadbutsad", "sad")
    print(result)
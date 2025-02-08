class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        map = {}
        check_map = set(s)

        if len(pattern) != len(s):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in map:
                map[pattern[i]] = s[i]
            elif map[pattern[i]] != s[i]:
                return False

        if len(check_map) == len(map):
            return True
        else:
            return False

if __name__ == '__main__':
    solution = Solution()
    result = solution.wordPattern("abba", "dog cat cat dog")
    print(result)
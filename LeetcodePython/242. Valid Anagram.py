class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = list(s)
        s1.sort()
        s2 = "".join(s1)

        t1 = list(t)
        t1.sort()
        t2 = "".join(t1)

        if s2 == t2:
            return True
        else:
            return False

if __name__ == '__main__':
    solution = Solution()
    result = solution.isAnagram("anagram", "nagaram")
    print(result)
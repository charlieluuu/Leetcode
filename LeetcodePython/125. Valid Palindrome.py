class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = []
        for char in s:
            if char.isalnum():
                clean.append(char.lower())

        for i in clean:
            if clean[:] == clean[::-1]:
                return True
            else:
                return False

        if len(clean) == 0:
            return True

if __name__ == '__main__':
    solution = Solution()
    result = solution.isPalindrome("A man, a plan, a canal: Panama")
    print(result)
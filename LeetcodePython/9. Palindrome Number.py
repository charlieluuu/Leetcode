class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        # If x is a palindrome, then it will be the same even it reversed
        reversed_x = int(str(x)[::-1])
        return x == reversed_x


if __name__ == '__main__':
    solution = Solution()
    result = solution.isPalindrome(121)
    print(result)
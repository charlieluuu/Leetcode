class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()



if __name__ == '__main__':
    solution = Solution()
    s = ["h","e","l","l","o"]
    solution.reverseString(s)  # s is modified in-place
    print(s)  # Now s is reversed correctly
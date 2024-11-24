class Solution:
    def isValid(self, s: str) -> bool:
        check_valid = []
        for i in s:
            if i in "{[(":
                check_valid.append(i)
            else:
                if not check_valid or \
                    (i == ')' and check_valid[-1] != '(') or \
                    (i == ']' and check_valid[-1] != '[') or \
                    (i == '}' and check_valid[-1] != '{'):
                    return False
                check_valid.pop() #remove the opening bracket that add previously if the brackets are not pair
        return not check_valid #if it's empty then print True

if __name__ == '__main__':
    solution = Solution()
    result = solution.isValid("()")
    print(result)
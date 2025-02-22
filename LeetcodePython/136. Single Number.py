class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        checkList = {}

        for i in nums:
            if i not in checkList:
                checkList[i] = 1
            else:
                checkList[i] = checkList[i] + 1

        for i in checkList:
            if checkList[i] == 1:
                return i


if __name__ == '__main__':
    solution = Solution()
    result = solution.singleNumber([4,1,2,1,2])
    print(result)
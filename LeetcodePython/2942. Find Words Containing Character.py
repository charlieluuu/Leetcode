class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        output =[]
        for i in range(len(words)):
            if x in words[i]:
                output.append(i)

        return output


if __name__ == '__main__':
    solution = Solution()
    result = solution.findWordsContaining(["leet","code"], "e")
    print(result)
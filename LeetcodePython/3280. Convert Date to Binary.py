class Solution:
    def convertDateToBinary(self, date: str) -> str:
        list_date = date.split("-")
        output_bin_date = []

        for i in list_date:
            bin_date = bin(int(i))[2:]
            output_bin_date.append(bin_date)

        output = '-'.join(output_bin_date)
        return output


if __name__ == '__main__':
    solution = Solution()
    result = solution.convertDateToBinary("2080-02-29")
    print(result)
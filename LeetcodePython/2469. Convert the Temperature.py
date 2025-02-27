class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        Kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.8 + 32
        return Kelvin, Fahrenheit


if __name__ == '__main__':
    solution = Solution()
    result = solution.convertTemperature(36.5)
    print(result)
class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        answer = 0

        for i in range(len(s) - 1):
            if symbol[s[i]] < symbol[s[i + 1]]:
                answer -= symbol[s[i]]
            else:
                answer += symbol[s[i]]

        answer += symbol[s[-1]]

        return answer

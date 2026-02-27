# 풀이 1 - 69 / 85 testcases passed
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1

        pointer = 0
        idx = 0

        for i in range(len(haystack)):
            if haystack[i] == needle[pointer]:
                if pointer == 0:
                    idx = i

                pointer += 1

                if pointer == len(needle):
                    return idx
            else:
                pointer = 0

        return -1


# 풀이 2 - 투 포인터
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1

        n, m = len(haystack), len(needle)

        if m == 0:
            return 0

        for i in range(n - m + 1):
            j = 0
            while j < m and haystack[i + j] == needle[j]:
                j += 1

            if j == m:
                return i

        return -1

class Solution:
    def isPalindrome(self, x: int) -> bool:
        p_num = str(x)

        if x < 0:
            return False

        if x % 2 == 0:
            left = p_num[0 : x // 2]
            right = p_num[-1 : -(x // 2 + 1) : -1]

            if left == right:
                return True
            else:
                return False
        else:
            left = p_num[0 : x // 2]
            right = p_num[-1 : -(x // 2 + 1) : -1]

            if left == right:
                return True
            else:
                return False


# 초간단 버전 샘플
class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        return str_x == str_x[::-1]

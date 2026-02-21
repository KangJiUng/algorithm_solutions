class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) < 2:
            return False

        for bracket in s:
            if bracket == "(":
                stack.append(bracket)
            elif bracket == "{":
                stack.append(bracket)
            elif bracket == "[":
                stack.append(bracket)

            elif bracket == ")":
                if not stack:
                    return False
                op = stack.pop()
                if op != "(":
                    return False

            elif bracket == "}":
                if not stack:
                    return False
                op = stack.pop()
                if op != "{":
                    return False

            elif bracket == "]":
                if not stack:
                    return False
                op = stack.pop()
                if op != "[":
                    return False

        if len(stack) > 0:
            return False

        return True

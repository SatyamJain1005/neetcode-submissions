class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        stack_ = []
        if len(s) % 2 != 0:
            return False

        for i in s:
            if i in mapping.values():
                stack_.append(i)
            elif stack_ and mapping[i] == stack_[-1]:
                stack_.pop()
            else:
                return False

        if len(stack_) == 0:
            return True
        else:
            return False
            
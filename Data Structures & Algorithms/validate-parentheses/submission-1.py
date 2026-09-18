class Solution:
    def isValid(self, s: str) -> bool:
        map_ = {
        ")" : "(",
        '}' : "{",
        "]" : "["
        }
        stack_ = []

        if len(s) % 2 != 0:
            return False

        for i in s:
            if i in map_.values():
                stack_.append(i)
            elif map_[i] in stack_ and stack_[-1]==map_[i]:
                stack_.pop()
            else:
                return False

        if len(stack_) == 0:
            return True
        else:
            return False

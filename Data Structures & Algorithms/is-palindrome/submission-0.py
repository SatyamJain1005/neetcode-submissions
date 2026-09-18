class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''
        for i in s:
            if i.isalnum():
                cleaned += i.lower()

        for i in range(len(cleaned)):
            if cleaned[i]!=cleaned[-1-i]:
                return False
            else:
                continue
        return True
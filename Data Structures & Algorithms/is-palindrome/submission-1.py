def t(s):
    ords=ord(s)
    return 65<=ords<=90 or 97<=ords<=122 or 48<=ords<=57


class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpabet = ''
        s = ''.join([l for l in s if t(l)]).lower()
        return s == s[::-1]
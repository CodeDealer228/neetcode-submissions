def t(s):
    return 65<=ord(s)<=90 or 97<=ord(s)<=122 or 48<=ord(s)<=57


class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpabet = ''
        s = ''.join([l for l in s if t(l)]).lower()
        return s == s[::-1]
class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return True
        l = 0
        open_chars = '([{'
        close_chars = ')]}'
        while True:
            k = open_chars.find(s[l])
            if k == -1:
                if s[l] in close_chars:
                    return False
                l+=1
            else:
                r = s[l+1:].find(close_chars[k]) + l + 1
                if r == l:
                    return False
                return self.isValid(s[l+1:r]) and self.isValid(s[r+1:])

            




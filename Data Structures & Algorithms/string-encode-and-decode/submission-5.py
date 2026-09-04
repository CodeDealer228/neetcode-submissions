class Solution:
    def __init__(self):
        self.sep_code = 257
        self.sep_char = chr(self.sep_code)

    def encode(self, strs: List[str]) -> str:
        if strs:
            return self.sep_char + self.sep_char.join(strs) + self.sep_char
        else:
            return ''

    def decode(self, s: str) -> List[str]:
        if s:
            return s.split(self.sep_char)[1:-1] if s else [s]
        else:
            return []

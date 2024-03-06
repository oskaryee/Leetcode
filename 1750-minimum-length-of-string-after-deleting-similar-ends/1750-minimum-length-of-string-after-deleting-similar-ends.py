class Solution:
    def minimumLength(self, s: str) -> int:

        # s[0] = letter we need to get rid
        while len(s) > 1 and s.endswith(s[0]):
            s = s.lstrip(s[0]).rstrip(s[0])

        return len(s)

            
        
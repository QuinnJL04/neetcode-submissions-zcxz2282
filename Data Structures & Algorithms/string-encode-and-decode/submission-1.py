class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for stri in strs:
            length = len(stri)
            result += str(length) + "#" + stri
        return result

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            curr_length = ""
            while i < len(s) and s[i].isdigit():
                curr_length += s[i]
                i+=1
            i += 1
            length = int(curr_length)
            substr = s[i: i + length]
            result.append(substr)

            i += length
        return result

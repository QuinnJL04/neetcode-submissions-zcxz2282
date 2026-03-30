class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            encode = str(len(word)) + "#" + word
            res += encode
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            idx = j + 1 + length
            word = s[j+1:idx]
            res.append(word)          
            i = j + 1 + length  
        return res
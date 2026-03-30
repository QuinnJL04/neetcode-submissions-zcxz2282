class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        library = {}

        for c in s:
            if c not in library:
                library[c] = 1
            else:
                library[c] += 1

        for c in t:
            if c in library.keys():
                library[c] -= 1
            else:
                return False
        
        for key in library.keys():
            if library[key] != 0:
                return False
        
        return True
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        library = {}
        for i in t:
            if i not in library:
                library[i] = 1
            else:
                library[i] += 1

        for j in s:
            if j in library:
                library[j] -= 1
                if library[j] < 0:
                    return False
            else:
                return False
        for count in library.values():
            if count != 0:
                return False
        return True
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = []
        processed = set()
        for i in range(len(strs)):
            if i in processed:
                continue
            substr = [strs[i]]
            for j in range(i + 1, len(strs)):
                if len(strs[i]) != len(strs[j]):
                    continue
                
                seen = {}
                for char in strs[i]:
                    seen[char] = seen.get(char, 0) + 1
                
                is_anagram = True  # Assume strs[i] and strs[j] are anagrams
                for char in strs[j]:
                    if char not in seen or seen[char] == 0:
                        is_anagram = False  # Not an anagram
                        break
                    seen[char] -= 1
                
                # Verify if all counts are zero
                if is_anagram and all(count == 0 for count in seen.values()):
                    substr.append(strs[j])
                    processed.add(j)
            
            result.append(substr)
        return result
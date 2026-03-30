class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        j = len(numbers) - 1

        for i in range(len(numbers)):
            
            while i < j:
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
                j-=1

            j = len(numbers) - 1
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        #numbers[i] < numbers[i + 1] and  equal target

        i = 0
        j = len(numbers) - 1

        while i < j:
            if numbers[i] < numbers[j]:
                summ = numbers[i] + numbers[j]
                if summ == target:
                    return [i + 1, j + 1]
                elif summ < target:
                    i += 1
                elif summ > target:
                    j -= 1
                


        


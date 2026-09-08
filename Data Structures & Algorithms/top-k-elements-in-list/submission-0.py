class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elementFreq = {}    # key = num: value = frequency

        for num in nums:
            if num not in elementFreq:
                elementFreq[num] = 1
            else:
                elementFreq[num] += 1
        
        sortEF = sorted(elementFreq.keys(), key = elementFreq.get, reverse = True)
        result = []
        for i in range(k):
            result.append(sortEF[i])

        return result
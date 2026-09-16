class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}

        for word in strs:
            orderedWord = ("").join(sorted(word))

            if orderedWord in hashMap:
                hashMap[orderedWord].append(word)
            else:
                hashMap[orderedWord] = [word]
        
        return list(hashMap.values())
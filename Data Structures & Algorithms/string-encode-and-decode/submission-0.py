class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedstr = ""
        for word in strs:
            wordlength = len(word)
            encodedstr += str(wordlength) + "#" + word
        return encodedstr

    def decode(self, s: str) -> List[str]:
        decodedstr = []
        i = 0
        getWordLength = ""
        while i < len(s):
            if s[i] != "#":
                getWordLength += s[i]
                i += 1
                continue
            else:
                count = int(getWordLength)
                cutString = s[i + 1:i + count + 1]
                decodedstr.append(cutString)
                getWordLength = ""
                i += 1 + count
        return decodedstr
class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(f"{len(s)}#{s}")
        return ''.join(result)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            # index of #, starting from our tracking pointer
            j = s.index('#', i)
            length = int(s[i:j])
            # add the word after the length + separator tokens
            decoded.append(s[j+1:j+1+length])
            # set tracking pointer to next word
            i = j + 1 + length
        return decoded

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. an anagram just means the freq of chars match
        # 2. only 26 letters possible -> an anagram can be
        # identified by its count per letter -> use an 26-index array
        # 3. we want to return sublists -> mapping needed for anagram -> word list

        a2w = defaultdict(list)
        for s in strs:
            count = [0] * 26 
            for c in s:
                count[ord(c.lower()) - ord('a')] += 1
            a2w[tuple(count)].append(s)

        # return sublists
        return list(a2w.values())
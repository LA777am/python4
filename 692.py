from collections import Counter
class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        d= Counter(words)
        ls =[]
        d2= sorted(d.items(), key= lambda x: (-x[1],x[0]))
        return [x[0] for x in d2[:k]]
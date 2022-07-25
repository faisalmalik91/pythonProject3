from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count_s, res = Counter(s), ""
        print(count_s.items())
        print([(k * v) for k, v in count_s.items()])
        print(count_s['e']*'d')
        for char in order:
            if char in count_s:
                res += (char * count_s[char])
                del count_s[char]

        return res + "".join([(k * v) for k, v in count_s.items()])


'''"kqep"
"pekeq"'''
obj = Solution()
print(obj.customSortString('kqep','pekeq'))

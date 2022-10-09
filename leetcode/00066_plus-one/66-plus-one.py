class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        s = ""
        for d in digits:
            s = s+str(d)

        s = int(s)+1

        s = [str(i) for i in str(s)]

        return s

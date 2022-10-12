class Solution:
    def hammingWeight(self, n: int) -> int:
        # print(n)
        count = 0
        # binary = str(bin(n))
        # print(binary)

        # for b in binary:
        #     if b=='1':
        #         count+=1
        while n:
            n &= n-1
            print(n)
            count += 1
            # count+=n%2
            # n = n>>1
        return count

class Solution:
    def isHappy(self, n: int) -> bool:

        def square(num):

            sum = 0
            num = str(num)
            for i in range(len(num)):
                sum += int(num[i])*int(num[i])

            return sum

        present_num = n
        visited = set()

        while present_num not in visited:
            visited.add(present_num)
            num = square(present_num)
            if num == 1:
                return True
            else:
                present_num = num

        return False

class DetectSquares:

    def __init__(self):
        self.data = []
        self.pointCount = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.data.append(point)
        self.pointCount[tuple(point)] += 1

        # print(self.data, self.pointCount)

    def count(self, point: List[int]) -> int:

        # print(self.data, point)

        res = 0
        qx, qy = point[0], point[1]

        for p in self.data:
            x, y = p[0], p[1]
            if (abs(qx-x) != abs(qy-y)) or (qx == x and qy == y):
                continue

            if (x, qy) in self.pointCount and (qx, y) in self.pointCount:
                res += self.pointCount[(x, qy)] * self.pointCount[(qx, y)]

        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)

from collections import defaultdict
from typing import List

class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)
        self.points_by_x = defaultdict(list)

    def add(self, point: List[int]) -> None:
        x, y = point

        self.points[(x, y)] += 1
        self.points_by_x[x].append((x, y))

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        result = 0

        for x2, y2 in self.points_by_x[x1]:

            if y2 == y1:
                continue

            side_length = abs(y2 - y1)

            # Square to the right and square to the left
            for x3 in (x1 + side_length, x1 - side_length):
                result += (
                    self.points[(x3, y1)]
                    * self.points[(x3, y2)]
                )

        return result
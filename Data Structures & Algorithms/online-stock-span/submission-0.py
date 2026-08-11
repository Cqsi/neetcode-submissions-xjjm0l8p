class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        self.stack.append(price)
        cur = self.stack.copy()
        l = 0
        while cur and cur[-1] <= price:
            cur.pop()
            l += 1
        return l


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
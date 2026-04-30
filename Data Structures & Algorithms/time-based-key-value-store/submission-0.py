class TimeMap:

    def __init__(self):
        self.data = {} # key -> (value, timestamp)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data:
            self.data[key].append((value, timestamp))
        else:
            self.data[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data or len(self.data[key]) == 0:
            return ""
        
        stamps = self.data[key]
        lo = 0
        hi = len(stamps)-1
        result = ""

        while lo <= hi:
            mid = (lo+hi)//2
            if stamps[mid][1] <= timestamp:
                # this ensures that its less than or equal to as in the assigment description
                result = stamps[mid][0]
                lo = mid + 1
            else:
                hi = mid - 1

        return result

class Interval:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        
    def __eq__(self, other):
        return self.left == other.left and self.right == other.right
    
    def __lt__(self, other):
        if self.left == other.left:
            return self.right < other.right
        return self.left < other.left
    
    def __repr__(self):
        return f"left: {self.left}, right: {self.right}"
            

def merge_intervals(intervals:list[Interval]) -> list[Interval]:
    intervals.sort()
    res: list[Interval] = []
    i, N = 0, len(intervals)
    while i < N:
        curr = intervals[i]
        k = 1
        while i + k < N and intervals[i+k].left <= curr.right:
            curr.right = max(intervals[i+k].right, curr.right)
            k += 1
        res.append(curr)
        i += k
    return res

intervals = [Interval(3, 5), Interval(4, 6), Interval(20, 30), Interval(10, 50), Interval(7, 7), Interval(2, 6), Interval(4, 6)]
res = merge_intervals(intervals)

for interval in res:
    print(interval)

class SquareIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            square = self.current ** 2
            self.current += 1
            return square
start_num = 1
end_num = 5
square_iter = SquareIterator(start_num, end_num)
for square in square_iter:
    print(square)

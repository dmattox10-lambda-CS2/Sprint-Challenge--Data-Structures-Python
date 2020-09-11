class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []
        self.index = 0

    def append(self, item):
        if len(self.buffer) < self.capacity:
            self.buffer.append(item)
        else:
            self.buffer[self.index] = item
        if self.index < self.capacity - 1:
            self.index += 1
        else:
            self.index = 0

    def get(self):
        return self.buffer

class Queue:

    def __init__(self):
        self.rear = -1
        self.data = []

    def enqueue(self, value):
        self.data.append(value)
        self.rear += 1

    def dequeue(self):
        try:
            value = self.data[0]
            del self.data[0]
            self.rear -= 1
            return value
        except:
            return None

    def isEmpty(self):
        if self.rear == -1:
            return True
        else:
            return False

    def peek(self):
        try:
            value = self.data[0]
            return value
        except:
            None
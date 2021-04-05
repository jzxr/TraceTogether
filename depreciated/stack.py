class Stack:
    
    def __init__(self):
        self.top = -1
        self.data = []

    def push(self, value):
        self.data.append(0)
        self.top += 1
        self.data[self.top] = value

    def pop(self):
        try:
            value = self.data[self.top]
            del self.data[self.top]
            self.top -= 1
            return value
        except:
            None

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def peek(self):
        try:
            value = self.data[self.top]
            return value
        except:
            None
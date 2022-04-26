'''
https://leetcode.com/problems/implement-queue-using-stacks/
'''

class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        result = self.queue[0]
        self.queue = self.queue[1:]
        return result

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0
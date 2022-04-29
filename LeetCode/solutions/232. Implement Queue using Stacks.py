'''
문제 이름 : 232. Implement Queue using Stacks
문제 링크 : https://leetcode.com/problems/implement-queue-using-stacks/
문제 풀이 : stack 책 쌓기, queue 줄 스기
시간 복잡도 : O(N)
공간 복잡도 : O(1)
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
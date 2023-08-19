from collections import deque

stack1 = deque()
stack1.append(10)
stack1.append(20)
stack1.append(30)

stack1.pop()
stack1.append(40)
print(stack1)


queue1 = deque()
queue1.append(10)
queue1.append(20)
queue1.append(30)
queue1.popleft()
queue1.append(40)
queue1.popleft()
print(queue1)
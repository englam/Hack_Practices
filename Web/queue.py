import Queue
# -*- coding: utf-8 -*-

#排列用 類似QoS , Queue

q = Queue.Queue()

for i in range(5):
    q.put(i)

while not q.empty():
    print q.get()
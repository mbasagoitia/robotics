import numpy as np
import matplotlib.pyplot as plt
from collections import deque, defaultdict
from heapq import heapify, heappush, heappop


map = np.ones((200,300))*255

rows, cols = 20, 30
grid = (np.random.rand(rows, cols) < 0.2).astype(float)

qstart = (100,150)
qgoal = (np.random.randint(0,len(map)),np.random.randint(0,len(map[0])))

G = {qstart : []}
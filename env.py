import numpy as np

class GridWorld:
    def __init__(self, size=10):
        self.size = size
        self.obstacles = [(3,3),(3,4),(4,3),(6,6)]
        self.reset()

    def reset(self):
        self.agent_pos = [0, 0]
        self.goal = [self.size-1, self.size-1]
        return self.get_state()

    def get_state(self):
        return np.array(self.agent_pos + self.goal, dtype=np.float32)

    def step(self, action):
        x, y = self.agent_pos

        if action == 0: x -= 1
        if action == 1: x += 1
        if action == 2: y -= 1
        if action == 3: y += 1

        if x < 0 or y < 0 or x >= self.size or y >= self.size:
            return self.get_state(), -10, False

        self.agent_pos = [x, y]

        if tuple(self.agent_pos) in self.obstacles:
            return self.get_state(), -100, True

        if self.agent_pos == self.goal:
            return self.get_state(), 100, True

        return self.get_state(), -1, False

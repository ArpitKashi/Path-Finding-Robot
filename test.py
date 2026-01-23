from env import GridWorld
from agent import DQNAgent

env = GridWorld()
agent = DQNAgent(4, 4)
agent.epsilon = 0  # no random actions

state = env.reset()

print("Robot Path:")
for step in range(50):
    action = agent.act(state)
    state, reward, done = env.step(action)
    print(env.agent_pos)
    if done:
        print("Goal Reached 🎯")
        break

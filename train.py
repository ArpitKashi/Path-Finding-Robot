from env import GridWorld
from agent import DQNAgent

env = GridWorld()
agent = DQNAgent(state_size=4, action_size=4)

episodes = 500

for e in range(episodes):
    state = env.reset()
    for step in range(200):
        action = agent.act(state)
        next_state, reward, done = env.step(action)
        agent.remember(state, action, reward, next_state, done)
        state = next_state

        if done:
            print(f"Episode {e+1}/{episodes} finished in {step} steps")
            break

        if len(agent.memory) > 32:
            agent.replay(32)

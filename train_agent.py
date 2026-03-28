import numpy as np
import matplotlib.pyplot as plt
from water_tank_env import WaterTankEnv
import random

env = WaterTankEnv()

state_bins = 20
actions = 3
q_table = np.zeros((state_bins, actions))

# ✅ SAFE DISCRETIZATION FUNCTION
def discretize(state):
    idx = int(state[0] // 5)
    return min(idx, state_bins - 1)   # ensures max index = 19

episodes = 5000
alpha = 0.1
gamma = 0.95
epsilon = 1.0
epsilon_decay = 0.995
min_epsilon = 0.01

rewards = []

for ep in range(episodes):
    state = env.reset()
    state_idx = discretize(state)
    total_reward = 0

    for step in range(200):
        # Exploration vs Exploitation
        if random.uniform(0, 1) < epsilon:
            action = random.randint(0, 2)
        else:
            action = np.argmax(q_table[state_idx])

        next_state, reward, done = env.step(action)
        next_state_idx = discretize(next_state)

        # Q-learning update
        q_table[state_idx, action] += alpha * (
            reward + gamma * np.max(q_table[next_state_idx]) - q_table[state_idx, action]
        )

        state_idx = next_state_idx
        total_reward += reward

    epsilon = max(min_epsilon, epsilon * epsilon_decay)
    rewards.append(total_reward)

print("Training Complete!")

# ✅ Save trained model
np.save("q_table.npy", q_table)
print("Q-table saved!")

# Plot learning curve
plt.plot(rewards)
plt.title("Training Rewards Over Episodes")
plt.xlabel("Episodes")
plt.ylabel("Total Reward")
plt.show()


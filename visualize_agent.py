import matplotlib.pyplot as plt
from water_tank_env import WaterTankEnv
import numpy as np
import time

env = WaterTankEnv()
state = env.reset()

levels = []

for _ in range(200):
    action = np.argmax(np.random.rand(3))  # Replace with trained policy later
    state, reward, done = env.step(action)
    levels.append(state[0])

plt.ion()
fig, ax = plt.subplots()

for level in levels:
    ax.clear()
    ax.bar(["Water Level"], [level])
    ax.set_ylim(0, 100)
    ax.set_title(f"Tank Level: {level:.2f}")
    plt.pause(0.1)

plt.ioff()
plt.show()

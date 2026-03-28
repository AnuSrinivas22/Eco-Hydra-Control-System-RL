import numpy as np
import random

class WaterTankEnv:
    def __init__(self):
        self.max_level = 100
        self.min_level = 0
        self.ideal_level = 70
        self.reset()

    def reset(self):
        self.water_level = random.randint(40, 80)
        return self._get_state()

    def step(self, action):
        # Random inflow and demand
        inflow = random.uniform(0, 2)
        demand = random.uniform(1, 3)

        # Pump effect
        if action == 0:      # OFF
            pump_flow = 0
        elif action == 1:    # LOW
            pump_flow = 2
        else:                # HIGH
            pump_flow = 4

        # Update water level
        self.water_level += inflow + pump_flow - demand
        self.water_level = max(self.min_level, min(self.water_level, self.max_level))

        # Reward calculation
        reward = -abs(self.water_level - self.ideal_level) * 0.5

        if self.water_level >= self.max_level or self.water_level <= self.min_level:
            reward -= 100

        if action == 2:
            reward -= 2
        elif action == 1:
            reward -= 1

        done = False  # continuous process
        return self._get_state(), reward, done

    def _get_state(self):
        return np.array([self.water_level])



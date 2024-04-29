import numpy as np
import matplotlib.pyplot as plt

class Agent:
    def __init__(self):
        self.is_buyer = False
        self.is_user = False

class Product:
    def __init__(self, decay_time):
        self.decay_time = decay_time
        self.days_until_decay = decay_time

    def degrade(self):
        self.days_until_decay -= 1

class Environment:
    def __init__(self, num_agents, initial_buyer_percentage, decay_time):
        self.num_agents = num_agents
        self.agents = [Agent() for _ in range(num_agents)]
        self.product = Product(decay_time)
        self.initial_buyer_percentage = initial_buyer_percentage
        self.buyers = []

    def initialize_buyers(self):
        num_initial_buyers = int(self.initial_buyer_percentage * self.num_agents)
        buyer_indices = np.random.choice(range(self.num_agents), num_initial_buyers, replace=False)
        for idx in buyer_indices:
            self.agents[idx].is_buyer = True
            self.buyers.append(idx)

    def simulate_day(self):
        for agent in self.agents:
            if not agent.is_user:
                if np.random.rand() < self.initial_buyer_percentage:
                    agent.is_buyer = True
                    self.buyers.append(self.agents.index(agent))

        for buyer_idx in self.buyers:
            if not self.agents[buyer_idx].is_user:
                self.agents[buyer_idx].is_user = True
                if np.random.rand() < 0.5:  # Probability of notifying another potential buyer
                    notify_idx = np.random.choice([idx for idx in range(self.num_agents) if idx != buyer_idx])
                    self.agents[notify_idx].is_buyer = True
                    self.buyers.append(notify_idx)

        self.product.degrade()
        if self.product.days_until_decay == 0:
            self.product = Product(self.product.decay_time)
            self.buyers = []

    def visualize(self, day):
        agent_positions = np.zeros(self.num_agents)
        for idx, agent in enumerate(self.agents):
            if agent.is_user:
                agent_positions[idx] = 1

        plt.figure(figsize=(10, 6))
        plt.bar(range(self.num_agents), agent_positions, color='skyblue', alpha=0.7)
        plt.title('Agent Population on Day {}'.format(day))
        plt.xlabel('Agent Index')
        plt.ylabel('User Status')
        plt.ylim(0, 1.2)
        plt.xticks([])
        plt.yticks([0, 1], ['Not User', 'User'])
        plt.grid(axis='y', linestyle='--', alpha=0.5)
        plt.show()

# Example usage
num_agents = 100
initial_buyer_percentage = 0.1
decay_time = 5
num_days = 10

env = Environment(num_agents, initial_buyer_percentage, decay_time)
env.initialize_buyers()

for day in range(num_days):
    env.simulate_day()
    env.visualize(day+1)

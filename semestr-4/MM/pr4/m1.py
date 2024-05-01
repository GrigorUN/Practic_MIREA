import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

class Environment:
    def __init__(self, size):
        self.size = size
        self.grid = np.zeros(size)
    
    def add_agent(self, position):
        self.grid[position] = 1
    
    def remove_agent(self, position):
        self.grid[position] = 0
    
    def add_product(self, position):
        self.grid[position] = 2
    
    def remove_product(self, position):
        self.grid[position] = 0
    
    def decay_product(self, position):
        self.grid[position] = 3
    
    def display(self):
        plt.imshow(self.grid, cmap='YlGn', origin='lower')
        plt.colorbar(ticks=[0, 1, 2, 3], label='State')
        plt.title('Agents and Products Distribution')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()

class Simulation:
    def __init__(self, environment_size, agent_count, product_decay_time):
        self.environment = Environment(environment_size)
        self.agent_count = agent_count
        self.product_decay_time = product_decay_time
        self.agents = []
        self.products = []
    
    def initialize_agents(self):
        for _ in range(self.agent_count):
            position = (random.randint(0, self.environment.size[0]-1), random.randint(0, self.environment.size[1]-1))
            self.agents.append(position)
            self.environment.add_agent(position)
    
    def step(self):
        for agent in self.agents:
            if random.random() < 0.1:  # Вероятность покупки продукта
                self.products.append(agent)
                self.environment.remove_agent(agent)
                self.agents.remove(agent)
        
        for product in self.products:
            if random.random() < 0.2:  # Вероятность оповещения другого агента
                new_buyer = (random.randint(0, self.environment.size[0]-1), random.randint(0, self.environment.size[1]-1))
                self.agents.append(new_buyer)
                self.environment.add_agent(new_buyer)
        
        for product in self.products[:]:  # Проверка порчи продукта
            if random.random() < 0.3:  # Вероятность порчи продукта
                self.products.remove(product)
                self.environment.decay_product(product)
        
        for _ in range(self.product_decay_time):  # Прошло время порчи продукта
            self.products = [(x, y) for (x, y) in self.products if (x, y) not in self.agents]
        
    def run(self, steps):
        self.initialize_agents()
        fig = plt.figure()
        ims = []
        for _ in range(steps):
            self.step()
            im = plt.imshow(self.environment.grid, cmap='YlGn', animated=True)
            ims.append([im])
        ani = animation.ArtistAnimation(fig, ims, interval=500, blit=True, repeat_delay=1000)
        plt.colorbar(im, label='State')
        plt.title('Agents and Products Distribution Over Time')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()

# Параметры симуляции
environment_size = (20, 20)
agent_count = 50
product_decay_time = 3
simulation_steps = 10

# Запуск симуляции
simulation = Simulation(environment_size, agent_count, product_decay_time)
simulation.run(simulation_steps)

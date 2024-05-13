import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

class Marketplace:
    def __init__(self, size):
        self.size = size
        self.grid = np.zeros(size)
    
    def add_user(self, position):
        self.grid[position] = 1
    
    def remove_user(self, position):
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
        plt.title('Пользователи и распространение продуктов')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()

class MarketplaceSimulation:
    def __init__(self, marketplace_size, user_count, product_decay_time):
        self.marketplace = Marketplace(marketplace_size)
        self.user_count = user_count
        self.product_decay_time = product_decay_time
        self.users = []
        self.products = []
    
    def initialize_users(self):
        for _ in range(self.user_count):
            position = (random.randint(0, self.marketplace.size[0]-1), random.randint(0, self.marketplace.size[1]-1))
            self.users.append(position)
            self.marketplace.add_user(position)
    
    def step(self):
        for user in self.users:
            if random.random() < 0.1:
                self.products.append(user)
                self.marketplace.remove_user(user)
                self.users.remove(user)
        
        for product in self.products:
            if random.random() < 0.2:
                new_viewer = (random.randint(0, self.marketplace.size[0]-1), random.randint(0, self.marketplace.size[1]-1))
                self.users.append(new_viewer)
                self.marketplace.add_user(new_viewer)
        
        for product in self.products[:]:
            if random.random() < 0.3: 
                self.products.remove(product)
                self.marketplace.decay_product(product)
        
        for _ in range(self.product_decay_time):
            self.products = [(x, y) for (x, y) in self.products if (x, y) not in self.users]
        
    def run(self, steps):
        self.initialize_users()
        fig = plt.figure()
        ims = []
        for _ in range(steps):
            self.step()
            im = plt.imshow(self.marketplace.grid, cmap='YlGn', animated=True)
            ims.append([im])
        ani = animation.ArtistAnimation(fig, ims, interval=500, blit=True, repeat_delay=1000)
        plt.colorbar(im, label='State')
        plt.title('Распределение пользователей и продуктов с течением времени')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()

# Параметры симуляции
marketplace_size = (20, 20)
user_count = 50
product_decay_time = 3
simulation_steps = 10

# Запуск симуляции
simulation = MarketplaceSimulation(marketplace_size, user_count, product_decay_time)
simulation.run(simulation_steps)

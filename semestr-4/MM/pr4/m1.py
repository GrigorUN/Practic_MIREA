import tkinter as tk
import random

class Seller:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.state = "Новичок"
        self.shape = canvas.create_rectangle(x-4, y-4, x+4, y+4, fill="blue")

    def become_experienced(self):
        if self.state == "Новичок":
            self.state = "Опытный"
            self.canvas.itemconfig(self.shape, fill="orange")

    def become_successful(self):
        if self.state == "Опытный":
            self.state = "Успешный"
            self.canvas.itemconfig(self.shape, fill="green")

    def become_newbie(self):
        if self.state == "Опытный":
            self.state = "Новичок"
            self.canvas.itemconfig(self.shape, fill="blue")

class MarketplaceSimulation:
    def __init__(self, width, height, num_sellers, experience_interval, success_interval, demote_interval, return_interval):
        self.width = width
        self.height = height
        self.num_sellers = num_sellers
        self.experience_interval = experience_interval
        self.success_interval = success_interval
        self.demote_interval = demote_interval
        self.return_interval = return_interval
        self.sellers = []
        self.experienced_count = 0

        self.root = tk.Tk()
        self.root.title("Симуляция маркетплейсов")
        self.canvas = tk.Canvas(self.root, width=width, height=height, bg="white")
        self.canvas.pack()

        self.promote_button = tk.Button(self.root, text="Продвигать продавцов", command=self.promote_random_seller)
        self.promote_button.pack(side=tk.LEFT)

        self.increase_experience_button = tk.Button(self.root, text="Увеличить промоушен", command=self.increase_experience_interval)
        self.increase_experience_button.pack(side=tk.LEFT)

        self.decrease_experience_button = tk.Button(self.root, text="Уменьшить промоушен", command=self.decrease_experience_interval)
        self.decrease_experience_button.pack(side=tk.LEFT)

        self.increase_success_button = tk.Button(self.root, text="Увеличить продажи", command=self.increase_success_interval)
        self.increase_success_button.pack(side=tk.LEFT)

        self.decrease_success_button = tk.Button(self.root, text="Уменьшить продажи", command=self.decrease_success_interval)
        self.decrease_success_button.pack(side=tk.LEFT)

        for _ in range(num_sellers):
            x = random.randint(0, width)
            y = random.randint(0, height)
            seller = Seller(self.canvas, x, y)
            self.sellers.append(seller)

    def promote_random_seller(self):
        for seller in self.sellers:
            if seller.state == "Новичок":
                if random.random() < self.experience_interval:
                    seller.become_experienced()
                    self.experienced_count += 1

        self.root.after(100, self.promote_random_seller)

    def update(self):
        if self.experienced_count > self.num_sellers / 2:
            self.success_interval = 0.1

        for seller in self.sellers:
            if seller.state == "Опытный":
                if random.random() < self.success_interval:
                    seller.become_successful()
                    self.experienced_count -= 1
                elif random.random() < self.demote_interval:
                    seller.become_newbie()
                    self.experienced_count -= 1
            elif seller.state == "Успешный":
                if random.random() < self.return_interval:
                    seller.state = "Новичок"
                    seller.canvas.itemconfig(seller.shape, fill="blue")
                    self.experienced_count -= 1

        self.root.after(100, self.update)

    def increase_experience_interval(self):
        self.experience_interval *= 1.1

    def decrease_experience_interval(self):
        self.experience_interval *= 0.9

    def increase_success_interval(self):
        self.success_interval *= 0.8

    def decrease_success_interval(self):
        self.success_interval *= 1.2

    def run(self):
        self.update()
        self.root.mainloop()

WIDTH = 500
HEIGHT = 500
NUM_SELLERS = 500
EXPERIENCE_INTERVAL = 0.02
SUCCESS_INTERVAL = 0.05
DEMOTE_INTERVAL = 0.03
RETURN_INTERVAL = 0.05

sim = MarketplaceSimulation(WIDTH, HEIGHT, NUM_SELLERS, EXPERIENCE_INTERVAL, SUCCESS_INTERVAL, DEMOTE_INTERVAL, RETURN_INTERVAL)
sim.run()

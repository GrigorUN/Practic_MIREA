import numpy as np
import matplotlib.pyplot as plt

def generate_sprite(x,y):
    sprite = np.zeros((x, y), dtype=int)

    for i in range(x):
        for j in range(y//2):
            sprite[i][j] = np.random.randint(0, 2)
            
    sprite += np.fliplr(sprite)

    return sprite

def plot_sprite(sprite):
    plt.imshow(sprite, cmap='gray', interpolation='nearest')
    plt.axis('on')
    plt.show()

sprite = generate_sprite(5,5)
plot_sprite(sprite)

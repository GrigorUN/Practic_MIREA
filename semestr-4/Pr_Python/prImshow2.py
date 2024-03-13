import numpy as np
import matplotlib.pyplot as plt

def generate_sprite(x, y):
    sprite = np.zeros((x, y), dtype=int)

    for i in range(x):
        for j in range(y//2):
            sprite[i][j] = np.random.randint(0, 2)
            
    sprite += np.fliplr(sprite)

    return sprite

def add_border(sprite):
    new_sprite = np.zeros((sprite.shape[0] + 2, sprite.shape[1] + 2), dtype=int)
    new_sprite[1:-1, 1:-1] = sprite
    new_sprite[0, :] = 1
    new_sprite[-1, :] = 1
    new_sprite[:, 0] = 1
    new_sprite[:, -1] = 1
    return new_sprite

def generate_map(num_sprites, sprite_size):
    map_size = num_sprites * (sprite_size + 2)
    map_sprites = np.zeros((map_size, map_size), dtype=int)

    for i in range(num_sprites):
        for j in range(num_sprites):
            sprite = generate_sprite(sprite_size, sprite_size)
            sprite_with_border = add_border(sprite)
            map_sprites[i*(sprite_size+2):(i+1)*(sprite_size+2), j*(sprite_size+2):(j+1)*(sprite_size+2)] = sprite_with_border

    return map_sprites

def plot_sprite(sprite):
    plt.imshow(sprite, cmap='Greys', interpolation='nearest')
    plt.axis('on')
    plt.show()

num_sprites = 15
sprite_size = 7
map_sprites = generate_map(num_sprites, sprite_size)
plot_sprite(map_sprites)

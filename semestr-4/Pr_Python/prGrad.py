import math
import tkinter as tk


def draw(shader, width, height):
    image = bytearray((0, 0, 0) * width * height)
    for y in range(height):
        for x in range(width):
            pos = (width * y + x) * 3
            color = shader(x / width, y / height)
            normalized = [max(min(int(c * 255), 255), 0) for c in color]
            image[pos:pos + 3] = normalized
    header = bytes(f'P6\n{width} {height}\n255\n', 'ascii')
    return header + image


def main(shader):
    label = tk.Label()
    img = tk.PhotoImage(data=draw(shader, 256, 256)).zoom(2, 2)
    label.pack()
    label.config(image=img)
    tk.mainloop()


def shader(x, y):
    # ( x – a)**2 + ( y – b)**2 = R**2
    r = 0.2 - ((x * 0.95 - 0.5) ** 2 + (y * 0.95 - 0.5) ** 2)
    g = 0.2 - ((x * 1.05 - 0.5) ** 2 + (y * 1.05 - 0.5) ** 2)
    return r * 4, g * 4, 0


main(shader)
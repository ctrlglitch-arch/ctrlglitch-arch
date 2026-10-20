#!/usr/bin/env python3
"""
A real-time rotating ASCII donut rendered directly in the terminal.
This does NOT rotate a GIF or load any image.

Run:
    python spinning_donut.py

Stop with Ctrl+C.
"""
import math
import os
import time

WIDTH = 80
HEIGHT = 24
CHARS = ".,-~:;=!*#$@"
A = 0.0
B = 0.0

def render(a, b):
    output = [" "] * (WIDTH * HEIGHT)
    zbuffer = [0.0] * (WIDTH * HEIGHT)

    for theta_i in range(90):
        theta = theta_i * 2 * math.pi / 90
        ct = math.cos(theta)
        st = math.sin(theta)

        for phi_i in range(314):
            phi = phi_i * 2 * math.pi / 314
            cp = math.cos(phi)
            sp = math.sin(phi)

            # 3D torus surface, rotated around two axes.
            circle_x = 2 + ct
            circle_y = st

            x = circle_x * (math.cos(b) * cp + math.sin(a) * math.sin(b) * sp) \
                - circle_y * math.cos(a) * math.sin(b)
            y = circle_x * (math.sin(b) * cp - math.sin(a) * math.cos(b) * sp) \
                + circle_y * math.cos(a) * math.cos(b)
            z = 5 + math.cos(a) * circle_x * sp + circle_y * math.sin(a)
            ooz = 1 / z

            xp = int(WIDTH / 2 + 30 * ooz * x)
            yp = int(HEIGHT / 2 - 15 * ooz * y)
            if 0 <= xp < WIDTH and 0 <= yp < HEIGHT:
                idx = xp + WIDTH * yp
                luminance = cp * ct * math.sin(b) - math.cos(a) * ct * sp \
                    - math.sin(a) * st + math.cos(b) * (math.cos(a) * st - ct * math.sin(a) * sp)
                if ooz > zbuffer[idx]:
                    zbuffer[idx] = ooz
                    char_index = max(0, min(len(CHARS) - 1,
                                            int((luminance + 1) * 0.5 * (len(CHARS) - 1))))
                    output[idx] = CHARS[char_index]

    return "\033[H" + "\n".join(
        "".join(output[y * WIDTH:(y + 1) * WIDTH]) for y in range(HEIGHT)
    )

def main():
    global A, B
    # Clear terminal once; subsequent frames repaint in place.
    os.system("cls" if os.name == "nt" else "clear")
    try:
        while True:
            print(render(A, B), end="", flush=True)
            A += 0.07
            B += 0.03
            time.sleep(0.025)
    except KeyboardInterrupt:
        print("\nDonut stopped.")

if __name__ == "__main__":
    main()

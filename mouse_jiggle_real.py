import pyautogui
import time
import random

def mouse_jiggle():
    try:
        while True:
            # Generate random offsets for x and y coordinates
            x_offset = random.randint(-10, 10)
            y_offset = random.randint(-10, 10)

            # Get current mouse position
            current_x, current_y = pyautogui.position()

            # Move the mouse to the new position
            pyautogui.moveRel(x_offset, y_offset, duration=0.1)

            print(f"Jiggling mouse: offset x={x_offset}, y={y_offset}")

            # Wait for a random interval between 1 and 3 seconds
            time.sleep(random.uniform(1, 3))
    except KeyboardInterrupt:
        print("Mouse jiggle stopped.")

if __name__ == "__main__":
    mouse_jiggle()

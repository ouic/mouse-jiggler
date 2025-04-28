import random
import asyncio

async def mouse_jiggle():
    try:
        while True:
            # Simulate a small mouse movement
            x_offset = random.randint(-5, 5)
            y_offset = random.randint(-5, 5)

            print(f"Simulating mouse jiggle: offset x={x_offset}, y={y_offset}")
            
            # Wait for a random interval between 1 and 5 seconds
            await asyncio.sleep(random.randint(1, 5))
    except KeyboardInterrupt:
        print("Mouse jiggle stopped.")

if __name__ == "__main__":
    asyncio.run(mouse_jiggle())

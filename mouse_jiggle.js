async function mouseJiggle() {
  try {
    while (true) {
      const xOffset = Math.floor(Math.random() * 10) - 5;
      const yOffset = Math.floor(Math.random() * 10) - 5;

      console.log(`Simulating mouse jiggle: offset x=${xOffset}, y=${yOffset}`);

      // Wait for a random interval between 1 and 5 seconds
      const delay = Math.floor(Math.random() * 4000) + 1000; // milliseconds
      await new Promise(resolve => setTimeout(resolve, delay));
    }
  } catch (err) {
    console.log("Mouse jiggle stopped.");
  }
}

mouseJiggle();

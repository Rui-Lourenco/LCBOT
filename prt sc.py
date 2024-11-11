import time
import os
from datetime import datetime
from PIL import ImageGrab
import keyboard  # For detecting key presses

# Parameters
screenshot_interval = 5  # Time in seconds between each screenshot
output_folder = "./screenshots"  # Folder to save screenshots

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

def take_screenshot():
    # Capture the screenq
    screenshot = ImageGrab.grab()
    
    # Create a timestamped filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(output_folder, f"screenshot_{timestamp}.png")
    
    # Save the screenshot
    screenshot.save(filename)
    print(f"Screenshot saved: {filename}")

# Main loop with start/stop functionality
is_active = False  # Flag to control the screenshotting state

print("Press 'q' to start/stop screenshot capture.")

try:
    while True:
        # Check for 'q' key press to toggle the screenshot state
        if keyboard.is_pressed('q'):
            is_active = not is_active
            print("Screenshot capture " + ("started." if is_active else "stopped."))
            time.sleep(0.5)  # Prevent multiple toggles from one key press

        # If active, take a screenshot at the defined interval
        if is_active:
            start_time = time.time()
            while is_active:
                take_screenshot()
                
                # Wait for the specified interval or check for stop signal
                while time.time() - start_time < screenshot_interval:
                    if keyboard.is_pressed('q'):
                        is_active = False
                        print("Screenshot capture stopped.")
                        time.sleep(0.5)  # Prevent multiple toggles
                        break
                start_time = time.time()
except KeyboardInterrupt:
    print("Exited the program.")


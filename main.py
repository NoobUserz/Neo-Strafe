import keyboard
from pynput import mouse
import threading

scroll_count = 0  # Variable to keep track of scroll count
scroll_up = True  # Flag to indicate scroll direction
scroll_active = False  # Flag to indicate if scrolling is active
actions = ['space', 'w+space', 'space+w', 'space+w', 'space+w', 'space+w', 'space+w', 'space+w', 'space+w', 'space+w', 'space+w+d', 'space+w+d', 'space+w+d', 'space+w+d', 'space+w+d', 'space+w+d', 'space+w+d', 'space+w+d', 'space+d', 'space+d', 'space+d', 'space+d', 'space+d', 'space+d', 'space+d', 'space+d', 'space+s+d', 'space+s+d', 'space+s+d', 'space+s+d', 'space+s+d', 'space+s+d', 'space+s+d', 'space+s+d', 'space+s', 'space+s', 'space+s', 'space+s', 'space+s', 'space+s', 'space+s', 'space+s', 'space+s+a', 'space+s+a', 'space+s+a', 'space+s+a', 'space+s+a', 'space+s+a', 'space+s+a', 'space+s+a', 'space+a', 'space+a', 'space+a', 'space+a', 'space+a', 'space+a', 'space+a', 'space+a', 'space+w+a', 'space+w+a', 'space+w+a', 'space+w+a', 'space+w+a', 'space+w+a', 'space+w+a', 'space+w+a']
scroll_increment = 2  # Define scroll increment
w_intensity = 3  # Define intensity of 'w' input when scrolling is not active
lock = threading.Lock()  # Lock to synchronize access to shared variables

def on_scroll(x, y, dx, dy):
    """Handle scroll events."""
    global scroll_count, scroll_up, actions, scroll_active

    with lock:
        if not scroll_active:
            if dy < 0:  # If scrolling down and not active, simulate 'w' key press multiple times
                for _ in range(w_intensity):
                    if not keyboard.is_pressed('w'):  # Check if 'w' is not already pressed manually
                        keyboard.press_and_release('w')
            return

        if dy > 0:
            scroll_up = True
        else:
            scroll_up = False

        scroll_count += scroll_increment  # Increment the scroll count

        # Get action based on scroll count and perform it
        action = actions[(scroll_count - 1) % len(actions)]
        keyboard.press_and_release(action)

def on_press(key):

    global scroll_active, scroll_count

    if key.name == 'space':
        if scroll_active:  # Deactivate scrolling
            scroll_count = 0  # Reset scroll count when deactivating scrolling
            print("Scrolling deactivated")
            scroll_active = False
    elif key.name == '4':
        if not scroll_active:
            print("Scrolling activated")
            scroll_active = True

# Start listening for key press
keyboard.on_press(on_press)

# Start listening to scroll events and key presses
listener = mouse.Listener(on_scroll=on_scroll)
listener.start()

# Keep the program running
keyboard.wait('=')  # Wait until '=' key is pressed to exit

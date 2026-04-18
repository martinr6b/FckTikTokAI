import json
import time

from utils.adb import get_screen, tap, key
from utils.vision import find_template

with open("config.json") as f:
    config = json.load(f)

ATTEMPTS = config.get("attempts", 1)
DELAY = config.get("delay_between_steps", 1.0)
STEPS = config["steps"]

for attempt in range(ATTEMPTS):
    print(f"\n=== Attempt {attempt+1}/{ATTEMPTS} ===")

    for step in STEPS:
        step_type = step["type"]

        if step_type == "template":
            print(f"Looking for {step['image']}")

            screen = get_screen()
            pos = find_template(
                screen,
                step["image"],
                step.get("threshold", 0.8)
            )

            if pos:
                print(f"Found at {pos}, tapping")
                tap(*pos)
            else:
                print("Not found")

        elif step_type == "click":
            print(f"Clicking at ({step['x']}, {step['y']})")
            tap(step["x"], step["y"])

        elif step_type == "key":
            print(f"Sending key {step['keycode']}")
            key(step["keycode"])

        time.sleep(DELAY)
import subprocess
import numpy as np
import cv2

def get_screen():
    result = subprocess.run(
        ["adb", "exec-out", "screencap", "-p"],
        stdout=subprocess.PIPE
    )
    img = np.frombuffer(result.stdout, np.uint8)
    return cv2.imdecode(img, cv2.IMREAD_COLOR)

def tap(x, y):
    subprocess.run(["adb", "shell", "input", "tap", str(x), str(y)])

def key(keycode):
    subprocess.run(["adb", "shell", "input", "keyevent", str(keycode)])
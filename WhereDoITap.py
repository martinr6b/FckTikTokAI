import subprocess
import re
import time

# Matches Android pointer overlay output like: (1053, 1906)
COORD_REGEX = re.compile(r"\((\d+),\s*(\d+)\)")

def enable_pointer():
    subprocess.run(["adb", "shell", "settings", "put", "system", "pointer_location", "1"])

def disable_pointer():
    subprocess.run(["adb", "shell", "settings", "put", "system", "pointer_location", "0"])

def main():
    print("Enabling pointer overlay...")
    enable_pointer()

    subprocess.run(["adb", "logcat", "-c"])

    print("Listening for taps... Press Ctrl+C to stop.\n")

    process = subprocess.Popen(
        ["adb", "logcat"],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True,
        bufsize=1
    )

    last_time = 0

    try:
        for line in process.stdout:
            match = COORD_REGEX.search(line)
            if match:
                now = time.time()

                # simple debounce (prevents duplicate logs per tap)
                if now - last_time < 0.3:
                    continue
                last_time = now

                x = int(match.group(1))
                y = int(match.group(2))

                print(f"Tap at: X={x}, Y={y}")

    except KeyboardInterrupt:
        print("\nStopping...")
        process.terminate()
        disable_pointer()

if __name__ == "__main__":
    main()
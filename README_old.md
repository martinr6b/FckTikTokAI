# FckTikTokAI
 A tool that automatically scrolls your posts removing the "Allow AI to remix content" Option 
## One thing i need to clarify: YES, this code is AI written and i do NOT care as long as my posts are not processed

## How it works:
- Grabs an android device's screen
- Finds the necessary icons it needs to click 
- Clicks them
(That's pretty much it)
(Please note this is being made as a side project on a weekend, this code is far from perfect but it just needs to work)

## What you'll need: 
- An android device
- A computer
- a USB-c cable
- ADB acess
- Time 
- A tiktok account (Obviously, LOL)


## HOW TO USE:

### 1. Prerequisites
- Make sure your TikTok theme is set to **dark mode**
- Download/clone this repository
- Install Python 3.8+ (if you haven't already)
- Connect your Android device via USB with ADB enabled

### 2. Automatic Setup (Recommended)

#### For Linux/macOS:
```bash
chmod +x setup.sh    # Make it executable
./setup.sh           # Run the setup script
```

#### For All Systems (Windows, Linux, macOS):
```bash
python3 setup.py
```

The setup script will:
- ✓ Detect your OS/distribution
- ✓ Install tkinter automatically
- ✓ Create a Python virtual environment
- ✓ Install all dependencies from requirements.txt

### 3. Manual Setup (If automatic fails)

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

**Linux/macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Then install tkinter for your system:
- **Arch Linux:** `sudo pacman -S tk`
- **Ubuntu/Debian:** `sudo apt-get install python3-tk`
- **Fedora:** `sudo dnf install python3-tkinter`
- **macOS:** `brew install python-tk`
- **Windows:** Usually included; reinstall Python if missing

### 4. Running the Application

**Option A: Using the GUI (Recommended)**
```bash
# Activate venv first (optional)
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

# Then run the GUI
python gui.py
```

**Option B: Direct command**
```bash
# Linux/macOS
.venv/bin/python gui.py

# Windows
.venv\Scripts\python.exe gui.py
```

### 5. Configuration

Edit `config.json` to set up your automation:
- **attempts**: Number of times to repeat the sequence
- **delay_between_steps**: Delay between each action (seconds)
- **steps**: Array of actions (click, swipe, template, key)

See `Dconfig.json` for detailed documentation on all options.

### 6. Tools Available

**GUI Application** - User-friendly interface with buttons to:
- Run main automation
- Run tap location finder (shows screen coordinates on tap)
- Stop running scripts
- View real-time output terminal

**Command Line** - Run scripts directly:
```bash
# Run main automation
python main.py

# Run tap location finder
python WhereDoITap.py
```
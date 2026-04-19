# FckTikTokAI 🤖

*A tool that automatically removes the "Allow AI to remix content" option from your TikTok posts*

> **Note:** YES, this code is AI-written and I do NOT care as long as my posts are not processed by AI.

## ✨ Features

- 🔄 **Automated TikTok AI opt-out** - Automatically removes AI processing options
- 📱 **Android device control** - Uses ADB to interact with your Android device
- 🎯 **Template matching** - Smart image recognition for UI elements
- 🖱️ **Multiple input methods** - Click, swipe, and key event support
- 🎨 **Dark mode optimized** - Designed for TikTok's dark theme
- 🖥️ **Cross-platform GUI** - Works on Windows, Linux, and macOS
- ⚙️ **Configurable automation** - JSON-based configuration system

## 🚀 Quick Start

### 1. Prerequisites
- Android device with USB debugging enabled
- ADB installed and working
- TikTok app in **DARK MODE**
- Python 3.8+

### 2. Setup (Universal)
```bash
# Clone or download the repository
git clone https://github.com/yourusername/FckTikTokAI.git
cd FckTikTokAI

# Run universal setup (works on Windows, Linux, macOS)
python3 setup.py
```

### 3. Run
```bash
# Launch the GUI
python gui.py
```

That's it! The setup script automatically handles everything for your operating system.

## 📋 Manual Setup (if needed)

If the automatic setup fails:

1. **Install tkinter** (GUI library):
   - Windows: Usually included with Python
   - Linux: Install system package (`tk`, `python3-tk`, etc.)
   - macOS: `brew install python-tk`

2. **Create virtual environment**:
   ```bash
   python3 -m venv .venv
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 Usage

### GUI Mode (Recommended)
Run `python gui.py` and use the buttons:
- **Run Main** - Execute automation from config.json
- **Run Tap Finder** - Find screen coordinates by tapping
- **Stop Script** - Stop any running automation

### Command Line
```bash
# Run automation
python main.py

# Find tap coordinates
python WhereDoITap.py
```

## ⚙️ Configuration

Edit `config.json` to customize your automation:

```json
{
  "attempts": 10,
  "delay_between_steps": 1.0,
  "steps": [
    {
      "type": "click",
      "x": 500,
      "y": 1200
    },
    {
      "type": "swipe",
      "start_x": 100,
      "start_y": 500,
      "end_x": 900,
      "end_y": 100,
      "duration": 300
    },
    {
      "type": "template",
      "image": "temeplates/icon.png",
      "threshold": 0.8,
      "SkipOnFail": false
    },
    {
      "type": "key",
      "keycode": 4
    }
  ]
}
```

See `Dconfig.json` for complete documentation of all options.

## 🔧 Step Types

| Type | Description | Parameters |
|------|-------------|------------|
| `click` | Tap at coordinates | `x`, `y` |
| `swipe` | Swipe gesture | `start_x`, `start_y`, `end_x`, `end_y`, `duration` |
| `template` | Find and click image | `image`, `threshold`, `SkipOnFail` |
| `key` | Send key event | `keycode` |

## 🐛 Troubleshooting

### Common Issues

**❌ "tkinter not found"**
```bash
# Run setup again
python3 setup.py
```

**❌ "cv2 not found"**
```bash
pip install opencv-python
```

**❌ "adb: command not found"**
- Install ADB and add to PATH
- Enable USB debugging on Android device

**❌ Template matching fails**
- Ensure TikTok is in DARK mode
- Lower `threshold` in config.json (try 0.5-0.7)
- Replace template images with fresh screenshots

**❌ GUI won't start**
- Verify tkinter installation
- Try reinstalling Python with tkinter support

## 📁 Project Structure

```
FckTikTokAI/
├── gui.py              # Main GUI application
├── main.py             # Command-line automation
├── WhereDoITap.py      # Tap coordinate finder
├── setup.py            # Universal setup script
├── config.json         # Configuration file
├── Dconfig.json        # Configuration documentation
├── requirements.txt    # Python dependencies
├── SETUP_GUIDE.txt     # Quick setup guide
├── temeplates/         # Template images folder
├── utils/
│   ├── adb.py         # ADB interaction functions
│   └── vision.py      # Image processing functions
└── README.md          # This file
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source. Feel free to use and modify as needed.

## ⚠️ Disclaimer

- Use at your own risk
- Ensure you comply with TikTok's terms of service
- This is a weekend project - code may not be perfect but it works
- No warranty or support provided

---

*Made with ❤️ and a bit of automation magic*
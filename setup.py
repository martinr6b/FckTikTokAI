#!/usr/bin/env python3
"""
FckTikTokAI Setup Script
Handles installation of dependencies across all systems (Linux, macOS, Windows)
"""

import subprocess
import platform
import sys
import os

class Setup:
    def __init__(self):
        self.system = platform.system()
        self.distro = self._detect_distro()
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.venv_path = os.path.join(self.script_dir, ".venv")
        
    def _detect_distro(self):
        """Detect Linux distribution"""
        if self.system != "Linux":
            return None
            
        try:
            with open("/etc/os-release") as f:
                content = f.read().lower()
                if "arch" in content or "manjaro" in content:
                    return "arch"
                elif "ubuntu" in content or "debian" in content:
                    return "debian"
                elif "fedora" in content or "rhel" in content or "centos" in content:
                    return "fedora"
                elif "opensuse" in content:
                    return "opensuse"
        except:
            pass
        return None
    
    def print_header(self, text):
        """Print colored header"""
        print(f"\n{'='*60}")
        print(f"  {text}")
        print(f"{'='*60}\n")
    
    def print_success(self, text):
        """Print success message"""
        print(f"✓ {text}")
    
    def print_error(self, text):
        """Print error message"""
        print(f"✗ {text}")
        sys.exit(1)
    
    def run_command(self, cmd, description, check=True, sudo=False):
        """Run command with description"""
        print(f"  → {description}")
        
        if sudo and os.geteuid() != 0:
            cmd = ["sudo"] + cmd
        
        try:
            result = subprocess.run(cmd, check=check, capture_output=True, text=True)
            if result.returncode == 0 or not check:
                self.print_success(description)
                return True
            else:
                print(f"    Output: {result.stderr}")
                return False
        except FileNotFoundError:
            self.print_error(f"Command not found: {cmd[0]}")
        except Exception as e:
            if check:
                self.print_error(f"Error: {str(e)}")
            return False
    
    def install_tkinter(self):
        """Install tkinter based on system"""
        self.print_header(f"Installing Tkinter ({self.system}/{self.distro})")
        
        if self.system == "Linux":
            if self.distro == "arch":
                self.run_command(["pacman", "-S", "--noconfirm", "tk"], 
                               "Installing tk (pacman)", sudo=True)
            elif self.distro == "debian":
                self.run_command(["apt-get", "update"], "Updating package lists", sudo=True)
                self.run_command(["apt-get", "install", "-y", "python3-tk"], 
                               "Installing python3-tk (apt)", sudo=True)
            elif self.distro == "fedora":
                self.run_command(["dnf", "install", "-y", "python3-tkinter"], 
                               "Installing python3-tkinter (dnf)", sudo=True)
            elif self.distro == "opensuse":
                self.run_command(["zypper", "install", "-y", "python3-tkinter"], 
                               "Installing python3-tkinter (zypper)", sudo=True)
            else:
                print("  ⚠ Unknown Linux distribution. Please install tkinter manually:")
                print("    - Arch: sudo pacman -S tk")
                print("    - Debian/Ubuntu: sudo apt-get install python3-tk")
                print("    - Fedora: sudo dnf install python3-tkinter")
                print("    - openSUSE: sudo zypper install python3-tkinter")
        
        elif self.system == "Darwin":  # macOS
            if self.run_command(["brew", "--version"], "Checking for Homebrew", check=False):
                self.run_command(["brew", "install", "python-tk"], 
                               "Installing python-tk (Homebrew)")
            else:
                print("  ⚠ Homebrew not found. Install from https://brew.sh")
                print("    Then run: brew install python-tk")
        
        elif self.system == "Windows":
            print("  ⚠ On Windows, tkinter is usually included with Python")
            print("    If missing, reinstall Python and check 'tcl/tk and IDLE' option")
        
        else:
            self.print_error(f"Unsupported system: {self.system}")
    
    def create_venv(self):
        """Create virtual environment"""
        self.print_header("Setting up Virtual Environment")
        
        if os.path.exists(self.venv_path):
            self.print_success(f"Virtual environment already exists at {self.venv_path}")
            return
        
        self.run_command([sys.executable, "-m", "venv", self.venv_path], 
                        f"Creating virtual environment at {self.venv_path}")
    
    def activate_venv(self):
        """Set up virtual environment paths for subsequent operations"""
        self.print_header("Setting up Virtual Environment")
        
        if self.system == "Windows":
            self.venv_python = os.path.join(self.venv_path, "Scripts", "python.exe")
            self.venv_pip = os.path.join(self.venv_path, "Scripts", "pip.exe")
        else:
            self.venv_python = os.path.join(self.venv_path, "bin", "python")
            self.venv_pip = os.path.join(self.venv_path, "bin", "pip")
        
        # Verify venv python exists
        if os.path.exists(self.venv_python):
            self.print_success(f"Using Python: {self.venv_python}")
        else:
            self.print_error(f"Virtual environment Python not found: {self.venv_python}")
    
    def install_requirements(self):
        """Install Python dependencies"""
        self.print_header("Installing Python Dependencies")
        
        req_file = os.path.join(self.script_dir, "requirements.txt")
        
        if not os.path.exists(req_file):
            self.print_error(f"requirements.txt not found at {req_file}")
        
        self.run_command([self.venv_pip, "install", "--upgrade", "pip"], 
                        "Upgrading pip")
        self.run_command([self.venv_pip, "install", "-r", req_file], 
                        "Installing dependencies from requirements.txt")
    
    def print_completion(self):
        """Print completion message and offer to run GUI"""
        self.print_header("Setup Complete!")
        
        if self.system == "Windows":
            python_exe = os.path.join(self.venv_path, "Scripts", "python.exe")
        else:
            python_exe = os.path.join(self.venv_path, "bin", "python")
        
        print("Setup completed successfully! 🎉")
        print(f"Virtual environment created at: {self.venv_path}")
        print(f"Python executable: {python_exe}")
        print()
        
        # Ask user what to do next
        while True:
            print("What would you like to do next?")
            print("1) Run the GUI now")
            print("2) Finish setup (exit)")
            print()
            
            try:
                choice = input("Enter your choice (1 or 2): ").strip()
                
                if choice == "1":
                    print("\nLaunching GUI...")
                    self.run_gui()
                    break
                elif choice == "2":
                    print("\nSetup complete! To run the GUI later:")
                    print(f"  {python_exe} gui.py")
                    print(f"Or from the project directory: python gui.py (venv activated)")
                    break
                else:
                    print("Please enter 1 or 2.")
                    
            except KeyboardInterrupt:
                print("\n\nSetup complete!")
                break
            except EOFError:
                print("\n\nSetup complete!")
                break
    
    def run_gui(self):
        """Run the GUI using the virtual environment"""
        try:
            if self.system == "Windows":
                python_exe = os.path.join(self.venv_path, "Scripts", "python.exe")
                cmd = [python_exe, "gui.py"]
            else:
                python_exe = os.path.join(self.venv_path, "bin", "python")
                cmd = [python_exe, "gui.py"]
            
            print(f"Running: {' '.join(cmd)}")
            subprocess.run(cmd, cwd=self.script_dir)
            
        except Exception as e:
            print(f"Error launching GUI: {str(e)}")
            print("You can run it manually with:")
            if self.system == "Windows":
                print(f"  {os.path.join(self.venv_path, 'Scripts', 'python.exe')} gui.py")
            else:
                print(f"  {os.path.join(self.venv_path, 'bin', 'python')} gui.py")
    
    def run(self):
        """Run full setup"""
        print(f"\nFckTikTokAI Setup Script")
        print(f"System: {self.system}")
        if self.distro:
            print(f"Distro: {self.distro}")
        
        self.install_tkinter()
        self.create_venv()
        self.activate_venv()
        self.install_requirements()
        self.print_completion()

if __name__ == "__main__":
    try:
        setup = Setup()
        setup.run()
    except KeyboardInterrupt:
        print("\n\nSetup cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Unexpected error: {str(e)}")
        sys.exit(1)

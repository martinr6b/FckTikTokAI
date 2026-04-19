import tkinter as tk
from tkinter import scrolledtext, messagebox
import subprocess
import threading
import os
import sys

class AutomationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("FckTikTokAI - Automation GUI")
        self.root.geometry("800x600")
        
        # Get the directory where this script is located
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        
        self.process = None
        self.is_running = False
        
        # Top frame for buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10, padx=10, fill=tk.X)
        
        self.run_main_btn = tk.Button(
            button_frame, 
            text="Run Main", 
            command=self.run_main,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 10, "bold"),
            width=15
        )
        self.run_main_btn.pack(side=tk.LEFT, padx=5)
        
        self.run_finder_btn = tk.Button(
            button_frame,
            text="Run Tap Finder",
            command=self.run_tap_finder,
            bg="#2196F3",
            fg="white",
            font=("Arial", 10, "bold"),
            width=15
        )
        self.run_finder_btn.pack(side=tk.LEFT, padx=5)
        
        self.stop_btn = tk.Button(
            button_frame,
            text="Stop Script",
            command=self.stop_script,
            bg="#f44336",
            fg="white",
            font=("Arial", 10, "bold"),
            width=15,
            state=tk.DISABLED
        )
        self.stop_btn.pack(side=tk.LEFT, padx=5)
        
        # Terminal output area
        terminal_label = tk.Label(root, text="Output Terminal:", font=("Arial", 10, "bold"))
        terminal_label.pack(anchor=tk.W, padx=10, pady=(10, 0))
        
        self.terminal = scrolledtext.ScrolledText(
            root,
            height=20,
            width=90,
            bg="#1e1e1e",
            fg="#00ff00",
            font=("Courier New", 9),
            insertbackground="#00ff00"
        )
        self.terminal.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready")
        status_bar = tk.Label(
            root,
            textvariable=self.status_var,
            bg="#f0f0f0",
            relief=tk.SUNKEN,
            anchor=tk.W,
            padx=10
        )
        status_bar.pack(fill=tk.X, side=tk.BOTTOM)
    
    def log(self, message):
        """Add message to terminal output"""
        self.terminal.insert(tk.END, message + "\n")
        self.terminal.see(tk.END)
        self.root.update()
    
    def run_script(self, script_name):
        """Run a script and capture its output"""
        if self.is_running:
            messagebox.showwarning("Already Running", "A script is already running!")
            return
        
        self.is_running = True
        self.run_main_btn.config(state=tk.DISABLED)
        self.run_finder_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.terminal.delete(1.0, tk.END)
        
        self.log(f"Starting {script_name}...\n")
        self.status_var.set(f"Running: {script_name}")
        
        # Run script in a separate thread
        thread = threading.Thread(target=self._execute_script, args=(script_name,))
        thread.daemon = True
        thread.start()
    
    def _execute_script(self, script_name):
        """Execute script and capture output"""
        try:
            # Use the virtual environment Python
            python_exe = os.path.join(self.script_dir, ".venv/bin/python")
            
            if script_name == "main":
                cmd = [python_exe, "main.py"]
            elif script_name == "finder":
                cmd = [python_exe, "WhereDoITap.py"]
            
            self.process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                cwd=self.script_dir
            )
            
            # Read output line by line
            for line in self.process.stdout:
                if self.is_running:
                    self.log(line.rstrip())
            
            # Wait for process to finish
            self.process.wait()
            
            if self.is_running:
                self.log(f"\n{script_name} finished with exit code {self.process.returncode}")
                self.status_var.set(f"Finished: {script_name} (Exit code: {self.process.returncode})")
        
        except Exception as e:
            self.log(f"Error: {str(e)}")
            self.status_var.set("Error")
        
        finally:
            self.is_running = False
            self.process = None
            self.run_main_btn.config(state=tk.NORMAL)
            self.run_finder_btn.config(state=tk.NORMAL)
            self.stop_btn.config(state=tk.DISABLED)
    
    def run_main(self):
        """Run main.py"""
        self.run_script("main")
    
    def run_tap_finder(self):
        """Run WhereDoITap.py"""
        self.run_script("finder")
    
    def stop_script(self):
        """Stop the running script"""
        if self.process and self.is_running:
            self.log("\nStopping script...")
            self.process.terminate()
            
            try:
                self.process.wait(timeout=3)
            except subprocess.TimeoutExpired:
                self.log("Force killing process...")
                self.process.kill()
            
            self.is_running = False
            self.status_var.set("Stopped by user")
            self.run_main_btn.config(state=tk.NORMAL)
            self.run_finder_btn.config(state=tk.NORMAL)
            self.stop_btn.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = AutomationGUI(root)
    root.mainloop()

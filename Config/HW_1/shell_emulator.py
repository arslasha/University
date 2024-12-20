import os
import zipfile
import tkinter as tk
from tkinter import scrolledtext
import toml
import csv
from datetime import datetime
import calendar

class ShellEmulator:
    def __init__(self, master, config_file):
        self.master = master
        self.master.title("Shell Emulator")
        self.config = self.load_config(config_file)
        self.vfs_path = self.config["settings"]["vfs_path"]
        self.log_path = self.config["settings"]["log_path"]
        self.start_script = self.config["settings"]["start_script"]

        self.cwd = "/"  # Current working directory
        self.vfs = None  # Handle for the zip archive

        self.setup_vfs()

        self.create_gui()
        self.run_start_script()

    def load_config(self, config_file):
        with open(config_file, "r") as f:
            return toml.load(f)

    def setup_vfs(self):
        """Open the virtual filesystem from the zip archive."""
        self.vfs = zipfile.ZipFile(self.vfs_path, 'r')

    def create_gui(self):
        """Create the GUI layout."""
        self.text = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, height=20, width=80)
        self.text.pack(pady=10)

        self.entry = tk.Entry(self.master, width=80)
        self.entry.pack(pady=5)
        self.entry.bind("<Return>", self.execute_command)  # Прямая привязка
        self.entry.focus_set()  # Установка фокуса на поле ввода

        self.master.protocol("WM_DELETE_WINDOW", self.cleanup)

    def run_start_script(self):
        """Execute commands from the start script."""
        if os.path.exists(self.start_script):
            with open(self.start_script, "r") as f:
                for line in f:
                    self.process_command(line.strip())

    def execute_command(self, event=None):
        print("execute_command вызван")  # Отладочный вывод
        command = self.entry.get().strip()
        print(f"Получена команда: {command}")  # Проверка ввода
        if command:
            self.process_command(command)
            self.entry.delete(0, tk.END)

    def process_command(self, command):
        """Process shell commands."""
        if not command.strip():
            return

        self.log_command(command)
        cmd = command.split()

        if not cmd:
            return

        command_name = cmd[0]
        args = cmd[1:]

        try:
            if command_name == "ls":
                self.command_ls()
            elif command_name == "cd":
                self.command_cd(args[0] if args else None)
            elif command_name == "exit":
                self.cleanup()
            elif command_name == "wc":
                self.command_wc(args[0] if args else None)
            elif command_name == "cal":
                self.command_cal()
            elif command_name == "rmdir":
                self.command_rmdir(args[0] if args else None)
            else:
                self.append_output(f"Unknown command: {command_name}")
        except Exception as e:
            self.append_output(f"Error while executing command: {command_name}\n{str(e)}")

    def command_ls(self):
        """List directory contents."""
        try:
            if self.cwd == "/":
                path = ""  # Root of the zip archive
            else:
                path = self.cwd.lstrip("/")

            items = [name[len(path):].strip("/") for name in self.vfs.namelist() if name.startswith(path)]
            unique_items = {item.split("/")[0] for item in items if item}
            self.append_output("\n".join(sorted(unique_items)))
        except Exception as e:
            self.append_output(f"Error: {e}")

    def command_cd(self, path):
        """Change directory."""
        if not path:
            self.append_output("Usage: cd <directory>")
            return

        new_path = os.path.normpath(os.path.join(self.cwd, path))
        if new_path == "/":
            self.cwd = "/"
            self.append_output("Changed to root directory")
            return

        test_path = new_path.lstrip("/") + "/"
        if any(name.startswith(test_path) for name in self.vfs.namelist()):
            self.cwd = new_path
            self.append_output(f"Changed directory to {self.cwd}")
        else:
            self.append_output(f"Error: Directory not found: {path}")

    def command_wc(self, path):
        """Word count."""
        if not path:
            self.append_output("Usage: wc <file>")
            return

        abs_path = os.path.normpath(os.path.join(self.cwd.lstrip("/"), path))
        if abs_path not in self.vfs.namelist():
            self.append_output(f"Error: File not found: {path}")
            return

        try:
            with self.vfs.open(abs_path) as f:
                contents = f.read().decode("utf-8")
                lines = contents.count("\n")
                words = len(contents.split())
                chars = len(contents)
                self.append_output(f"{lines} {words} {chars} {path}")
        except Exception as e:
            self.append_output(f"Error: {e}")

    def command_cal(self):
        """Display the current month's calendar."""
        try:
            now = datetime.now()
            cal = calendar.TextCalendar()
            output = cal.formatmonth(now.year, now.month)
            self.append_output(output)
        except Exception as e:
            self.append_output(f"Error: {e}")

    def command_rmdir(self, path):
        """Remove a directory."""
        if not path:
            self.append_output("Usage: rmdir <directory>")
            return

        abs_path = os.path.normpath(os.path.join(self.cwd.lstrip("/"), path)) + "/"
        if not any(name.startswith(abs_path) for name in self.vfs.namelist()):
            self.append_output(f"Error: Directory not found: {path}")
            return

        # Check if the directory is empty
        items_in_dir = [name for name in self.vfs.namelist() if name.startswith(abs_path)]
        if len(items_in_dir) > 1:  # More than just the directory itself
            self.append_output(f"Error: Directory not empty: {path}")
            return

        self.append_output(f"Removed directory: {path}")
        # Note: Actual removal requires modifying the ZIP, which Python's `zipfile` doesn't support in-place.

    def log_command(self, command):
        """Log commands to CSV."""
        try:
            with open(self.log_path, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([datetime.now(), command, self.cwd])
        except Exception as e:
            self.append_output(f"Error logging command: {e}")

    def append_output(self, output):
        """Display command output in the GUI."""
        self.text.insert(tk.END, output + "\n")
        self.text.see(tk.END)

    def cleanup(self):
        """Clean up and exit."""
        if self.vfs:
            self.vfs.close()
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ShellEmulator(root, "config.toml")
    root.mainloop()

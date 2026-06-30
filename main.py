#!/usr/bin/env python3
import sys
import types
import os

def load_module(name, path):
    """
    Dynamically load a Python module from a file without extension.
    """
    # Try without extension first
    if not os.path.isfile(path):
        # If not found, try with .py
        path_py = path + '.py'
        if os.path.isfile(path_py):
            path = path_py
        else:
            raise FileNotFoundError(f"File '{path}' or '{path_py}' not found.")
    
    with open(path, 'r', encoding='utf-8') as f:
        code = f.read()
    
    module = types.ModuleType(name)
    module.__file__ = path
    sys.modules[name] = module
    exec(code, module.__dict__)
    return module

# ==================== LOAD ALL MODULES IN ORDER ====================
# Important: order matters because of import dependencies
load_module('colors', 'colors')
load_module('config', 'config')
load_module('templates', 'templates')
load_module('logger', 'logger')
load_module('handler', 'handler')
load_module('server', 'server')
load_module('tunnel', 'tunnel')
load_module('utils', 'utils')
load_module('menu', 'menu')

# ==================== IMPORT INTO CURRENT NAMESPACE ====================
from menu import show_menu, auto_start
from utils import show_banner, clear_screen, view_logs, kill_previous_servers
from colors import colored, Colors

# ==================== MAIN ====================
def main():
    try:
        if sys.version_info < (3, 6):
            print(colored("Please use Python 3.6 or higher", Colors.RED))
            sys.exit(1)
        show_banner()
        while True:
            show_menu()
            choice = input(colored("Enter your choice [1-3]: ", Colors.BLUE))
            if choice == '1':
                auto_start()
            elif choice == '2':
                view_logs()
            elif choice == '3':
                print(colored("\nExiting... Bye Hacker! 👋\n", Colors.RED))
                kill_previous_servers()
                sys.exit(0)
            else:
                print(colored("\nInvalid choice! Please try again.\n", Colors.RED))
                import time
                time.sleep(1)
    except KeyboardInterrupt:
        print(colored("\n\nExiting... Bye Hacker! 👋\n", Colors.RED))
        kill_previous_servers()
        sys.exit(0)

if __name__ == "__main__":
    main()
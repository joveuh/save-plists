import shutil, os

"""
This program will save your current Dock settings
under ~/plist/dock folder. After Mac update or 
restart if you find the Dock has changed, you can
run restoreall.py script to restore Dock settings
from ~/plist/dock folder


To run from terminal, issue:
                            python save_dock.py

if using python3, issue:
                            python3 save_dock.py

"""


def run():
    # Get user's HOME
    HOME = os.getenv("HOME")

    source = HOME + "/Library/Preferences/com.apple.dock.plist"
    target = HOME + "/plists/dock/com.apple.dock.plist"

    shutil.copy2(source, target)


if __name__ == "__main__":
    run()

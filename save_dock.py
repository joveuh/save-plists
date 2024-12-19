import shutil, restoreall, os, time

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

    source = os.path.join(HOME, "Library", "Preferences", "com.apple.dock.plist")
    target = os.path.join(HOME, "plists", "dock", "com.apple.dock.plist")
    epochtime = int(time.time())
    backup = os.path.join(
        HOME, "plists", "backups", "dock", f"{epochtime}", "com.apple.dock.plist"
    )
    target_dir = os.path.dirname(target)
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    if not os.path.exists(backup):
        os.makedirs(backup)
    shutil.copy2(target, backup)
    shutil.copy2(source, target)


if __name__ == "__main__":
    run()

import shutil, os, time

"""
This program will save your current Dock settings
under ~/plist/finder folder. After Mac update or 
restart if you find the Dock has changed, you can
run restoreall.py script to restore Dock settings
from ~/plist/finder folder


To run from terminal, issue:
                            python save_finder.py

if using python3, issue:
                            python3 save_finder.py

"""


def run():
    # Get user's HOME
    HOME = os.getenv("HOME")

    source = os.path.join(HOME, "Library", "Preferences", "com.apple.finder.plist")
    target = os.path.join(HOME, "plists", "finder", "com.apple.finder.plist")
    epochtime = int(time.time())
    backup = os.path.join(
        HOME, "plists", "backups", "finder", f"{epochtime}", "com.apple.finder.plist"
    )
    os.makedirs(backup)
    shutil.copy2(target, backup)
    shutil.copy2(source, target)


if __name__ == "__main__":
    run()

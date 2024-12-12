import restoreall, os, time

"""
This program will save you current Stickies (including settings)
under ~/plist/stickies folder. 

Instructions:

Please ensure once you have decided what settings need to be saved,
you Quit the Stickies app from the File Menu. Then restart
Stickies to ensure what you see on the screen are the desired settings
you wish to save.

Settings include all current Stickies widget windows,
their colors, their contents, and their positions on screens.
Since we copy all data, even if you have stickies scattered on multiple screens, 
this should save that setting, so upon restore each stickies widget will be 
restored to its corresponding screen.

Then run this script.
To run from terminal, issue:
                            python save_stickies.py

if using python3, issue:
                            python3 save_stickies.py

When you notice Stickies settings have changed, you can
run the restoreall.py script to restore its settings back from the
 ~/plist/countdown folder
"""


def run():

    # Get user's HOME
    HOME = os.getenv("HOME")

    source = HOME + "/Library/Containers/com.apple.Stickies/Data"
    target = HOME + "/plists/stickies/Data"
    epochtime = time.time()
    backup = HOME + f"plists/backups/stickies_{epochtime}/Data"
    restoreall.copy(target,backup)
    restoreall.copy(source, target)


if __name__ == "__main__":
    run()

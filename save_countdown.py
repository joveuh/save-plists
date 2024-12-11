import restoreall, os

"""
This program will save you current CountDown Timer Plus settings
under ~/plist/countdown folder. Settings inclue, all current timer widgets,
their colors, their countdowns, and their positions on screens.
Since we copy all data, even if you have widgets on multiple screens, 
this should save that setting, so upon restore each countdown widget will be 
restored to its corresponding screen.

Instructions:

Please ensure once you have decided what settings need to be saved that
you Quit the CountDown Timer Plus app from the File Menu. Then restart 
it to ensure what you see on the screen are the desired settings
you wish to save.

Then run this script.
To run from terminal, issue:
                            python save_countdown.py

if using python3, issue:
                            python3 save_countdown.py

When you notice  CountDown Timer Plus settings have changed, you can
run the restoreall.py script to restore its settings back from the
 ~/plist/countdown folder
"""


def run():
    # Get user's HOME
    HOME = os.getenv("HOME")

    source = HOME + "/Library/Containers/com.arvistech.countdowntimerplus/Data"
    target = HOME + "/plists/countdown/Data"
    restoreall.copy(source, target)


if __name__ == "__main__":
    run()

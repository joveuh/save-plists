import sys, save_stickies, save_dock, save_countdown, save_finder, restoreall, time


def run(
    countdown: bool = True,
    stickies: bool = True,
    dock: bool = True,
    finder: bool = True,
):

    if countdown:
        restoreall.terminate_countdown()
        time.sleep(0.6)
        save_countdown.run()
        time.sleep(0.2)
        restoreall.restart_countdown()
    if stickies:
        restoreall.terminate_stickies()
        time.sleep(0.6)
        save_stickies.run()
        time.sleep(0.2)
        restoreall.restart_stickies()
    if dock:
        time.sleep(1)
        save_dock.run()
        time.sleep(0.2)
        restoreall.restart_dock()
    if finder:
        time.sleep(1)
        save_finder.run()
        time.sleep(0.2)
        restoreall.restart_finder()


if __name__ == "__main__":
    args = [arg.lower() for arg in sys.argv[1:]]
    if len(args) == 0:
        run()
        exit
    else:
        countdown = "countdown" in args
        stickies = "stickies" in args
        dock = "dock" in args
        finder = "finder" in args
        run(countdown, stickies, dock, finder)

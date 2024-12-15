import sys, save_stickies, save_dock, save_countdown, restoreall, time


def run(countdown: bool = True, stickies: bool = True, dock: bool = True):
    scripts = [save_countdown, save_dock, save_stickies]
    if countdown:
        restoreall.terminate_countdown()
        time.sleep(0.6)
        save_countdown.run()
        time.sleep(0.2)
        restoreall.restart_countdown()
    if stickies:
        restoreall.terminate_countdown()
        time.sleep(0.6)
        save_stickies.run()
        time.sleep(0.2)
    if dock:
        restoreall.restart_dock()
        time.sleep(0.6)
        save_dock.run()
        time.sleep(0.2)
        restoreall.restart_dock()


if __name__ == "__main__":
    args = [arg.lower() for arg in sys.argv[1:]]
    if len(args) == 0:
        run(countdown=True, stickies=True, dock=True)
        exit
    else:
        countdown = "countdown" in args
        stickies = "stickies" in args
        dock = "dock" in args
        run(countdown, stickies, dock)

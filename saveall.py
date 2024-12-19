import sys, os, restoreall, time, constants


def save_settings(app_name: str):
    HOME = os.getenv("HOME")
    target_path = constants.get_target_path(app_name).split("/")
    source_path = os.path.join(HOME, "Library", target_path, f"com.apple.{app_name}.plist")
    # source_path = os.path.join(

def run(
    countdown: bool = True,
    stickies: bool = True,
    dock: bool = True,
    finder: bool = True,
):
    args = locals()
    for arg in args:
        if args[arg]:
            restoreall.terminate(arg)
            time.sleep(0.1)
            save_settings(arg)
            time.sleep(0.125)
            restoreall.restart(arg)


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

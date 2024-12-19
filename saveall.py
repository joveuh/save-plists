import sys, os, restoreall, time, constants, shutil


def save_settings(app_name: str):
    HOME = os.getenv("HOME")
    single_flag = False
    source_path = constants.get_target_path(app_name).split("/")
    match source_path[1]:
        case "Containers":
            target_path = os.path.join(HOME, "plists", app_name, "Data")
        case "Preferences":
            single_flag = True
            target_path = os.path.join(HOME, "plists", app_name, source_path[2])
        case _:
            raise Exception("Unknown path for the application. Please check constants.")
    epochtime = int(time.time())
    backup = os.path.join(
        HOME, "plists", "backup", app_name, f"{epochtime}", source_path[2]
    )
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    if not os.path.exists(backup):
        os.makedirs(backup)
    if os.path.exists(target_path) and os.path.getsize(target_path) > 0:
        (
            shutil.copy2(target_path, backup)
            if single_flag
            else restoreall.copy(target_path, backup)
        )
    (
        shutil.copy2(source_path, target_path)
        if single_flag
        else restoreall.copy(source_path, target_path)
    )


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

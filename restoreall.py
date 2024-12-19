import os, sys, shutil, subprocess, time
import constants

"""
This script restores saved settings for 
Dock, Stickies, and CountdownTimer Plus application.
The restore objects should previously have been saved by the user
under user's USERDIR -> ~/plists/

    Ensure you quit the applications whose settings you will be restoring
    prior to running this script (see __name__ == "__main__" below). 
    This script will attempt to Quit the applications before performing 
    restore operations anyways.

To run from terminal, issue:
                            python runthis.py

if using python3, issue:
                            python3 runthis.py

"""


def copy(source_dir: str, target_dir: str):
    print(f"Copying files from {source_dir} to {target_dir}...")
    """
    Recursivley copy files and folders from source_dir to
    target_dir. Skip any symbolic links.

    Args:
        source_dir (str): The source directory to copy
        target_dir (str): The target directory to store settings under

    """
    # Ensure source and target directories exist
    if not os.path.isdir(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return
    if not os.path.isdir(target_dir):
        os.makedirs(target_dir)  # Create target directory if it doesn't exist

    # Walk through the source directory
    for root, dirs, files in os.walk(source_dir):
        # Calculate target path
        relative_path = os.path.relpath(root, source_dir)
        target_path = os.path.join(target_dir, relative_path)

        # Ensure the target directory structure exists
        os.makedirs(target_path, exist_ok=True)

        # Copy files
        for file_name in files:
            source_file = os.path.join(root, file_name)
            target_file = os.path.join(target_path, file_name)

            # Skip if the file is a symbolic link (alias)
            if os.path.islink(source_file):
                print(f"Skipping alias (symlink): {source_file}")
                continue

            shutil.copy2(source_file, target_file)  # Copy file with metadata
            print(f"Copied file: {source_file} -> {target_file}")

        # Copy directories (skip symbolic links)
        dirs[:] = [d for d in dirs if not os.path.islink(os.path.join(root, d))]

    print("All files and folders have been copied, excluding aliases.")


def restart(app_name: str):
    """
    Issue command to restart {app_name} application after restoring settings.
    """
    try:
        subprocess.run(["open", "-a", f"{app_name}"], check=True)
        print(f"{app_name} have been launched.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while trying to restart {app_name}: {e}")
    except FileNotFoundError:
        print("The `open` command was not found. Make sure you're on macOS.")


def terminate(app_name: str):
    """
    Issue command to terminate the {app_name} application before restoring settings.
    """
    try:
        subprocess.run(["killall", f"{app_name}"], check=True)
        print(f"{app_name} has been terminated.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while trying to terminate {app_name}: {e}")
    except FileNotFoundError:
        print("The `killall` command was not found. Make sure you're on macOS.")


def run(
    countdown: bool = True,
    stickies: bool = True,
    dock: bool = True,
    finder: bool = True,
):
    args = locals()
    single_flag = False
    HOME = os.getenv("HOME")
    PLISTS_PATH = os.path.join(HOME, "plists")
    for arg in args:
        if args[arg]:
            source_path = os.path.join(PLISTS_PATH, f"{arg}")
            target_path = os.path.join(HOME, constants.get_target_path(arg).lstrip("/"))

            print(f"Restoring {arg} settings...")
            terminate(constants.get_full_name(arg))
            time.sleep(0.1)
            if target_path.endswith("/Data"):
                single_flag = True
                source_path = os.path.join(source_path, "Data")

            (
                copy(source_path, os.path.dirname(target_path))
                if single_flag
                else copy(source_path, target_path)
            )
            time.sleep(0.125)
            restart(constants.get_full_name(arg))


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

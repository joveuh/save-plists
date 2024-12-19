import os, sys, shutil, subprocess, time

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


def restart_dock():
    """
    Issue  command to restart Dock for changes to take effect.
    """
    try:
        subprocess.run(["killall", "Dock"], check=True)
        print("Dock has been restarted.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while trying to restart the Dock: {e}")
    except FileNotFoundError:
        print("The `killall` command was not found. Make sure you're on macOS.")


def restart_finder():
    """
    Issue  command to restart Finder for changes to take effect.
    """
    try:
        subprocess.run(["killall", "Finder"], check=True)
        print("Finder has been restarted.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while trying to restart the Finder: {e}")
    except FileNotFoundError:
        print("The `killall` command was not found. Make sure you're on macOS.")


def terminate_stickies():
    """
    Issue command to terminate Stickies before restoring settings.
    """
    try:
        subprocess.run(["killall", "Stickies"], check=True)
        print("Stickies has been terminated.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while trying to terminate Stickies: {e}")
    except FileNotFoundError:
        print("The `killall` command was not found. Make sure you're on macOS.")


def restart_stickies():
    """
    Issue command to restart Stickies after restoring settings.
    """
    try:
        subprocess.run(["open", "-a", "Stickies"], check=True)
        print("Stickies have been launched.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while trying to restart Stickies: {e}")
    except FileNotFoundError:
        print("The `open` command was not found. Make sure you're on macOS.")


def terminate_countdown():
    """
    Issue command to terminate CountDown Timer Plus before restoring settings.
    """
    try:
        subprocess.run(["killall", "CountDown Timer Plus"], check=True)
        print("CountDown Timer Plus has been terminated.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while trying to terminate CountDown Timer Plus: {e}")
    except FileNotFoundError:
        print("The `killall` command was not found. Make sure you're on macOS.")


def restart_countdown():
    """
    Issue command to restart CountDown Timer Plus after restoring settings.
    """
    try:
        subprocess.run(["open", "-a", "Countdown Timer Plus"], check=True)
        print("CountDown Timer Plus has been launched.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while trying to restart CountDown Timer Plus: {e}")
    except FileNotFoundError:
        print("The `open` command was not found. Make sure you're on macOS.")


def run(countdown: bool = True, stickies: bool = True, dock: bool = True):

    HOME = os.getenv("HOME")

    if countdown:
        # countdown start
        terminate_countdown()
        time.sleep(0.25)
        source_path = HOME + "/plists/countdown/Data"
        target_path = HOME + "/Library/Containers/com.arvistech.countdowntimerplus/Data"
        copy(source_path, target_path)
        time.sleep(0.25)
        restart_countdown()
        # countdown end

    if stickies:
        # stickies start
        terminate_stickies()
        time.sleep(0.25)
        source = HOME + "/plists/stickies/Data"
        target = HOME + "/Library/Containers/com.apple.Stickies/Data"
        copy(source, target)
        time.sleep(0.25)
        restart_stickies()
        # stickies end

    if dock:
        # dock start
        source = HOME + "/plists/dock"
        target = HOME + "/Library/Preferences"
        copy(source, target)
        time.sleep(0.25)
        restart_dock()
        # dock end

    if finder:
        # dock start
        source = HOME + "/plists/finder"
        target = HOME + "/Library/Preferences"
        copy(source, target)
        time.sleep(0.25)
        restart_dock()
        # dock end


if __name__ == "__main__":
    args = [arg.lower() for arg in sys.argv[1:]]
    if len(args) == 0:
        run(countdown=True, stickies=True, dock=True, finder=True)
        exit
    else:
        countdown = "countdown" in args
        stickies = "stickies" in args
        dock = "dock" in args
        finder = "finder" in args
        run(countdown, stickies, dock, finder)

STICKIES = "/Library/Containers/com.apple.Stickies/Data"
DOCK = "/Library/Preferences"
FINDER = "/Library/Preferences"
COUNTDOWNTIMERPLUS = "/Library/Containers/com.arvistech.countdowntimerplus/Data"


def get_target_path(app_name: str):
    return str.upper(app_name)

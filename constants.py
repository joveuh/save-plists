APP_NAMES = {
    "STICKIES": "/Library/Containers/com.apple.Stickies/Data",
    "COUNTDOWN_TIMER_PLUS": "/Library/Containers/com.arvistech.countdowntimerplus/Data",
    "DOCK": "/Library/Preferences/com.apple.dock.plist",
    "FINDER": "/Library/Preferences/com.apple.finder.plist",
}


def match_app_name(app_name: str):
    app_name = str.upper(app_name)
    for key in APP_NAMES.keys():
        if app_name in key:
            return APP_NAMES[key]


def get_target_path(app_name: str):
    return match_app_name(app_name)


def get_full_name(app_name: str):
    app_name = str.upper(app_name)
    for key in APP_NAMES.keys():
        splitkey = key.split("_")
        if app_name in splitkey:
            return " ".join(word.capitalize() for word in splitkey)

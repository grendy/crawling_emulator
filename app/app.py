# import subprocess
#
# subprocess.call("/opt/google/chrome/google-chrome --profile-directory=Default --app-id=menkifleemblimdogmoihpfopnplikde")

# import os
# os.system("/opt/google/chrome/google-chrome --profile-directory=Default --app-id=menkifleemblimdogmoihpfopnplikde")

from Xlib import display
def mousepos():
    """mousepos() --> (x, y) get the mouse coordinates on the screen (linux, Xlib)."""
    data = display.Display().screen().root.query_pointer()._data
    return data["root_x"], data["root_y"]
if __name__ == "__main__":
    print("The mouse position on the screen is {0}".format(mousepos()))

#(287, 223)
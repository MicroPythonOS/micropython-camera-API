# Include the board's default manifest.
include("$(PORT_DIR)/boards/manifest.py")
# Add custom driver
module("acamera.py")

import os

# Part of MicroPythonOS: its frozen manifest lives in the sibling
# lvgl_micropython tree and must not be overridden by this board manifest.
if os.path.isdir("../../lvgl_micropython"):
    include("../../lvgl_micropython/build/manifest.py")

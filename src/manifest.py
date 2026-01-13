# Include the board's default manifest.
include("$(PORT_DIR)/boards/manifest.py")
# Add custom driver
module("acamera.py")
include("/home/user/projects/MicroPythonOS/claude/MicroPythonOS/lvgl_micropython/build/manifest.py") # workaround to prevent micropython-camera-API from overriding the lvgl_micropython manifest...

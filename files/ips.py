#!/usr/bin/env python

import time
import signal
import subprocess


import scrollphathd
from scrollphathd.fonts import font5x7

print("""
Scroll pHAT HD: Hello World

Scrolls "Hello World" across the screen
in a 5x7 pixel large font.

Press Ctrl+C to exit!

""")

# Uncomment to rotate the text
scrollphathd.rotate(180)

# Set a more eye-friendly default brightness
scrollphathd.set_brightness(0.1)

msg = "Hello World! "
scrollphathd.write_string(msg, x=0, y=0, font=font5x7)

while True:
    hostname = subprocess.check_output(['/bin/hostname', '-I'])
    if msg != hostname:
        msg = hostname
        scrollphathd.clear()
        scrollphathd.write_string(" *IP: " + msg.strip(), x=0, y=0, font=font5x7)
    scrollphathd.show()
    scrollphathd.scroll()
    time.sleep(0.02)
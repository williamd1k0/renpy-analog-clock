# Copyright (c) 2018 William Tumeo
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


image clock bg:
    'clock/clock.png'
    align (0.5, 0.5)
image clock second:
    'clock/clock-s.png'
    align (0.5, 0.5)
image clock minute:
    'clock/clock-m.png'
    align (0.5, 0.5)
image clock hour:
    'clock/clock-h.png'
    align (0.5, 0.5)


label start:
    scene bg
    show screen clock
    "Analog Clock"
    return


init python:
    from datetime import datetime
    current_time = datetime.now()
    def update_clock():
        global current_time
        current_time = datetime.now()
        renpy.restart_interaction()

screen clock(position=(0.1, 0.15), scale=0.5):
    add 'clock bg':
        pos position
        zoom scale
    add 'clock hour':
        pos position
        zoom scale
        rotate current_time.hour*360/12
    add 'clock minute':
        pos position
        zoom scale
        rotate current_time.minute*360/60
    add 'clock second':
        pos position
        zoom scale
        rotate current_time.second*360/60
    timer 0.5 repeat True action Function(update_clock)

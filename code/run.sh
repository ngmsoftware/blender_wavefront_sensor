#!/bin/bash

/Applications/blender.app/Contents/MacOS/blender wavefront_sensor_2D_iteractive_2x.blend | grep --line-buffered "NIRPS" | ./pipingServer.py 

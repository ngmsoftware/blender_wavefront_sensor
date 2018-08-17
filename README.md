# Blender Wavefront Sensor

Small project aimed to demonstrate the principles of adaptive optics using blender and Matlab. In this project, we explore a new use for Blender as a tool to learn advanced concepts in optics. It is about using Blender to simulate a complete adaptive optics system that corrects for distortions in a non-uniform medium for light propagation like the atmosphere. The system is composed by a Blender file that contains an array of “detectors”, a light path and a deformable mirror between the light source and the detectors. The user can put any transparent object in the light path and the system will compute the wavefront deformation caused by this object in the detectors. The user can also ask for a set of “commands” to be applied to the deformable mirror. Those commands consists of micro deformations in the mirror surface. A Matlab script them compute such deformations and send back to the Blender file that moves the “actuators” of the mirror, compensating for the deformation of the object and thus correcting the distortion caused by the light passing through the object.

Demo vídeo: https://www.youtube.com/watch?v=HRdmDOKqeHg

## Software

- blender

- Matlab

- python

## Hardware

## Screen-shoots

![Screenshoot 1](/doc/homepage/blender.png?raw=true "Sample image 1")
![wavefront plots](/doc/homepage/plotsMatlab.png?raw=true "wavefront plots")
![optical devices](/doc/homepage/devices.png?raw=true "optical devices")
![pipe server interface](/doc/homepage/interface.png?raw=true "pipe server interface")
![blender panel](/doc/homepage/panel.png?raw=true "blender panel")

## Instructions

To compute wavefronts:

1 - Run blender using the shell script run.sh. This script will run blender with the pipe server in the middle using the grep to capture and filter the outputs.

2 - In blender, open the main blender file.

3 - Run the panel.py script

4 - Without any object in the light path, check "calibrate" and click compute. This will calibrate the array of detectors

5 - Place an object in the light path and click compute (uncheck the calibrate box)


To use the deformable mirror (you can skip the steps 1 to 3 if you executed it once)

1 - To generate the DM command matrix, click "Command Matrix". This will pich each actuator in the mirror and generate, for each one, a .m file with the deformations. It generates in the /tmp folder.

2 - Copy the generated .m files to code/AO/blender

3 - configure read_DM.m to compute the DM commands from "current" 

4 - run read_DM.m 

5 - in blender, click "Load mirror commands"



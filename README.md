# Grav_sim
This is a python script for simulating gravity using the newtonian formulae.

# How to use?
Edit the main.py script and change the values used when creating the planet1, planet2... objects.
The first argument is the mass(in Kg) of that stellar object, the second and third one are the acceleration(in m/s) on the x and y axis and the fourth and fifth are the position on the x and y axis(in Meters).

Then start the python script using "python.exe main.py". You can use -s for setting the time step of the simulation(in seconds), you can use -t to set the totaltime(in seconds) and -f for the filename of the exported .npz.

You can calculate the number of seconds this would correspond to in real life by doing totaltime/sigma. If I used sigma 1(for recalculating the position every second) and 50000 totaltime the simulation simulate 50000s.

# What to do after running the simulation?
After having generated a Gravdata.npz file which contains the positions of the planets(it can become quite big) you have to run the read.py script using "python.exe read.py" or whatever name you gave the *.npz file. If you do not provide a third argument it will default to "Gravdata.npz".

This will open a pygame window. You can change the camera position using the Arrow-Keys and Zoom-in and out using "A" and "Z".
When you are satisfied with the position you can press "W" and the the programm will draw the full path on the screen.
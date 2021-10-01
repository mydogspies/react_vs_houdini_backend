# REACT vs HOUDINI - backend

### A tiny case study of one way to use React as the web front to manipulate parameters in Houdini.

This repo is the Flask backend.

The goal is to try out one of many ways to use a web front end to directly manipulate parameters in SideFX Houdini. It is by no means the only way and the necessarily correct way. In this case I used vanilla react for the front end, Flask running on Houdini's own Hython (in this case we stick to the built-in Python 2.7.15 in Houdini version 18.5.596) and using the Hrpyc library within Houdini's python distro to make the connection.

** I will not maintain this particular repo so no point in filing code issues but feel free to comment on better ways of doing this particular hurdle. **

Here are some thoughts regarding the backend part;
* Hrpyc is a wrapper around the Rpyc lib specifically for Houdini. It only works from within Houdini's own python distro so I had to run Houdini's built-in Python 2.7.15 (Hython) as interpreter which lead to other issues. If anyone has managed to migrate Hrpyc to outside of Houdini, pretty please, let me know!
* Someone noted that this is specifically a Windows issue since on Linux one can run Houdini on a system python distro but on Win Houdini is locked to its own because of the fact that the python distro must be compiled with the same compiler as the python used for Houdini itself. Don't quote me on this and if I got that wrong then would be super if someone pointed me in the right direction to understand how that all works.
* The only reason I used Houdini with Python 2.7 and not 3.x is that that particular system I tested this on uses Renderman which in the moment of writing this is still only compatible with 2.7. It should all work exactly the same under 3.x.
* Hython does not come with certain mainstream libraries so I had to install pip directly into the distro, followed by flask-restful and flask-cors. For some reason Flask installed globally works but not the two other libs. Could just be an Intellij issue or a Win ditto.
* I made sure to add the following lines PYTHONPATH; *HOUDINI_PATH\python27\lib\site-packages*; *HOUDINI_PATH\python27\python2.7libs* where HOUDINI_PATH is the path to the particular Houdini install.

A great video on how to install PIP into Houdini itself can be found here; https://www.youtube.com/watch?v=cIEN50WuPoc
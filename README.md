# REACT vs HOUDINI - backend

### A tiny case study of one way to use React as the web front to manipulate parameters in Houdini.

This repo is the Flask backend.

The goal is to try out one of many ways to use a web front end to directly manipulate parameters in SideFX Houdini. It is by no means the only way and the necessarily correct way. In this case I used vanilla react for the front end, Flask running on Houdini's own Hython (in this case we stick to the built-in Python 2.7.15 in Houdini version 18.5.596 which uses Python 2.7.15 internally) and using the Hrpyc library within Houdini's python distro to make the connection.

** I will not maintain this particular repo so no point in filing code issues but feel free to comment on better ways of doing this particular hurdle. **

Here are some thoughts regarding the backend part;
* Hrpyc is a wrapper around the Rpyc lib specifically for Houdini. It only works from within Houdini's own python distro so I had to run Houdini's built-in Python 2.7 (Hython) as interpreter which lead to other issues. If anyone has managed to migrate Hrpyc to outside of Houdini (on WIN!), pretty please, let me know!
* Someone noted that this is specifically a Windows issue since on Linux one can run Houdini on a system python distro but on Win Houdini is locked to its own because of the fact that the python distro must be compiled with the same compiler as the python used for Houdini itself. Don't quote me on this and if I got that wrong then would be super if someone pointed me in the right direction to understand how that all works.
* The only reason I used Houdini with Python 2.7 and not 3.x is that that particular system I tested this on uses Renderman which at the moment of writing this is still only compatible with 2.7. It should all work exactly the same under 3.x.
* Hython does not come with certain mainstream libraries so I had to install pip directly into the distro, followed by flask-restful and flask-cors. For some reason Flask installed globally works but not the two other libs. Could just be an Intellij issue or a Win ditto.
* I made sure to add the following lines PYTHONPATH; *HOUDINI_PATH\python27\lib\site-packages*; *HOUDINI_PATH\python27\python2.7libs* where HOUDINI_PATH is the path to the particular Houdini install.
* Finally and importantly!; For Hrpyc to work the server MUST be started from within Houdini prior to connection being made. See the projectfiles part of this project for explanation!

A great video on how to install PIP into Houdini itself can be found here; https://www.youtube.com/watch?v=cIEN50WuPoc

HOW TO INSTALL AND RUN

So no guarantees and only tested on Windows and within Intellij;

These are the three repos you need;
* https://github.com/mydogspies/react_vs_houdini_backend
* https://github.com/mydogspies/react_vs_houdini_frontend
* https://github.com/mydogspies/react_vs_houdini_projectfiles

* Clone all *three* REACT vs HOUDINI repos to somewhere on your disc.
* **In the Flask BACKEND**; change the paths in the config.py to match with wherever you saved the project files to and your Houdini install dir (path://to/Houdini 18.5.xxx/)
* **In the Flask BACKEND**; Set the Python interpreter within your Intellij project settings to Hython - which you find in path/to/Houdini 18.5.xxx/bin/hython.exe. It will NOT work!
* **Inside of the React FRONTEND**; run *npm install* followed by *npm run build*. NOTE: Flask runs the build dir as a static site. You need to build for every change.

SPECIFICALLY for INTELLIJ on WINDOWS

* Start the React frontend in dev mode by simply doing a *npm start* in the FRONTEND dir. Intellij will automatically open the site under port 3000 in your browser. Close this.
* Start the Flask server by running the app.py from within Intellij with the **Run** (shift + F10 on win) command. Note that doing a "flask run" starts Flask with the wrong python interpreter, at least on my dev machine and by using the Intellij run command you force Flask with whatever interpreter you chose as part of your project settings.
* Open the React frontend using http://localhost:5000

HOW IT WORKS IN PRACTICE

The React frontend simply sends API calls and is completely unaware of the backend. The Flask backend deals with the API endpoints and then uses Hrpyc to directly send and receive commands from Houdini. Hrpyc is pretty much a wrapper for the Hou module, the Houdini API.

This solution has one big caveat! It only works if the Hrpyc server is already running and that can only be started from WITHIN Houdini. In the scripts sub-folder of the projects files is a super short script that does just that on starting up Houdini - starts the server. That is why I added a button to open Houdini on the front end - to make sure Houdini is configured for the communication with the outer world.

FINAL DISCLAIMER

This project is just a simple proof of concept I wrote in one evening and not meant to be production code. There are for sure much better ways to establish a React to Houdini pipeline and I would love to hear from anyone about your solution. Just drop a message in the issues in any of the three repos. 
import subprocess, os
import hrpyc
from flask import Flask, send_from_directory, request
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
import config

app = Flask(__name__, static_url_path='', static_folder='../frontend/build')
CORS(app)
api = Api(app)


@app.route("/", defaults={'path': ''})
def serve(path):
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/houdini/start', methods=['POST'])
def houdini():
    houdini_app = config.houdini_install_path + "bin/houdini.exe"
    houdini_default_file = config.local_project_file
    houdini_default_script = config.local_startup_script
    os.environ['JOB'] = config.local_project_root
    houdini_cmd = '{} {} {}'.format(houdini_app, houdini_default_file, houdini_default_script)
    subprocess.Popen(houdini_cmd)
    return 'ok'


@app.route('/houdini/sphere/<hue>', methods=['POST'])
def color_sphere(hue):
    connection, hou = hrpyc.import_remote_module()
    color = hou.node("/obj/geo1/color1")
    version = hou.applicationVersion()
    if hue == "red":
        color.parm("colorr").set(1)
        color.parm("colorg").set(0)
        color.parm("colorb").set(0)
    if hue == "green":
        color.parm("colorr").set(0)
        color.parm("colorg").set(1)
        color.parm("colorb").set(0)
    return 'ok'


if __name__ == "__main__":
    app.run()

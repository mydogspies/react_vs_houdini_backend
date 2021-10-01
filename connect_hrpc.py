import hrpyc

connection, hou = hrpyc.import_remote_module()
node = hou.node("/obj/sphere1/sphere1")
color = hou.node("/obj/sphere1/color1")
node.parm("scale").set(2.0)
color.parm("colorr").set(1)
color.parm("colorg").set(0)
color.parm("colorb").set(0)

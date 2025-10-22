bl_info = {
    "name": "Generate Shape Keys",
    "description": "Quickly generate blank ARKit shape keys on your mesh",
    "author": "lunazera",
    "version": (0, 1),
    "blender": (3, 0, 0),
    "location": "3D View > Tools",
    "warning": "",
}

import bpy

def register():
    from . import ui
    ui.register()

def unregister():
    from . import ui
    ui.unregister()


if __name__ == "__main__":
    register()
# Script for creating blank shapekeys
import bpy

from bpy.types import (Object, Mesh)

def Generate_Blank_Shapekeys(mesh_object: Object, blendshapes):
    if hasattr(mesh_object, 'data'):
        mesh = mesh_object.data
        if not isinstance(mesh, Mesh):
            return

        current_shapekeys = []

        # Check if there are any existing 
        if hasattr(mesh, 'shape_keys'):
            if hasattr(mesh.shape_keys, 'key_blocks'):
                current_shapekeys = mesh.shape_keys.key_blocks

        for shape in blendshapes:
            if not shape in current_shapekeys:
                mesh_object.shape_key_add(name=shape, from_mix=False)
import bpy

from .scripts.ARKitBlendshapes import *
from .scripts.Generate_Blank_Shapekeys import *

from bpy.props import (StringProperty,
                        CollectionProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       EnumProperty,
                       PointerProperty,
                       )
from bpy.types import (Panel,
                       Menu,
                       Operator,
                       PropertyGroup,
                       Object, Mesh, Armature
                       )
                   
                       
## Generate ARKit Shapekeys ##
# author: lunazera

# ------------------------------------------------------------------------
#    Scene Properties
# ------------------------------------------------------------------------
class GENSHAPES_PG_SceneProperties(PropertyGroup):
    name_mesh: StringProperty(
        name="Mesh",
        description="Name of your main mesh to add blendshapes from",
        default="",
        maxlen=1024,
        )

# ------------------------------------------------------------------------
#    Operators
# ------------------------------------------------------------------------
class WM_OT_Generate(Operator):
    bl_label = "Generate Shapekeys"
    bl_idname = "wm.generate" 

    def execute(self, context):
        scene = context.scene
        genshapes_tool = scene.genshapes_tool
        
        mesh = genshapes_tool.name_mesh.lstrip()

        print("Applying to " + mesh)
        if mesh:
            if mesh in bpy.data.objects:
                mesh_object = bpy.data.objects[mesh]
                blendshapes = Get_ARkit()
                Generate_Blank_Shapekeys(mesh_object, blendshapes)
            return {'FINISHED'}
        else:
            return {'CANCELLED'}

# ------------------------------------------------------------------------
#    Panel in Object Mode
# ------------------------------------------------------------------------
class OBJECT_PT_GENSHAPES(Panel):
    bl_label = "Generate ARKit Shapekeys"
    bl_idname = "OBJECT_PT_LZTools_GenerateShapekeys"
    bl_space_type = "VIEW_3D"   
    bl_region_type = "UI"
    bl_category = "LZTools"
    bl_context = "objectmode"  

    @classmethod
    def poll(self,context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False  # No animation.

        scene = context.scene
        genshapes_tool = scene.genshapes_tool

        layout.label(text="Name of mesh to apply")
        layout.prop(genshapes_tool, "name_mesh")
        
        layout.separator(factor=3)
        layout.operator("wm.generate")
        layout.separator()

##################################

classes = (
    WM_OT_Generate,
    GENSHAPES_PG_SceneProperties,
    OBJECT_PT_GENSHAPES
)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

    bpy.types.Scene.genshapes_tool = PointerProperty(type=GENSHAPES_PG_SceneProperties)

def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
    del bpy.types.Scene.genshapes_tool


if __name__ == "__main__":
    register()
bl_info = {
    "name": "Roblox Starter Rigs",
    "author": "SoftGB and Paribes",
    "version": (1, 2),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > Roblox Starter Rigs",
    "description": "Append the Roblox Starter Rigs",
    "warning": "",
    "doc_url": "",
    "category": "Object",
}


def register():
    pass


def unregister():
    pass

import bpy
import os

# Specify the path to the .blend file
script_directory = os.path.dirname(os.path.abspath(__file__))
script_directory = os.path.join(script_directory, "Rigs")
script_directory = os.path.normpath(script_directory)
blend_path1 = os.path.join(script_directory, "Starter_2.0_Rig.blend")
blend_path2 = os.path.join(script_directory, "Starter_Blocky_Rig.blend")
blend_path3 = os.path.join(script_directory, "Starter_Man_Rig.blend")
blend_path4 = os.path.join(script_directory, "Starter_Boy_Rig.blend")
blend_path5 = os.path.join(script_directory, "Starter_Superhero_Rig.blend")
blend_path6 = os.path.join(script_directory, "Starter_Girl_Rig.blend")
blend_path7 = os.path.join(script_directory, "Starter_Woman_Rig.blend")

# Specify the name of the collection to append
collection_name1 = "Starter 2.0 Rig"
collection_name2 = "Starter Blocky Rig"
collection_name3 = "Starter Man Rig"
collection_name4 = "Starter Boy Rig"
collection_name5 = "Starter Superhero Rig"
collection_name6 = "Starter Girl Rig"
collection_name7 = "Starter Woman Rig"

class AppendRobloxianOperator(bpy.types.Operator):
    bl_idname = "object.append_robloxian_operator"
    bl_label = "Append 2.0 Rig"
    bl_description = "Appends the Starter 2.0 Rig collection"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Append the collection from the .blend file
        with bpy.data.libraries.load(blend_path1, link=False) as (data_from, data_to):
            data_to.collections = [collection_name1]
        context.collection.children.link(data_to.collections[0])

        return {'FINISHED'}
    
class AppendBlockyOperator(bpy.types.Operator):
    bl_idname = "object.append_blocky_operator"
    bl_label = "Append Blocky Rig"
    bl_description = "Appends the Starter Blocky Rig collection"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Append the collection from the .blend file
        with bpy.data.libraries.load(blend_path2, link=False) as (data_from, data_to):
            data_to.collections = [collection_name2]
        context.collection.children.link(data_to.collections[0])

        return {'FINISHED'}
    
class AppendManOperator(bpy.types.Operator):
    bl_idname = "object.append_man_operator"
    bl_label = "Append Man Rig"
    bl_description = "Appends the Starter Man Rig collection"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Append the collection from the .blend file
        with bpy.data.libraries.load(blend_path3, link=False) as (data_from, data_to):
            data_to.collections = [collection_name3]
        context.collection.children.link(data_to.collections[0])

        return {'FINISHED'}
    
class AppendBoyOperator(bpy.types.Operator):
    bl_idname = "object.append_boy_operator"
    bl_label = "Append Boy Rig"
    bl_description = "Appends the Starter Boy Rig collection"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Append the collection from the .blend file
        with bpy.data.libraries.load(blend_path4, link=False) as (data_from, data_to):
            data_to.collections = [collection_name4]
        context.collection.children.link(data_to.collections[0])

        return {'FINISHED'}
    
class AppendSuperheroOperator(bpy.types.Operator):
    bl_idname = "object.append_superhero_operator"
    bl_label = "Append Superhero Rig"
    bl_description = "Appends the Starter Superhero Rig collection"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Append the collection from the .blend file
        with bpy.data.libraries.load(blend_path5, link=False) as (data_from, data_to):
            data_to.collections = [collection_name5]
        context.collection.children.link(data_to.collections[0])

        return {'FINISHED'}
    
class AppendGirlOperator(bpy.types.Operator):
    bl_idname = "object.append_girl_operator"
    bl_label = "Append Girl Rig"
    bl_description = "Appends the Starter Girl Rig collection"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Append the collection from the .blend file
        with bpy.data.libraries.load(blend_path6, link=False) as (data_from, data_to):
            data_to.collections = [collection_name6]
        context.collection.children.link(data_to.collections[0])

        return {'FINISHED'}
    
class AppendWomanOperator(bpy.types.Operator):
    bl_idname = "object.append_woman_operator"
    bl_label = "Append Woman Rig"
    bl_description = "Appends the Starter Woman Rig collection"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Append the collection from the .blend file
        with bpy.data.libraries.load(blend_path7, link=False) as (data_from, data_to):
            data_to.collections = [collection_name7]
        context.collection.children.link(data_to.collections[0])

        return {'FINISHED'}

class VIEW3D_PT_starter_rigs_panel(bpy.types.Panel):
    bl_label = "Starter Rigs"
    bl_idname = "VIEW3D_PT_starter_rigs_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Starter Rigs"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.menu("VIEW3D_MT_starter_rigs_menu", text="Select Rig")

class VIEW3D_MT_starter_rigs_menu(bpy.types.Menu):
    bl_label = "Starter Rigs"
    bl_idname = "VIEW3D_MT_starter_rigs_menu"

    def draw(self, context):
        layout = self.layout

        layout.operator("object.append_robloxian_operator", text="Starter 2.0 Rig", icon="OUTLINER_OB_ARMATURE")

        layout.operator("object.append_blocky_operator", text="Starter Blocky Rig", icon="OUTLINER_OB_ARMATURE")

        layout.operator("object.append_man_operator", text="Starter Man Rig", icon="OUTLINER_OB_ARMATURE")

        layout.operator("object.append_boy_operator", text="Starter Boy Rig", icon="OUTLINER_OB_ARMATURE")

        layout.operator("object.append_superhero_operator", text="Starter Superhero Rig", icon="OUTLINER_OB_ARMATURE")

        layout.operator("object.append_girl_operator", text="Starter Girl Rig", icon="OUTLINER_OB_ARMATURE")

        layout.operator("object.append_woman_operator", text="Starter Woman Rig", icon="OUTLINER_OB_ARMATURE")

def register():
    bpy.utils.register_class(VIEW3D_PT_starter_rigs_panel)
    bpy.utils.register_class(VIEW3D_MT_starter_rigs_menu)
    bpy.utils.register_class(AppendRobloxianOperator)
    bpy.utils.register_class(AppendBlockyOperator)
    bpy.utils.register_class(AppendManOperator)
    bpy.utils.register_class(AppendBoyOperator)
    bpy.utils.register_class(AppendSuperheroOperator)
    bpy.utils.register_class(AppendGirlOperator)
    bpy.utils.register_class(AppendWomanOperator)

def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_starter_rigs_panel)
    bpy.utils.unregister_class(VIEW3D_MT_starter_rigs_menu)
    bpy.utils.register_class(AppendRobloxianOperator)
    bpy.utils.register_class(AppendBlockyOperator)
    bpy.utils.register_class(AppendManOperator)
    bpy.utils.register_class(AppendBoyOperator)
    bpy.utils.register_class(AppendSuperheroOperator)
    bpy.utils.register_class(AppendGirlOperator)
    bpy.utils.register_class(AppendWomanOperator)

if __name__ == "__main__":
    register()

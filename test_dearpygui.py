import dearpygui.dearpygui as dpg
import dearpygui.demo as demo
from components.windows.ParamWindow import ParamWindow
dpg.create_context()

# def button_callback(sender, app_data, user_data):
#     print(f"sender is: {sender}")
#     print(f"app_data is: {app_data}")
#     print(f"user_data is: {user_data}")

# def print_value(sender):
#     print(dpg.get_value(sender))

with dpg.font_registry():
    try:
        dpg.bind_font(dpg.add_font("fonts/NotoSansSC-Medium.ttf", 24))
    except:
        pass

def save_callback(sender, app_data, user_data):
    dpg.save_init_file("dpg_layout.ini")
    print("Save button clicked")

def load_callback(sender, app_data, user_data):
    dpg.configure_app(docking=True, docking_space=True, init_file="dpg_layout.ini", load_init_file=True)
    print("Load button clicked")


with dpg.viewport_menu_bar():
    with dpg.menu(label="File"):
        dpg.add_menu_item(label="Save", callback=save_callback)
        dpg.add_menu_item(label="Load", callback=load_callback)
        dpg.add_menu_item(label="Exit")

    with dpg.menu(label="Edit"):
        dpg.add_menu_item(label="Undo")
        dpg.add_menu_item(label="Redo")
        dpg.add_menu_item(label="Cut")
        dpg.add_menu_item(label="Copy")
        dpg.add_menu_item(label="Paste")

    with dpg.menu(label="Help"):
        dpg.add_menu_item(label="About")


# 创建Dock Widgets
with dpg.window(label="Viewport", width=400, height=400) as viewport_window:
    dpg.add_text("3D Viewport")

with dpg.window(label="Side Panel", width=200, height=400) as side_panel_window:
    dpg.add_text("Side Panel")

with dpg.window(label="Console", width=600, height=200) as console_window:
    dpg.add_text("Console")

with dpg.window(label="Status Bar", width=800, height=50) as status_bar_window:
    dpg.add_text("Status Bar")


# dpg.show_documentation()
# dpg.show_style_editor()
# dpg.show_debug()
# dpg.show_about()
# dpg.show_metrics()
# dpg.show_item_registry()
# dpg.show_font_manager()
# dpg.show_implot_demo()
# dpg.show_imgui_demo()
# demo.show_demo() 

my_window = ParamWindow("Tutorial")
# my_window.add_child(my_button)
my_window.submit()

dpg.configure_app(docking=True, docking_space=True, init_file="dpg_layout.ini", load_init_file=True)
dpg.create_viewport(title='TBotViz')
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
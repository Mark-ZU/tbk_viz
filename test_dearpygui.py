import dearpygui.dearpygui as dpg

dpg.create_context()
# dpg.set_global_font_scale(1.5)

def button_callback(sender, app_data, user_data):
    print(f"sender is: {sender}")
    print(f"app_data is: {app_data}")
    print(f"user_data is: {user_data}")

def print_value(sender):
    print(dpg.get_value(sender))

# with dpg.font_registry():
#     dpg.bind_font(dpg.add_font("NotoSansSC-Medium.ttf", 24))

with dpg.window(label="Tutorial", width=300, height=600):
    dpg.add_button(label="Button 1")
    dpg.add_button(label="Button 2")
    # configuration set when button is created
    dpg.add_button(label="Apply", width=300)

    # user data and callback set any time after button has been created
    btn = dpg.add_button(label="Apply 2")
    dpg.set_item_label(btn, "Button 57")
    dpg.set_item_width(btn, 200)
    dpg.set_item_callback(btn, button_callback)
    dpg.set_item_user_data(btn, "Some Extra User Data")

    input_txt1 = dpg.add_input_text()
    # The value for input_text2 will have a starting value
    # of "This is a default value!"
    input_txt2 = dpg.add_input_text(
        label="InputTxt2",
        default_value="This is a default value!",
        callback=print_value
    )

    slider_float1 = dpg.add_slider_float()
    # The slider for slider_float2 will have a starting value
    # of 50.0.
    slider_float2 = dpg.add_slider_float(
        label="SliderFloat2",
        default_value=50.0,
        callback=print_value
    )

    dpg.set_item_callback(input_txt1, print_value)
    dpg.set_item_callback(slider_float1, print_value)

    print(dpg.get_value(input_txt1))
    print(dpg.get_value(input_txt2))
    print(dpg.get_value(slider_float1))
    print(dpg.get_value(slider_float2))

dpg.show_documentation()
dpg.show_style_editor()
dpg.show_debug()
dpg.show_about()
dpg.show_metrics()
dpg.show_item_registry()
dpg.show_font_manager()

dpg.create_viewport(title='Custom Title', width=1000, height=800)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
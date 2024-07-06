import dearpygui.dearpygui as dpg

class ParamWindow:
    def __init__(self, label):
        self._children = []
        with dpg.stage() as stage:
            self.id = dpg.add_window(label="Params")
        self.stage = stage
    def add_child(self, child):
        dpg.move_item(child.id, parent=self.id)
    def submit(self):
        dpg.unstage(self.stage)
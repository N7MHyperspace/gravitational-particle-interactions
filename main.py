from moderngl_window.context.base.window import WindowConfig
from moderngl_window import resources
import moderngl as mgl
from pathlib import Path

from moderngl_window.resources import (
    textures,
    programs,
    scenes,
    data,
)

from moderngl_window.meta import (
    TextureDescription,
    ProgramDescription,
    SceneDescription,
    DataDescription,
)

resources.register_dir(Path(__file__).parent / 'resource')
resources.register_dir(Path(__file__).parent / 'resource' / 'shader')

class Main(WindowConfig):
    gl_version = (3, 3)

    def __init__(self, **kwargs): # type: ignore
        super().__init__(**kwargs) # type: ignore 

        self.prog = programs.load(ProgramDescription(vertex_shader='vertex1.vert', fragment_shader='frag1.frag'))

    def on_render(self, time: float, frame_time: float):
        self.ctx.clear(1.0, 0.0, 0.0, 0.0)

    #####################
    ### Window events ###
    #####################
    def on_resize(self, width: int, height: int):
        print("Window was resized. buffer size is {} x {}".format(width, height))
    def on_close(self):
        print("The window is closing")

    #######################
    ### Keyboard events ###
    #######################
    def on_key_event(self, key, action, modifiers):
        # Key presses
        if action == self.wnd.keys.ACTION_PRESS:
            if key == self.wnd.keys.SPACE:
                print("SPACE key was pressed")
            # Using modifiers (shift and ctrl)
            if key == self.wnd.keys.Z and modifiers.shift:
                print("Shift + Z was pressed")
            if key == self.wnd.keys.Z and modifiers.ctrl:
                print("ctrl + Z was pressed")
        # Key releases
        elif action == self.wnd.keys.ACTION_RELEASE:
            if key == self.wnd.keys.SPACE:
                print("SPACE key was released")
    
    def on_unicode_char_entered(self, char: str):
        print('character entered:', char)

    ####################
    ### Mouse events ###
    ####################
    def on_mouse_position_event(self, x: int, y: int, dx: int, dy: int):
        print("Mouse position:", x, y, dx, dy)

    def on_mouse_drag_event(self, x: int, y: int, dx: int, dy: int):
        print("Mouse drag:", x, y, dx, dy)

    def on_mouse_scroll_event(self, x_offset: float, y_offset: float):
        print("Mouse wheel:", x_offset, y_offset)

    def on_mouse_press_event(self, x: int, y: int, button: int):
        print("Mouse button {} pressed at {}, {}".format(button, x, y))

    def on_mouse_release_event(self, x: int, y: int, button: int):
        print("Mouse button {} released at {}, {}".format(button, x, y))



if __name__ == '__main__':
    Main.run()


from moderngl_window.context.base.window import WindowConfig
from moderngl_window import resources
import moderngl as mgl
from moderngl import LINE_STRIP, DEPTH_TEST, POINTS
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

import numpy as np

resources.register_dir(Path(__file__).parent / 'resource')
resources.register_dir(Path(__file__).parent / 'resource' / 'shader')

class Main(WindowConfig):
    gl_version = (3, 3)

    def __init__(self, **kwargs): # type: ignore
        super().__init__(**kwargs) # type: ignore 
        self.ctx.enable(DEPTH_TEST)

        self.rp_prog = programs.load(ProgramDescription(vertex_shader='vertex1.vert', fragment_shader='frag1.frag'))
        self.up_prog = programs.load(ProgramDescription(vertex_shader='update1.vert', varyings=["out_cpos", "out_ppos"]))


        n = 5000000
        # positions


        # velocities
        a = np.random.rand(n) * 2.0 * np.pi * 1.0
        r = 0.25 + np.random.rand(n) * 0.001
        x = np.cos(a) * r
        y = np.sin(a) * r
        v = (1.0 + np.random.rand(n) * 0.1) * 0.01
        a += np.random.rand(n) * 2.0 * np.pi * 0.01
        vx = np.sin(a) * v
        vy = -np.cos(a) * v


        px = x + vx
        py = y + vy

        r = np.ones(n)
        g = np.zeros(n)
        b = np.zeros(n)

        particle_color = np.dstack([r, g, b])
        particle_pos_vel = np.column_stack([x, y, px, py]).astype('f4')

        # Two particle buffers
        self.up_vbo_a = self.ctx.buffer(particle_pos_vel.tobytes())
        self.up_vbo_b = self.ctx.buffer(reserve=n * 4 * 4)
        # copy a to b to initialize the second buffer with the same data
        self.up_vbo_b.write(self.up_vbo_a.read())

        self.up_vao_a = self.ctx.simple_vertex_array(self.up_prog, self.up_vbo_a, 'in_cpos', 'in_ppos')
        self.up_vao_b = self.ctx.simple_vertex_array(self.up_prog, self.up_vbo_b, 'in_cpos', 'in_ppos')

        self.rp_vbo = self.ctx.buffer(particle_color.astype('f4').tobytes())
        self.rp_vao = self.ctx.vertex_array(self.rp_prog, [(self.up_vbo_a, '2f 2f', 'in_cpos', 'in_ppos'), (self.rp_vbo, '3f', 'in_color')]) # type: ignore

        self.cam_x = 0.0
        self.cam_y = 0.0
        self.cam_zoom = 1.0
        self.cam_zzom = 1.0
        self.aspect_ratio = 1.0

    def on_render(self, time: float, frame_time: float):
        simulation_steps = 10
        fixed_dt = 1.0 / 60.0

        self.up_prog['dt'].value = fixed_dt * 0.5 / simulation_steps # type: ignore

        for _ in range(simulation_steps):
            self.up_vao_a.transform(self.up_vbo_b, vertices=self.up_vbo_a.size // (4 * 4)) # type: ignore
            self.up_vao_b.transform(self.up_vbo_a, vertices=self.up_vbo_b.size // (4 * 4)) # type: ignore


        self.cam_zzom += (self.cam_zoom - self.cam_zzom) * fixed_dt * 10.0

        self.aspect_ratio = self.wnd.height / self.wnd.width if self.wnd.width != 0 else 1.0
        self.rp_prog['aspect_ratio'].value = self.aspect_ratio # type: ignore
        self.rp_prog['camera_pos'].value = (self.cam_x, self.cam_y) # type: ignore
        self.rp_prog['camera_zoom'].value = self.cam_zzom # type: ignore
        self.ctx.screen.use()
        self.ctx.viewport = (0, 0, self.wnd.width, self.wnd.height)
        self.ctx.clear(0.0, 0.1, 0.1, 0.0)
        self.rp_vao.render(POINTS)

        
        



    #####################
    ### Window events ###
    #####################
    def on_resize(self, width: int, height: int):
        pass
        # print("Window was resized. buffer size is {} x {}".format(width, height))
    def on_close(self):
        pass
        # print("The window is closing")

    #######################
    ### Keyboard events ###
    #######################
    def on_key_event(self, key, action, modifiers):
        # Key presses
        if action == self.wnd.keys.ACTION_PRESS:
            if key == self.wnd.keys.SPACE:
                pass
                # print("SPACE key was pressed")
            # Using modifiers (shift and ctrl)
            if key == self.wnd.keys.Z and modifiers.shift:
                pass
                # print("Shift + Z was pressed")
            if key == self.wnd.keys.Z and modifiers.ctrl:
                pass
                # print("ctrl + Z was pressed")
        # Key releases
        elif action == self.wnd.keys.ACTION_RELEASE:
            if key == self.wnd.keys.SPACE:
                pass
                # print("SPACE key was released")
    
    def on_unicode_char_entered(self, char: str):
        pass
        # print('character entered:', char)

    ####################
    ### Mouse events ###
    ####################
    def on_mouse_position_event(self, x: int, y: int, dx: int, dy: int):
        pass
        # print("Mouse position:", x, y, dx, dy)

    def on_mouse_drag_event(self, x: int, y: int, dx: int, dy: int):
        if self.wnd.mouse_states.left: # type: ignore
            self.cam_x -= dx / self.aspect_ratio / self.cam_zoom / self.wnd.width * 2.0 # type: ignore
            self.cam_y += dy / self.cam_zoom / self.wnd.height * 2.0 # type: ignore
        # print("Mouse drag:", x, y, dx, dy)

    def on_mouse_scroll_event(self, x_offset: float, y_offset: float):
        self.cam_zoom += 0.1 * y_offset * self.cam_zoom # type: ignore
        self.cam_zoom = max(0.01, min(self.cam_zoom, 100.0))
        pass
        # print("Mouse wheel:", x_offset, y_offset)

    def on_mouse_press_event(self, x: int, y: int, button: int):
        pass
        # print("Mouse button {} pressed at {}, {}".format(button, x, y))

    def on_mouse_release_event(self, x: int, y: int, button: int):
        pass
        # print("Mouse button {} released at {}, {}".format(button, x, y))



if __name__ == '__main__':
    Main.run()


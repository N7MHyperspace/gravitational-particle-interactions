from moderngl_window.context.base.window import WindowConfig

class Test(WindowConfig):
    gl_version = (3, 3)

    def on_render(self, time: float, frame_time: float):
        self.ctx.clear(1.0, 0.0, 0.0, 0.0)

if __name__ == '__main__':
    Test.run()


from moderngl_window.context.base.window import WindowConfig
import moderngl as mgl
from pathlib import Path

ASSET = Path(__file__) / 'asset'
ASSET_SHADER = ASSET / 'shader'

class Main(WindowConfig):
    gl_version = (3, 3)

    def __init__(self, **kwargs): # type: ignore
        super().__init__(**kwargs) # type: ignore

        

    def on_render(self, time: float, frame_time: float):
        


        self.ctx.clear(1.0, 0.0, 0.0, 0.0)

if __name__ == '__main__':
    Main.run()


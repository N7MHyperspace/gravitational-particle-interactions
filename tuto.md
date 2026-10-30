Create buffer and program :
buffer       = store vertex data in graphics memory.
program      = glsl shader code.
vertex array = handle communication between buffer and program
frame buffer = offscreen render target. support texture and depth texture.


Mutable :
self.buf     = self.ctx.buffer(reserve=100)
self.prog    = self.ctx.program((ASSET_SHADER / 'shader.glsl').read_text())
self.tex     = self.ctx.texture()
self.fb      = self.ctx.framebuffer()

Immutable :
self.vert    = self.ctx.vertex_array()


#version 330

in vec2 in_cpos;
in vec2 in_ppos;
in vec3 in_color;

out vec3 v_color;

uniform float aspect_ratio;
uniform vec2 camera_pos;
uniform float camera_zoom;

void main() {
    float speed = length(in_ppos);
    v_color = in_color * min(1.0, speed * 10.0);

    gl_Position = vec4((in_cpos - camera_pos) * camera_zoom * vec2(aspect_ratio, 1.0), 0.0, 1.0);
}

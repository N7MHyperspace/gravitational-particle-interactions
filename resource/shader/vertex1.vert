#version 330

in vec2 in_vert;
in vec2 in_vel;
in vec3 in_color;

out vec3 v_color;

uniform float dt;

void main() {
    float speed = length(in_vel);
    v_color = in_color * min(1.0, speed * 10.0);

    vec2 pos = in_vert + in_vel * dt;

    gl_Position = vec4(pos, 0.0, 1.0);
}

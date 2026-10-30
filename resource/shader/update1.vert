#version 330

in vec2 in_pos;
in vec2 in_vel;

out vec2 out_pos;
out vec2 out_vel;

uniform float dt;

vec2 force(vec2 pos, vec2 vel) {
    float dist = length(pos);
    vec2 dir = normalize(pos);
    return -dir * dist * dist; // No force for now
}

void main() {
    out_pos = in_pos + in_vel * dt;
    out_vel = in_vel + dt * force(in_pos, in_vel);
}

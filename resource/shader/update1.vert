#version 330

in vec2 in_cpos;
in vec2 in_ppos;

out vec2 out_cpos;
out vec2 out_ppos;

uniform float dt;

vec2 force(vec2 pos) {
    float dist = length(pos);
    vec2 dir = normalize(pos);
    return -dir * dist * dist; // No force for now
}

void main() {
    vec2 acc = force(in_cpos);
    out_cpos = 2.0 * in_cpos - in_ppos + acc * dt * dt;
    out_ppos = in_cpos;
}

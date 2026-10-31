#version 330

in vec2 in_cpos;
in vec2 in_ppos;
in vec3 in_color;

out vec3 v_color;

uniform float aspect_ratio;
uniform vec2 camera_pos;
uniform float camera_zoom;

vec3 hsv2rgb(vec3 c)
{
    vec3 p = abs(fract(c.xxx / 360.0 + vec3(0.0, 2.0/3.0, 1.0/3.0))
                 * 6.0 - 3.0);

    return c.z * mix(vec3(1.0), clamp(p - 1.0, 0.0, 1.0), c.y);
}

vec3 rgb2hsv(vec3 c)
{
    vec4 K = vec4(0.0, -1.0/3.0, 2.0/3.0, -1.0);

    vec4 p = mix(vec4(c.bg, K.wz),
                 vec4(c.gb, K.xy),
                 step(c.b, c.g));

    vec4 q = mix(vec4(p.xyw, c.r),
                 vec4(c.r, p.yzx),
                 step(p.x, c.r));

    float d = q.x - min(q.w, q.y);
    float e = 1e-10;

    return vec3(
        360.0 * abs(q.z + (q.w - q.y) / (6.0 * d + e)),
        d / (q.x + e),
        q.x
    );
}

void main() {
    vec3 c = rgb2hsv(in_color);
    c.x += 20.0 * 360.0 * length(in_cpos - in_ppos);
    v_color = hsv2rgb(c);

    gl_Position = vec4((in_cpos - camera_pos) * camera_zoom * vec2(aspect_ratio, 1.0), 0.0, 1.0);
}

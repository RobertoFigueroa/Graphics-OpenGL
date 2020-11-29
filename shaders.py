# Los shaders de OpenGL se escriben en un lenguaje de progra llamado GLSL

vertex_shader = """
#version 460
layout (location = 0) in vec4 pos;
layout (location = 1) in vec4 normal;
layout (location = 2) in vec2 texcoords;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

uniform vec4 color;
uniform vec4 light;

uniform float ambient;

out vec4 vertexColor;
out vec2 vertexTexcoords;

void main()
{
    float intensity = dot(normal, normalize(light));

    gl_Position = projection * view * model * pos;
    vertexColor = vec4(ambient, ambient, ambient, 1) + color * intensity;
    vertexTexcoords = texcoords;
}
"""

vertex_shader2 = """
#version 460
layout (location = 0) in vec4 pos;
layout (location = 1) in vec4 normal;
layout (location = 2) in vec2 texcoords;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

uniform vec4 color;
uniform vec4 light;

uniform float ambient;
uniform float time;

out vec4 vertexColor;
out vec2 vertexTexcoords;

void main()
{
    


    float intensity = dot(normal, normalize(light));
    intensity = intensity * cos(time);
    gl_Position = projection * view * model * pos;
    vertexColor = vec4(ambient, ambient, ambient, 1) + color * intensity;
    vertexTexcoords = texcoords;
}
"""


vertex_shader3 = """
#version 460
layout (location = 0) in vec4 pos;
layout (location = 1) in vec4 normal;
layout (location = 2) in vec2 texcoords;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

uniform vec4 color;
uniform vec4 light;

uniform float ambient;

out vec4 vertexColor;
out vec2 vertexTexcoords;
out float intesity;

void main()
{
    float intensity = dot(normal, normalize(light));
    if(intensity < 0.25) {
        vertexColor = vec4(0.25,0.25,0.25,1);
    }
    else if(intensity >= 0.25 && intensity < 0.5){
        vertexColor = vec4(0.5,0.5,0.5,1);
    }
    else if(intensity >= 0.5 && intensity < 0.75){
        vertexColor = vec4(0.75,0.75,0.75,1);
    }
    else {
        vertexColor = vec4(1,1,1,1);
    }
    gl_Position = projection * view * model * pos;
    vertexTexcoords = texcoords;
}
"""



fragment_shader = """
#version 460
layout (location = 0) out vec4 diffuseColor;

in vec4 vertexColor;
in vec2 vertexTexcoords;

uniform sampler2D tex;

void main()
{
    diffuseColor =  vertexColor * texture(tex, vertexTexcoords);
}
"""

vertex_shader4 = """
#version 460
layout (location = 0) in vec4 pos;
layout (location = 1) in vec4 normal;
layout (location = 2) in vec2 texcoords;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

uniform vec4 color;
uniform vec4 light;

uniform float ambient;
uniform float time;

out vec4 vertexColor;
out vec2 vertexTexcoords;

void main()
{
    

    float intensity = dot(normal, normalize(light));

    gl_Position = projection * view * model * pos;
    _vertexColor = vec4(ambient, ambient, ambient, 1) + color * intensity;
    newVertColor = (_vertexColor.x, _vertexColor.y, _vertexColor.z, cos(time));
    vertexColor = newVertColor;
    vertexTexcoords = texcoords;
}
"""

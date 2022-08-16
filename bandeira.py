import numpy as np
from OpenGL.GL import *
import glfw

glfw.init()
# creating a window size having 900 as width and 700 as height
window = glfw.create_window(900, 700, "PyOpenGL Bandeira", None,None)
glfw.set_window_pos(window, 500, 300)
glfw.make_context_current(window)

vertices = [-1.0, -1.0,0.0,
             -1.0, 0.8,0.0,
             0.8, -1.0,0.0,
             ]
        
vertices1 = [1.0, 1.0,0.0,
             1.0, -0.8,0.0,
             -0.8, 1.0,0.0,
             ]

vertquadrado = [-1.0, 1.0, 0.0,
                -0.4, 1.0, 0.0,
                -0.4, 0.4, 0.0,
                 -1.0, 0.4, 0.0]

v = np.array(vertices, dtype = np.float32)

vq = np.array(vertices1, dtype=np.float32)

# this will draw a colorless triangle
glEnableClientState(GL_VERTEX_ARRAY)
glVertexPointer(3, GL_FLOAT,0,v)
glVertexPointer(1, GL_FLOAT,0,vq)

# this will set a color for your background
glClearColor(255, 0, 0, 0)
#glColor3f(0.0, 0.0, 1.0)

while not glfw.window_should_close(window):
    glfw.poll_events()
    glClear(GL_COLOR_BUFFER_BIT)
    glDrawArrays(GL_TRIANGLES,0,3)
    glfw.swap_buffers(window)

glfw.terminate()
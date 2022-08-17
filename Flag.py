from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def Desenha():
    glClearColor(1.0, 1.0, 1.0, 1.0) # Define o fundo branco

    glMatrixMode(GL_MODELVIEW)
    
#DesenhaTriangulo do meio
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 255.0)

    glBegin(GL_TRIANGLES)
    glVertex2f(-0.25, 0.0)
    glVertex2f(0.25, 0.0)
    glVertex2f(0.0, -0.2)
    glEnd()
    glFlush()

#DesenhaTriangulo de cima

    glBegin(GL_TRIANGLES)
    glVertex2f(0.08, 0.0)
    glVertex2f(-0.08, 0.0)
    glVertex2f(0.0, 0.25)
    glEnd()
    glFlush()

#Desenha Triangulo de baixo -- esquerda
    glBegin(GL_TRIANGLES)
    glVertex2f(0.0, -0.2)
    glVertex2f(-0.17, -0.4)
    glVertex2f(-0.08, -0.06)
    glEnd()
    glFlush()

#Desenha Triangulo de baixo -- direita

    glBegin(GL_TRIANGLES)
    glVertex2f(0.0, -0.2)
    glVertex2f(0.17, -0.4)
    glVertex2f(0.08, -0.06)
    glEnd()
    glFlush()

# Desenha Triangulo Vermelho de cima

#    glLoadIdentity()
    glBegin(GL_TRIANGLES)
#    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(255.0, 0.0, 0.0)
    glVertex2f(-0.8, 1.0)
    glVertex2f(1.0, 1.0)
    glVertex2f(1.0, -0.5)
    glEnd()
    glFlush()


# Desenha Triangulo Vermelho de baixo
    glBegin(GL_TRIANGLES)
    glVertex2f(-1.0, 0.2)
    glVertex2f(-1.0, -1.0)
    glVertex2f(0.7, -1.0)
    glEnd()
    glFlush()


#// Programa Principal 
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500,300)
    glutCreateWindow(b'Bandeira')
    glutDisplayFunc(Desenha)
#    glutDisplayFunc(DesenhaTriangulo)
#    glutDisplayFunc(DesenhaTriangulo2)
#    glutDisplayFunc(TeladeFundo)
    glutMainLoop()

main()

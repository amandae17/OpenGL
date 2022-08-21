from pydoc import describe
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def Desenha():

    glClearColor(1.0,0.0,0.0,1.0) # Define fundo vermelho
    glMatrixMode(GL_MODELVIEW)

# Define a cor da estrela
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 255.0)

#Desenha estrela 
    glBegin(GL_POLYGON)
#    glVertex2f(0.0, 0.25) # ponta superior
#    glVertex2f(-0.15, 0.0) # lateral esquerda
#    glVertex2f(-0.25, 0.0) # ponta da esquerda
#    glVertex2f(-0.08, -0.06) # lateral esquerda inferior
#    glVertex2f(-0.17, -0.4) # ponta esquerda inderior
#    glVertex2f(0.0, -0.2) # meio inferior
#    glVertex2f(0.17, -0.4) # ponta direita inferior
#    glVertex2f(-0.08,0.4) #lateral direita inferior
#    glVertex2f(0.25, 0.0) # ponta da direita
#    glVertex2f(0.15, 0.0) # lateral direita 
#    glVertex2f(0.0, 0.25)

    glVertex2f(0.0, 0.25) # ponta superior
    glVertex2f(0.15, 0.0) # lateral direita 
    glVertex2f(0.25, 0.0) # ponta da direita
    
    glVertex2f(-0.15, 0.0) # lateral esquerda
    glVertex2f(-0.25, 0.0) # ponta da esquerda
    glVertex2f(-0.08, -0.06) # lateral esquerda inferior
    glVertex2f(-0.08,0.4) #lateral direita inferior
    glVertex2f(-0.17, -0.4) # ponta esquerda inderior
    glVertex2f(0.17, -0.4) # ponta direita inferior
    glVertex2f(0.0, -0.2) # meio inferior
    
    
    glVertex2f(0.0, 0.25)

    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500,300)
    glutCreateWindow(b'Estrela')
    glutDisplayFunc(Desenha)
    glutMainLoop()

main()
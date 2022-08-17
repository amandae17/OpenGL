from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
#import sys

def TeladeFundo():
    #glClearColor(1.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)#Limpa a janela de visualização com a cor de fundo especificada 
    glClearColor(1.0, 0.0, 0.0, 1.0)#Define a cor de fundo da janela de visualização como vermelha
    glFlush()#Executa os comandos OpenGL 
    
def DesenhaTriangulo():
    glBegin(GL_TRIANGLES)
    glVertex2f(-1.0, -25.0)
    glVertex2f(0.0, 1.0)
    glVertex2f(1.0, -1.0)
    glEnd()

#// Programa Principal 
def main():
    glutInit(sys.argv)
    #glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutCreateWindow(b'Estrela')
    glutDisplayFunc(TeladeFundo)
    glutInitWindowSize(500,300)
    #glutBitmapWidth(DesenhaTriangulo)
    #glutDisplayFunc(DesenhaTriangulo)
    glutMainLoop()

main()

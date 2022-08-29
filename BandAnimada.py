from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def Desenha():
    glClearColor(0.0, 0.0, 0.0, 0.0) # Define o fundo preto

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

# Desenha Poligono branco
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POLYGON)
    glColor3f(255.0,255.0,255.0)
    glVertex2f(-0.3, 0.3)
    glVertex2f(-0.3, -0.3)
    glVertex2f(0.3, -0.3)
    glVertex2f(0.3, 0.3)
    glEnd()

#Define cor da estrela
    glColor3f(0.0, 0.0, 255.0)

#### --- Começo da estrela

    glBegin(GL_TRIANGLES)
    glVertex2f(-0.08, 0.0)
    glVertex2f(0.0, -0.08)
    glVertex2f(0.08, 0.0)
    glEnd()

#DesenhaTriangulo de cima

    glBegin(GL_TRIANGLES)
    glVertex2f(-0.03, 0.0)
    glVertex2f(0.03, 0.0)
    glVertex2f(0.0, 0.06)
    glEnd()

#Desenha Triangulo de baixo -- esquerda
    glBegin(GL_TRIANGLES)
    glVertex2f(0.0, -0.08)
    glVertex2f(-0.05, -0.13)
    glVertex2f(-0.03, -0.01)
    glEnd()

#Desenha Triangulo de baixo -- direita

    glBegin(GL_TRIANGLES)
    glVertex2f(0.0, -0.08)
    glVertex2f(0.05, -0.13)
    glVertex2f(0.03, -0.01)
    glEnd()

####  --- Final da estrela

# Desenha Triangulo Vermelho de cima

    glBegin(GL_TRIANGLES)
    glColor3f(255.0, 0.0, 0.0)
    glVertex2f(-0.2, 0.3)
    glVertex2f(0.3, 0.3)
    glVertex2f(0.3, -0.1)
    glEnd()



# Desenha Triangulo Vermelho de baixo
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.3, 0.0)
    glVertex2f(-0.3, -0.3)
    glVertex2f(0.2, -0.3)
    glEnd()
    glFlush()


def AlterandoTamanhoJanela(w,h):
    if( h==0):
        h = 1
    
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    print(w,h, "\n")
    gluOrtho2D(0.0, 100.0, 100.0, 0.0)

#// Programa Principal 
def main():
    glutInit(sys.argv)    
    glutReshapeFunc(AlterandoTamanhoJanela)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500,300)
    glutCreateWindow(b'Bandeira')
    glutDisplayFunc(Desenha)
    glutMainLoop()

main()
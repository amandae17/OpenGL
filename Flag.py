from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def Desenha():
    glClearColor(0.0, 0.0, 0.0, 0.0) # Define o fundo branco

    glMatrixMode(GL_MODELVIEW)
    
#Define cor da estrela
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(255.0,255.0,255.0)
    glBegin(GL_POLYGON)
    glVertex2f(10.0,10.0)
    glVertex2f(-10.0,10.0)
    glVertex2f(-10.0,-10.0)
    glVertex2f(10.0,-10.0)
    glEnd()

    
    glColor3f(0.0, 0.0, 255.0)

#### --- Começo da estrela

    glBegin(GL_TRIANGLES)
    glVertex2f(-0.25, 0.0)
    glVertex2f(0.25, 0.0)
    glVertex2f(0.0, -0.2)
    glEnd()

#DesenhaTriangulo de cima

    glBegin(GL_TRIANGLES)
    glVertex2f(0.08, 0.0)
    glVertex2f(-0.08, 0.0)
    glVertex2f(0.0, 0.25)
    glEnd()

#Desenha Triangulo de baixo -- esquerda
    glBegin(GL_TRIANGLES)
    glVertex2f(0.0, -0.2)
    glVertex2f(-0.17, -0.4)
    glVertex2f(-0.08, -0.06)
    glEnd()

#Desenha Triangulo de baixo -- direita

    glBegin(GL_TRIANGLES)
    glVertex2f(0.0, -0.2)
    glVertex2f(0.17, -0.4)
    glVertex2f(0.08, -0.06)
    glEnd()

####  --- Final da estrela

# Desenha Triangulo Vermelho de cima

    glBegin(GL_TRIANGLES)
    glColor3f(255.0, 0.0, 0.0)
    glVertex2f(-0.8, 1.0)
    glVertex2f(1.0, 1.0)
    glVertex2f(1.0, -0.5)
    glEnd()



# Desenha Triangulo Vermelho de baixo
    glBegin(GL_TRIANGLES)
    glVertex2f(-1.0, 0.2)
    glVertex2f(-1.0, -1.0)
    glVertex2f(0.6, -1.0)
    glEnd()
    glFlush()

def AlterandoTamanhoJanela(w,h):
    if( h==0):
        h = 15
    
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

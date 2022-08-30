from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

global windowWidth,windowHeight,x1,y1,xstep,ystep
windowWidth = 100
windowHeight = 50

x1 = 0.0
y1 = 0.0

xstep = 0.01
ystep = 0.01

def Desenha():
    global windowWidth,windowHeight,x1,y1,xstep,ystep
    
    glClearColor(0.0, 0.0, 0.0, 0.0) # Define o fundo preto

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

# Desenha Poligono branco
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POLYGON)
    glColor3f(255.0,255.0,255.0)
    glVertex2f(-0.3+x1, 0.3+y1)
    glVertex2f(-0.3+x1, -0.3+y1)
    glVertex2f(0.3+x1, -0.3+y1)
    glVertex2f(0.3+x1, 0.3+y1)
    glEnd()

#Define cor da estrela
    glColor3f(0.0, 0.0, 255.0)

#### --- Começo da estrela

    glBegin(GL_TRIANGLES)
    glVertex2f(-0.08+x1, 0.0+y1)
    glVertex2f(0.0+x1, -0.08+y1)
    glVertex2f(0.08+x1, 0.0+y1)
    glEnd()

#DesenhaTriangulo de cima

    glBegin(GL_TRIANGLES)
    glVertex2f(-0.03+x1, 0.0+y1)
    glVertex2f(0.03+x1, 0.0+y1)
    glVertex2f(0.0+x1, 0.06+y1)
    glEnd()

#Desenha Triangulo de baixo -- esquerda
    glBegin(GL_TRIANGLES)
    glVertex2f(0.0+x1, -0.08+y1)
    glVertex2f(-0.05+x1, -0.13+y1)
    glVertex2f(-0.03+x1, -0.01+y1)
    glEnd()

#Desenha Triangulo de baixo -- direita

    glBegin(GL_TRIANGLES)
    glVertex2f(0.0+x1, -0.08+y1)
    glVertex2f(0.05+x1, -0.13+y1)
    glVertex2f(0.03+x1, -0.01+y1)
    glEnd()

####  --- Final da estrela

# Desenha Triangulo Vermelho de cima

    glBegin(GL_TRIANGLES)
    glColor3f(255.0, 0.0, 0.0)
    glVertex2f(-0.2+x1, 0.3+y1)
    glVertex2f(0.3+x1, 0.3+y1)
    glVertex2f(0.3+x1, -0.1+y1)
    glEnd()



# Desenha Triangulo Vermelho de baixo
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.3+x1, 0.0+y1)
    glVertex2f(-0.3+x1, -0.3+y1)
    glVertex2f(0.2+x1, -0.3+y1)
    glEnd()
    glutSwapBuffers()

def Timer(value):
    global windowWidth,WindowHeight,x1,y1,xstep,ystep
    if(x1 > windowWidth or x1 <0):
        xstep = -xstep

    if(y1 > windowWidth or y1 <0):
        ystep = -ystep

    if(x1 > windowWidth):
        x1 = windowWidth-1

    if(y1 > windowHeight):
        y1 = windowHeight-1


    x1 += xstep
    y1 += ystep

    glutPostRedisplay()
    glutTimerFunc(33,Timer, 1)

def Inicializa():
    glClearColor(0.0,0.0,0.0,1.0)

def AlterandoTamanhoJanela(w,h):
    global windowWidth,WindowHeight,x1,y1,xstep,ystep
    if( h==0):
        h = 1
    
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    if (w <= h):
        windowHeight = 4.0*h/w
        windowWidth = 2.0
    else:
        windowHeight = 4.0*h/w
        windowWidth = 2.0
        
    gluOrtho2D(0.0, windowWidth, 0.0, windowHeight)

#// Programa Principal 
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    glutInitWindowSize(100,50);
    glutInitWindowPosition(10,10);
    glutCreateWindow(b"Anima");
    glutDisplayFunc(Desenha);
    glutReshapeFunc(AlterandoTamanhoJanela);
    glutTimerFunc(33, Timer, 1);
    Inicializa();
    glutMainLoop();

main()

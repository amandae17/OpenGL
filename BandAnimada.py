from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

global windowWidth,windowHeight,xf,yf,xstep,ystep
windowWidth = 100
windowHeight = 50

xf = 0.0
yf = 0.0

xstep = 0.01
ystep = 0.01

def Desenha():
    global windowWidth,windowHeight,xf,yf,xstep,ystep
    
    glClearColor(0.0, 0.0, 0.0, 0.0) # Define o fundo preto

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

# Desenha Poligono branco
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POLYGON)
    glColor3f(255.0,255.0,255.0)
    glVertex2f(-0.3+xf, 0.3+yf)
    glVertex2f(-0.3+xf, -0.3+yf)
    glVertex2f(0.3+xf, -0.3+yf)
    glVertex2f(0.3+xf, 0.3+yf)
    glEnd()

#Define cor da estrela
    glColor3f(0.0, 0.0, 255.0)

#### --- Começo da estrela

    glBegin(GL_TRIANGLES)
    glVertex2f(-0.08+xf, 0.0+yf)
    glVertex2f(0.0+xf, -0.08+yf)
    glVertex2f(0.08+xf, 0.0+yf)
    glEnd()

#DesenhaTriangulo de cima

    glBegin(GL_TRIANGLES)
    glVertex2f(-0.03+xf, 0.0+yf)
    glVertex2f(0.03+xf, 0.0+yf)
    glVertex2f(0.0+xf, 0.06+yf)
    glEnd()

#Desenha Triangulo de baixo -- esquerda
    glBegin(GL_TRIANGLES)
    glVertex2f(0.0+xf, -0.08+yf)
    glVertex2f(-0.05+xf, -0.13+yf)
    glVertex2f(-0.03+xf, -0.01+yf)
    glEnd()

#Desenha Triangulo de baixo -- direita

    glBegin(GL_TRIANGLES)
    glVertex2f(0.0+xf, -0.08+yf)
    glVertex2f(0.05+xf, -0.13+yf)
    glVertex2f(0.03+xf, -0.01+yf)
    glEnd()

####  --- Final da estrela

# Desenha Triangulo Vermelho de cima

    glBegin(GL_TRIANGLES)
    glColor3f(255.0, 0.0, 0.0)
    glVertex2f(-0.2+xf, 0.3+yf)
    glVertex2f(0.3+xf, 0.3+yf)
    glVertex2f(0.3+xf, -0.1+yf)
    glEnd()



# Desenha Triangulo Vermelho de baixo
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.3+xf, 0.0+yf)
    glVertex2f(-0.3+xf, -0.3+yf)
    glVertex2f(0.2+xf, -0.3+yf)
    glEnd()
    glutSwapBuffers()

def Timer(value):
    global windowWidth,WindowHeight,xf,yf,xstep,ystep
    if(xf > windowWidth or xf <0):
        xstep = -xstep

    if(yf > windowWidth or yf <0):
        ystep = -ystep

    if(xf > windowWidth):
        xf = windowWidth-0.1

    if(yf > windowHeight):
        yf = windowHeight-0.1


    xf += xstep
    yf += ystep

    glutPostRedisplay()
    glutTimerFunc(33,Timer, 1)

def Inicializa():
    glClearColor(0.0,0.0,0.0,1.0)

def AlterandoTamanhoJanela(w,h):
    global windowWidth,WindowHeight,xf,yf,xstep,ystep
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
    glutInitWindowSize(300,150);
    glutInitWindowPosition(10,10);
    glutCreateWindow(b"Anima");
    glutDisplayFunc(Desenha);
    glutReshapeFunc(AlterandoTamanhoJanela);
    glutTimerFunc(33, Timer, 1);
    Inicializa();
    glutMainLoop();

main()

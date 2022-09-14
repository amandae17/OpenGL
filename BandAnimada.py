from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

global wo,ho,windowWidth,windowHeight,x1,y1,xstep,ystep

x1 = 400
y1 = 400
xstep = 1.0
ystep = 1.0

#Funcao callback chamada para fazer o desenho
def Desenha():
    global wo,ho, windowWidth, windowHeight,x2,y2,x1,y1
    
    glClear(GL_COLOR_BUFFER_BIT)
    

    # Desenha Poligono branco
    glBegin(GL_POLYGON)
    glColor3f(255.0,255.0,255.0)
    glVertex2f(-40+x1, 30+y1)
    glVertex2f(-40+x1, -30+y1)
    glVertex2f(40+x1, -30+y1)
    glVertex2f(40+x1,30+y1)
    glEnd()
    
#Define cor da estrela
    glColor3f(0.0, 0.0, 255.0)

#### --- Começo da estrela

    glBegin(GL_TRIANGLES)
    glVertex2f(-8+x1, 0.0+y1)
    glVertex2f(0.0+x1, -8+y1)
    glVertex2f(8+x1, 0.0+y1)
    glEnd()

#DesenhaTriangulo de cima

    glBegin(GL_TRIANGLES)
    glVertex2f(-3+x1, 0.0+y1)
    glVertex2f(3+x1, 0.0+y1)
    glVertex2f(0.0+x1, 6+y1)
    glEnd()

#Desenha Triangulo de baixo -- esquerda
    glBegin(GL_TRIANGLES)
    glVertex2f(0.0+x1, -8+y1)
    glVertex2f(-5+x1, -13+y1)
    glVertex2f(-3+x1, -1+y1)
    glEnd()

#Desenha Triangulo de baixo -- direita

    glBegin(GL_TRIANGLES)
    glVertex2f(0.0+x1, -8+y1)
    glVertex2f(5+x1, -13+y1)
    glVertex2f(3+x1, -1+y1)
    glEnd()


####  --- Final da estrela

# Desenha Triangulo Vermelho de baixo

    glBegin(GL_TRIANGLES)
    glColor3f(255.0, 0.0, 0.0)
    glVertex2f(-40+x1, 0.0+y1)
    glVertex2f(-40+x1, -30+y1)
    glVertex2f(20+x1, -30+y1)
    glEnd()

# Desenha Triangulo Vermelho de cima
    glBegin(GL_TRIANGLES)
    glVertex2f(40+x1, 0+y1)
    glVertex2f(40+x1, 30+y1)
    glVertex2f(-20+x1, 30+y1)
    glEnd()
    glutSwapBuffers()

    

def Inicializa ():
    glClearColor(0.0, 0.0, 0.0, 1.0)

def AlteraTamanhoJanela(w, h):
    global windowWidth,windowHeight,x1,y1,rsize,xstep,ystep
    # Evita a divisao por zero
    if(h == 0):
        h = 1
                           
    # Especifica as dimensões da Viewport
    glViewport(0, 0, w, h)

    # Inicializa o sistema de coordenadas
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # Estabelece a janela de seleção (left, right, bottom, top)     
    if (w <= h):
        windowHeight = 250.0*h/w
        windowWidth = 250.0
    else:
        windowWidth = 250.0*w/h
        windowHeight = 250.0

    #windowWidth = w
    #windowHeight = h
    gluOrtho2D(0.0, windowWidth, 0.0, windowHeight)                      

def Timer(value):
  global windowWidth,windowHeight,x1,y1,xstep,ystep
  if(x1 > windowWidth-40 or x1 < 0): xstep = -xstep #muda direção lateral

  if(y1 > windowHeight-30 or y1 < 0): ystep = -ystep #muda direção superior e inferior

  if(x1 > windowWidth-40): x1 = windowWidth-40-1
  
  if(y1 > windowHeight-30): y1 = windowHeight-30-1

  x1 += xstep
  y1 += ystep

  glutPostRedisplay()
  glutTimerFunc(33,Timer,1)
    
  
def main():
     glutInit(sys.argv)
     glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
     glutInitWindowSize(600,600);
     glutInitWindowPosition(10,10);
     glutCreateWindow(b"Bandeira Animada");
     glutDisplayFunc(Desenha);
     glutReshapeFunc(AlteraTamanhoJanela);
     glutTimerFunc(33,Timer,1)    
     Inicializa();
     glutMainLoop();

main()

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

global wo,ho,windowWidth,windowHeight,x1,y1,xstep,ystep,x2,y2,win

x1 = 140
y1 = 310
x2 = 140
y2 = 310
xstep = 1.0
ystep = 1.0

#Funcao callback chamada para fazer o desenho
def Desenha():
    global wo,ho, windowWidth, windowHeight,x2,y2,x1,y1
    
    glClear(GL_COLOR_BUFFER_BIT)
    glViewport(0, 0, int(wo/2), int(ho))
    
    # Inicializa o sistema de coordenadas
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    if (wo <= ho):
        windowHeight = 300*ho/wo
        windowWidth = 350
    else:
        windowWidth = 300*wo/ho
        windowHeight = 350
    gluOrtho2D(0.0, windowWidth, 0.0, windowHeight);

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
    glVertex2f(40+x1, 5+y1)
    glVertex2f(40+x1, 30+y1)
    glVertex2f(-20+x1, 30+y1)
    glEnd()

# ///  //Segunda View port

    glViewport(int(wo/2), 0, int(wo/2), ho);
#    // Inicializa o sistema de coordenadas

    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
     
    gluOrtho2D(0.0, windowWidth, 0.0, windowHeight);
    
    # Desenha Poligono branco
    #glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POLYGON)
    glColor3f(255.0,255.0,255.0)
    glVertex2f(-40+x2, 30+y2)
    glVertex2f(-40+x2, -30+y2)
    glVertex2f(40+x2, -30+y2)
    glVertex2f(40+x2,30+y2)
    glEnd()
    
#Define cor da estrela
    glColor3f(0.0, 0.0, 255.0)

#### --- Começo da estrela

    glBegin(GL_TRIANGLES)
    glVertex2f(-8+x2, 0.0+y2)
    glVertex2f(0.0+x2, -8+y2)
    glVertex2f(8+x2, 0.0+y2)
    glEnd()

#DesenhaTriangulo de cima

    glBegin(GL_TRIANGLES)
    glVertex2f(-3+x2, 0.0+y2)
    glVertex2f(3+x2, 0.0+y2)
    glVertex2f(0.0+x2, 6+y2)
    glEnd()

#Desenha Triangulo de baixo -- esquerda
    glBegin(GL_TRIANGLES)
    glVertex2f(0.0+x2, -8+y2)
    glVertex2f(-5+x2, -13+y2)
    glVertex2f(-3+x2, -1+y2)
    glEnd()

#Desenha Triangulo de baixo -- direita

    glBegin(GL_TRIANGLES)
    glVertex2f(0.0+x2, -8+y2)
    glVertex2f(5+x2, -13+y2)
    glVertex2f(3+x2, -1+y2)
    glEnd()

####  --- Final da estrela

# Desenha Triangulo Vermelho de baixo

    glBegin(GL_TRIANGLES)
    glColor3f(255.0, 0.0, 0.0)
    glVertex2f(-40+x2, 5+y2)
    glVertex2f(-40+x2, -30+y2)
    glVertex2f(20+x2, -30+y2)
    glEnd()



# Desenha Triangulo Vermelho de cima
    glBegin(GL_TRIANGLES)
    glVertex2f(40+x2, 0.0+y2)
    glVertex2f(40+x2, 30+y2)
    glVertex2f(-20+x2, 30+y2)
    glEnd()
    glutSwapBuffers()

    

def Inicializa ():
    global win
    win = 350
    glClearColor(0.0, 0.0, 0.0, 1.0)

def AlteraTamanhoJanela(w, h):
    global wo,ho, view_h, view_w
    if(h == 0): h = 1
    wo=w;
    ho=h;                      

def Timer(value):
  global windowWidth,windowHeight,x1,y1,xstep,ystep
  if(x1 > windowWidth-40 or x1 < 0): xstep = -xstep

  if(y1 > windowHeight-30 or y1 < 0): ystep = -ystep

  if(x1 > windowWidth+40): x1 = windowWidth
  
  if(y1 > windowHeight+30): y1 = windowHeight

  x1 += xstep
  y1 += ystep

  glutPostRedisplay()
  glutTimerFunc(33,Timer,1)

def GerenciaTeclado(key, x, y):
    if(key==b'R' or key ==b'r'):
        glColor3f(1.0, 0.0, 0.0)
    elif (key==b'G' or key ==b'g'):
        glColor3f(0.0, 1.0, 0.0)
    elif (key==b'B' or key ==b'b'):
        glColor3f(0.0, 0.0, 1.0)
    glutPostRedisplay()

def GerenciaMouse(button, state, x, y):
    global x2, y2, win,wo,ho
    if (button == GLUT_LEFT_BUTTON):
         if (state == GLUT_DOWN):
                  # Troca o tamanho do retângulo, que vai do centro da 
                  # janela até a posição onde o usuário clicou com o mouse
                  escalax = (400)/(wo);

                  x2 = (x-wo/2)*escalax;

                  escalay= 400/(ho);

                  y2 = y*escalay;
    glutPostRedisplay()

def TeclasEspeciais(key, x, y):
    global x2, y2,win
    if(key == GLUT_KEY_UP):
           y2=y2+5           
           if (y2>310): y2=310
    if(key == GLUT_KEY_DOWN):
           y2=y2-3
           if (y2<30): y2=30

    if(key == GLUT_KEY_LEFT):
           x2=x2-3
           if (x2-40<0): x2=x2+3
           
    if(key == GLUT_KEY_RIGHT):
           x2=x2+3
           if (x2+30>win): x2=win-30

    glutPostRedisplay()
    
  
def main():
     glutInit(sys.argv)
     glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
     glutInitWindowSize(500,400);
     glutInitWindowPosition(10,10);
     glutCreateWindow(b"Para Multiplas ViewPorts");
     glutDisplayFunc(Desenha);
     glutReshapeFunc(AlteraTamanhoJanela);
     glutTimerFunc(33,Timer,1)
     glutKeyboardFunc(GerenciaTeclado)
     glutMouseFunc(GerenciaMouse)
     glutSpecialFunc(TeclasEspeciais)    
     Inicializa();
     glutMainLoop();

main()

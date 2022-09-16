from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

global x1,y1, win, view_w, view_h, wo, ho

def Desenha():
    global x1,y1, win, view_w, view_h
    
    glClearColor(0.0, 0.0, 0.0, 0.0) # Define o fundo preto

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

# Desenha Poligono branco
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POLYGON)
    glColor3f(255.0,255.0,255.0)
    glVertex2f(-0.4+x1, 0.3+y1)
    glVertex2f(-0.4+x1, -0.3+y1)
    glVertex2f(0.4+x1, -0.3+y1)
    glVertex2f(0.4+x1, 0.3+y1)
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
    glVertex2f(0.4+x1, 0.3+y1)
    glVertex2f(0.4+x1, -0.1+y1)
    glEnd()



# Desenha Triangulo Vermelho de baixo
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.4+x1, 0.0+y1)
    glVertex2f(-0.4+x1, -0.3+y1)
    glVertex2f(0.2+x1, -0.3+y1)
    glEnd()
    glutSwapBuffers()


def Inicializa():
    global x1,y1, win
    glClearColor(0.0,0.0,0.0,1.0)
    x1=1.0
    y1=1.0
    win=250.0

def AlterandoTamanhoJanela(w,h):
    global x1,y1, win, view_w, view_h, wo, ho

    glViewport(0,0,w,h)
    view_w = w
    view_h = h
    wo = w
    ho = h
    print(w,h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    if (w <= h):
        view_h = 4.0*h/w
        view_w = 2.0
    else:
        view_w = 4.0*h/w
        view_h = 2.0
        
    gluOrtho2D(0.0, view_w, 0.0, view_h)

def GerenciaTeclado(key, x, y):
    global x1, y1, win, view_w, view_h,wo,ho
    if(key==b'R' or key ==b'r'):
        glColor3f(1.0, 0.0, 0.0)
    elif (key==b'G' or key ==b'g'):
        glColor3f(0.0, 1.0, 0.0)
    elif (key==b'B' or key ==b'b'):
        glColor3f(0.0, 0.0, 1.0)
    print (key)
    glutPostRedisplay()
           
# Função callback chamada para gerenciar eventos do mouse
def GerenciaMouse(button, state, x, y):
    global x1, y1, win, view_w, view_h
    if (button == GLUT_LEFT_BUTTON):
         if (state == GLUT_DOWN):
                  # Troca o tamanho do retângulo, que vai do centro da 
                  # janela até a posição onde o usuário clicou com o mouse
                  escalax=view_w/wo
                  x1 = x*escalax
                  escalay=view_h/ho
                  y1 = (ho-y)*escalay
    glutPostRedisplay()

#// Função callback chamada para gerenciar eventos do teclado   
#// para teclas especiais, tais como F1, PgDn e Home

def TeclasEspeciais(key, x, y):
    global x1, y1, win, view_w, view_h
    if(key == GLUT_KEY_UP):
        y1=y1+0.1
        if (y1+0.3>view_h):
            y1=view_h-0.3
            
    if(key == GLUT_KEY_DOWN):
        y1=y1-0.2
        if (y1-0.3<0):
            y1=0.3
            
    if(key == GLUT_KEY_LEFT):
        x1=x1-0.1
        if (x1-0.4<0):
            x1=0.4
            
    if(key == GLUT_KEY_RIGHT):
        x1=x1+0.1
        if (x1+0.4>view_w):
            x1=view_w-0.4

    glutPostRedisplay()

#// Programa Principal 
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500,350)
    glutInitWindowPosition(10,10)
    glutCreateWindow(b"Interacao")
    glutDisplayFunc(Desenha)
    glutReshapeFunc(AlterandoTamanhoJanela)
    glutKeyboardFunc(GerenciaTeclado)
    glutMouseFunc(GerenciaMouse)
    glutSpecialFunc(TeclasEspeciais)
    Inicializa()
    glutMainLoop()

main()

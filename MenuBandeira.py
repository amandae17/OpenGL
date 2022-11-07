from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
global windowWidth,windowHeight,x1,y1,win,view_w, view_h,texto,r,g,b,r1,g1,b1,r2,g2,b2,r3,g3,b3,r4,g4,b4,teclasHabilitadas
teclasHabilitadas = False
x1 = 0
y1 = 0 


def inicializa():
    global win,texto,r,g,b,r1,g1,b1,r2,g2,b2,r3,g3,b3,r4,g4,b4
    glClearColor(0,0,0,1)
    win = 200
    r = 1.0; g = 1.0; b = 1.0;
    r1 = 1.0; g1 = 1.0; b1 = 1.0;
    r2 = 0.8; g2 = 0.0; b2 = 0.0;
    r3 = 0.0; g3 = 0.0; b3 = 0.0;
    r4 = 0.0; g4 = 0.0; b4 = 0.6;
    texto = '(0,0)'

def alteraTamanhoJanela(w,h):
    global windowWidth,windowHeight,x1,y1,view_w,view_h
    if(h == 0): h=1
    glViewport(0,0,w,h)
    view_w = w
    view_h = h
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if(w <= h):
      windowHeight = 4.0*h/w
      windowWidth = 4.0
    else:
      windowWidth = 4.0*w/h
      windowHeight = 4.0
    
    #gluOrtho2D(0,windowWidth,windowHeight,0)
    gluOrtho2D (-win, win, win, -win)
     
def GerenciaMouse(button, state, x, y):
    if (button == GLUT_RIGHT_BUTTON):
        if (state == GLUT_DOWN):  CriaMenu()
    glutPostRedisplay()

def MoveMouseBotaoPressionado(x,y):
    global texto
#    texto= "Botao pressionado ("+str(x)+","+str(y)+")"
    texto= "Botao pressionado ({0:d},{1:d})".format(x,y)
    glutPostRedisplay()

def MoveMouse(x, y):
    global texto
    texto = "("+str(x)+","+str(y)+")"
    glutPostRedisplay();    

def desenhaTexto(string):
    glPushMatrix()
    # Posição no universo onde o texto será colocado
    glRasterPos2f(-win,win-(win*0.18))
    # Exibe caracter a caracter

    for char in string:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24,ord(char))
        #glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_10,string)
    glPopMatrix()
    
def desenhaBandeira():
    global windowWidth,windowHeight,x1,y1,win, view_w, view_h,texto,r,g,b,r1,g1,b1,r2,g2,b2,r3,g3,b3,r4,g4,b4
  
  # Desenha Poligono branco
    
    glBegin(GL_POLYGON)
    glColor3f(r1,g1,b1)
    glVertex2f(-30+x1, 30+y1)
    glVertex2f(-30+x1, -30+y1)
    glVertex2f(40+x1, -30+y1)
    glVertex2f(40+x1,30+y1)
    glEnd()
    
#Define cor da estrela
    glColor3f(r, g, b)

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

# Desenha Triangulo Vermelho de cima

    glBegin(GL_TRIANGLES)
    glColor3f(r2, g2, b2)
    glVertex2f(-20+x1, 30+y1)
    glVertex2f(40+x1, 30+y1)
    glVertex2f(40+x1, -10+y1)
    glEnd()



# Desenha Triangulo Vermelho de baixo
    glBegin(GL_TRIANGLES)
    glVertex2f(-30+x1, 0.0+y1)
    glVertex2f(-30+x1, -30+y1)
    glVertex2f(20+x1, -30+y1)
    glEnd()
    
def desenha():#Função callback chamada para fazer o desenho
    
  global windowWidth,windowHeight,x1,y1,win, view_w, view_h,texto
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  glClear(GL_COLOR_BUFFER_BIT) #Limpa imagem 

  desenhaBandeira()

  glColor3f(1.0,1.0,1.0)
  desenhaTexto(texto)
 
  
  glutSwapBuffers()    

#// Função callback chamada para gerenciar eventos do teclado   
#// para teclas especiais, tais como F1, PgDn e Home
def TeclasEspeciais(key, x, y):
    global win,teclasHabilitadas

    if(teclasHabilitadas):
        if(key == GLUT_KEY_UP):
               win -= 10
               if (win < 10): win = 10
               glMatrixMode(GL_PROJECTION); glLoadIdentity()

               gluOrtho2D (-win, win, win, -win)
               #gluOrtho2D(0,windowWidth,windowHeight,0)

        if(key == GLUT_KEY_DOWN):
               win += 10
               if (win > 500): win = 500;

               glMatrixMode(GL_PROJECTION);    glLoadIdentity()
               gluOrtho2D (-win, win, win, -win)
               #gluOrtho2D(0,windowWidth,windowHeight,0)
           
    glutPostRedisplay()


# Gerenciamento do menu com as opções de cores           

def MenuPoligonoBranco(op):
    global r1,g1,b1
    if(op==0): r1 = 1.0; g1 = 1.0; b1 = 1.0;
    elif(op==1): r1 = 0.0; g1 = 1.0; b1 = 0.0;
    elif(op==2): r1 = 0.0; g1 = 0.0; b1 = 1.0;
    glutPostRedisplay();
    return 0;

def MenuEstrela(op):
    global r,g,b
    if(op==0): r = 0.0; g = 0.0; b = 1.0;
    elif(op==1): r = 0.0; g = 1.0; b = 0.0;
    elif(op==2): r = 1.0; g = 0.0; b = 0.0;
    glutPostRedisplay();
    return 0;


def MenuTriangulosVermelhos(op):
    global r2,g2,b2
    if(op==0): r2 = 1.0; g2 = 0.0; b2 = 0.0;
    elif(op==1): r2 = 0.0; g2 = 1.0; b2 = 0.0;
    elif(op==2): r2 = 0.0; g2 = 0.0; b2 = 1.0;
    glutPostRedisplay();
    return 0;

def MenuQuadrado(op):
    global r4,g4,b4
    if(op==0): r4 = 0.0; g4 = 0.0; b4 = 0.6;
    elif(op==1): r4 = 0.0; g4 = 1.0; b4 = 0.0;
    elif(op==2): r4 = 1.0; g4 = 0.0; b4 = 0.0;
    glutPostRedisplay();
    return 0;

def redimensionar(op):
    global teclasHabilitadas
    if(op==0): teclasHabilitadas = True
    elif(op==1): teclasHabilitadas = False    
    glutPostRedisplay();
    return 0;

def MenuPrincipal(op):
    return 0

def CriaMenu():
    # Criação do Menu


    submenu1 = glutCreateMenu(MenuEstrela)
    glutAddMenuEntry("Azul",0)
    glutAddMenuEntry("Verde",1)
    glutAddMenuEntry("Vermelho",2)

    submenu2 = glutCreateMenu(MenuPoligonoBranco)
    glutAddMenuEntry("Branco",0)
    glutAddMenuEntry("Verde",1)
    glutAddMenuEntry("Azul",2)

    submenu3 = glutCreateMenu(MenuTriangulosVermelhos)
    glutAddMenuEntry("Vermelho",0)
    glutAddMenuEntry("Verde",1)
    glutAddMenuEntry("Azul",2)


    submenu5 = glutCreateMenu(MenuQuadrado)
    glutAddMenuEntry("Azul",0)
    glutAddMenuEntry("Verde",1)
    glutAddMenuEntry("Vermelho",2)

    submenu6 = glutCreateMenu(redimensionar)
    glutAddMenuEntry("Habilitar",0)
    glutAddMenuEntry("Desabilitar",1)
    

    menu = glutCreateMenu(MenuPrincipal)
    glutAddSubMenu("Estrela",submenu1)
    glutAddSubMenu("Poligono de Fundo",submenu2)
    glutAddSubMenu("Triangulos",submenu3)
    glutAddSubMenu("Redimencionar",submenu6)
    glutAttachMenu(GLUT_RIGHT_BUTTON)
    return 0    


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(400,450)
    glutInitWindowPosition(0,0)
    glutCreateWindow(b'Bandeira')
    glutDisplayFunc(desenha)
    glutReshapeFunc(alteraTamanhoJanela)
    glutMotionFunc(MoveMouseBotaoPressionado)
    glutPassiveMotionFunc(MoveMouse)
    glutMouseFunc(GerenciaMouse)
    glutSpecialFunc(TeclasEspeciais)    
    inicializa()
    glutMainLoop()

    
main()
  

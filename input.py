import pygame as pg #Библиотека

#Иницилизация шрифтов и библиотеки
pg.init()
pg.font.init()
my_font = pg.font.SysFont('Comic Sans MS', 40)

#Создание окна и счетчика кадров
window = pg.display.set_mode((600,600))
clock = pg.time.Clock()

#Класс спрайта
class GameSprite(pg.sprite.Sprite):
    def __init__(self,png,sx,sy,x,y,txt,color):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(pg.image.load(png),(sx,sy))
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.txt = txt
        self.color = color
        self.text = my_font.render(txt, False, self.color)
        
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
        self.text = my_font.render(self.txt, False, self.color)
        window.blit(self.text,(self.rect.x+40,self.rect.y+15))

    def update(self):
        global pb
        match pb:
            case True:
                self.txt = 'X'
                p1.color = 'BLACK'
                p2.color = 'ORANGE'
                pb = False
            case False:
                self.txt = '0'
                p1.color = 'BLUE'
                p2.color = 'BLACK'
                pb = True


#Пустое поле
field = [['-','-','-'],
         ['-','-','-'],
         ['-','-','-']
        ]

#Случаи для побед
p1_w = ['X','X','X']
p2_w = ['0','0','0']

#pb - игроки, если true - ходит крестик, если false - нолик.
pb = True
#running - идет игра или нет.
running  = True
#Проверка победы
#win = False

#Транспонирование матрицы (для удобства работы со столбцами)
def transponent(a):
    new = [[0,0,0],[0,0,0],[0,0,0]]
    for row in range(len(a)):
        for column in range(len(a[0])):
            new[column][row] = a[row][column]
    return new

#Объекты - Клетки
c00 = GameSprite('cell.png',100,100,100,100,field[0][0],(0,0,0))
c01 = GameSprite('cell.png',100,100,250,100,field[0][1],(0,0,0))
c02 = GameSprite('cell.png',100,100,400,100,field[0][2],(0,0,0))

c10 = GameSprite('cell.png',100,100,100,250,field[1][0],(0,0,0))
c11 = GameSprite('cell.png',100,100,250,250,field[1][1],(0,0,0))
c12 = GameSprite('cell.png',100,100,400,250,field[1][2],(0,0,0))

c20 = GameSprite('cell.png',100,100,100,400,field[2][0],(0,0,0))
c21 = GameSprite('cell.png',100,100,250,400,field[2][1],(0,0,0))
c22 = GameSprite('cell.png',100,100,400,400,field[2][2],(0,0,0))

#Тексты
p1 = GameSprite('cell.png',1,1,0,0,'P1 X','BLUE')
p2 = GameSprite('cell.png',1,1,440,0,'P2 0','BLACK')
info = GameSprite('cell.png',1,1,90,500,'R - Начать сначала.','CYAN')

#Случаи побед
p1vic = my_font.render('Победил игрок 1!',True,'BLUE')
p2vic = my_font.render('Победил игрок 2!',True,'ORANGE')
null = my_font.render('Ничья!',True,'GREEN')

#Списки с объектами для рендера/проверок
cells = [c00,c01,c02,c10,c11,c12,c20,c21,c22]
texts = [p1,p2,info]

#Игровое поле/матрица с текстами клеток.
field_s = [[c00.txt,c01.txt,c02.txt],
           [c10.txt,c11.txt,c12.txt],
           [c20.txt,c21.txt,c22.txt]
          ]

#Поле, но перевернутое (столбцы на месте строк)
field_t = transponent(field_s)

#Диагонали
field_diag1 = [c00.txt,c11.txt,c22.txt]
field_diag2 = [c02.txt,c11.txt,c20.txt]

#Игровой цикл2
while running:
    #Проверка событий
    for event in pg.event.get():  
        match event.type:
            case pg.QUIT:
                running = False
            case pg.MOUSEBUTTONUP:                
                pos = pg.mouse.get_pos()
                for cell in cells:
                    #Если произошел клик по клетке, то обновить её и все доступные списки с именами.
                    pos = pg.mouse.get_pos()
                    if cell.rect.collidepoint(pos):
                        cell.update()
                                                
                        field_s = [[c00.txt,c01.txt,c02.txt],
                                   [c10.txt,c11.txt,c12.txt],
                                   [c20.txt,c21.txt,c22.txt]
                                  ]

                        field_t = transponent(field_s)

                        field_diag1 = [c00.txt,c11.txt,c22.txt]
                        field_diag2 = [c02.txt,c11.txt,c20.txt]
            #Рестарт          
            case pg.KEYDOWN:
                match event.key:
                    case K_r:
                        pass
    #Если не победа - проверять условия
    #if win != True:
    window.fill('WHITE')
        
    #Рендер клеток и текста        
    for cell in cells:
        cell.reset()
    
    for text in texts:
        text.reset()

    #Обновление экрана
    pg.display.update()
    clock.tick(60)
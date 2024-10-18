#Случаи для побед
p1_w = ['X','X','X']
p2_w = ['0','0','0']

#Проверка победы
win = False

#Тексты для побед
p1vic = my_font.render('Победил игрок 1!',True,'BLUE')
p2vic = my_font.render('Победил игрок 2!',True,'ORANGE')

if win != True:
    window.fill('WHITE')
    #Питон скотина, не позволил по нормальному реализовать условия, по другому не читает задуманное :/"
    if field_s[0] == p1_w or field_s[1] == p1_w or field_s[2] == p1_w or field_t[0] == p1_w or field_t[1] == p1_w or field_t[2] == p1_w or field_diag1 == p1_w or field_diag2 == p1_w:
        window.blit(p1vic,(125,0))
        win = True
    elif field_s[0] == p2_w or field_s[1] == p2_w or field_s[2] == p2_w or field_t[0] == p2_w or field_t[1] == p2_w or field_t[2] == p2_w or field_diag1 == p2_w or field_diag2 == p2_w:
    
        window.blit(p2vic,(125,0))
        win = True
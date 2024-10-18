def update(self):
        global pb
        if self.txt == '-':
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

        else:
            pass
class A():
    @staticmethod
    def pattern():
        letter='A'
        j=6
        k=1
        print(" "*7+letter*6)
        for i in range(6):
            
            if i==2 or i==3:
                print(" "*j+letter*((k*2)+6))
            else:
                print(" "*j+letter*3+" "*(k*2)+letter*3)
            j-=1
            k+=1
#A.pattern()

class B():
    @staticmethod
    def pattern():
        letter='B'
        for i in range(7):
            if i%3==0:
                print(letter*9)
            else:
                print(letter*3 + " "*6+letter)
#B.pattern()

class C():
    @staticmethod
    def pattern():
        l=['   CCCCCC',' CCC     CC','CCC']
        for i in l:
            print(i)
        print('CCC')
        for i in l[::-1]:
            print(i)    
#C.pattern()

class D():
    @staticmethod
    def pattern():
        l=['DDDDDDDDDD','DDD      DD','DDD       DD']
        for i in l:
            print(i)
        print('DDD       DD')
        for i in l[::-1]:
            print(i)
#D.pattern()

class E():
    @staticmethod
    def pattern():
        for i in range(7):
            if i%3==0:
                print('E'*12)
            else:
                print('E'*3)
#E.pattern()

class F():
    @staticmethod
    def pattern():
        for i in range(7):
            if i==3 or i==0:
                print('F'*12)
            else:
                print('F'*3)
#F.pattern()

class G():
    @staticmethod
    def pattern():
        l=['   GGGGGG',' GGG     GG','GGG']
        for i in l:
            print(i)
        print('GGG')
        l2=['   GGGGGGG GG',' GGG    GG GG','GGG     GGGGG']
        for i in l2[::-1]:
            print(i)
    
        #pass
#G.pattern()

class H():
    @staticmethod
    def pattern():
        for i in range(7):
            if i==7//2:
                print('HHHHHHHHHHHHHHH')
            else:
                print('HHH         HHH')
#H.pattern()

class I():
    @staticmethod
    def pattern():
        for i in range(7):
            if i%6==0:
                print('IIIIIIIIIIIIIII')
            else:
                print('      III      ')
#I.pattern()

class J():
    @staticmethod
    def pattern():
        print('JJJJJJJJJJJJJJ')
        print('        JJJ      ')
        print('        JJJ      ')
        print('        JJJ      ')
        print('        JJJ      ')
        print(' JJJ    JJ      ')
        print('   JJJJJ      ')
#J.pattern()

class K():
    @staticmethod
    def pattern():
        for i in range(3,-4,-1):
            print('K'*3+" "*(abs(i)*2)+'KK')
#K.pattern()

class L():
    @staticmethod
    def pattern():
        for i in range(6):
            print('LLL')
        print('LLLLLLLLLLLLLLL')
#L.pattern()

class M():
    @staticmethod
    def pattern():
        j=6
        print('MMMM          MMMM')
        for i in range(6):
            if i<=3: 
                print('MMM'+" "*i+'MMM'+" "*j+'MMM'+" "*i+'MMM')
                j-=2
            else:
                print('MMM            MMM')
#M.pattern()

class N():
    @staticmethod
    def pattern():
        j=8
        print('NNNN          NNN')
        for i in range(5):
            print('NNN'+' '*i*2+'NNN'+' '*j+'NNN')
            j-=2
        print('NNN          NNNN')
#N.pattern()

class O():
    @staticmethod
    def pattern():
        l=['     OOOOOOO','  OOO       OOO','OOO           OOO']
        for i in l:
            print(i)
        print('OOO           OOO')
        for i in l[::-1]:
            print(i)
#O.pattern()

class P():
    @staticmethod
    def pattern():
        letter='P'
        for i in range(4):
            if i%3==0:
                print(letter*9)
            else:
                print(letter*3 + " "*6+letter)
        for i in range(3):
            print("PPP")
#P.pattern()

class Q():
    @staticmethod
    def pattern():
        l=['     QQQQQQQ','  QQQ       QQQ','QQQ           QQQ','QQQ           QQQ']
        for i in l:
            print(i)
        l2=['     QQQQQQQ   QQ','  QQQ        QQ','QQQ        QQ QQQ']
        for i in l2[::-1]:
            print(i)
#Q.pattern()

class R():
    @staticmethod
    def pattern():
        letter='R'
        for i in range(4):
            if i%3==0:
                print(letter*9)
            else:
                print(letter*3 + " "*6+letter)
        for i in range(-1,-4,-1):
            print('R'*3+" "*(abs(i)*2)+'RR')
#R.pattern()

class S():
    @staticmethod
    def pattern():
        l=['   SSSSSS',' SSS     SS','  SSS','    SSSS','       SSS',' SS     SSS','   SSSSSS']
        for i in l:
            print(i)
#S.pattern()

class T():
    @staticmethod
    def pattern():
        for i in range(7):
            if i==0:
                print('TTTTTTTTTTTTTTT')
            else:
                print('      TTT      ')
#T.pattern()

class U():
    @staticmethod
    def pattern():
        l=['    UUUUUUUUU','  UU         UU','UUU           UUU']
        for _ in range(4):
            print(l[-1])
        for i in l[::-1]:
            print(i)
#U.pattern()

class V():
    @staticmethod
    def pattern():
        pass
#.pattern()

class W():
    @staticmethod
    def pattern():
        pass
#.pattern()

class X():
    @staticmethod
    def pattern():
        pass
#.pattern()

class Y():
    @staticmethod
    def pattern():
        pass
#.pattern()

class Z():
    @staticmethod
    def pattern():
        pass
#.pattern()

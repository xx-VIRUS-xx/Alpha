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
        pass
#.pattern()

class N():
    @staticmethod
    def pattern():
        pass
#.pattern()

class O():
    @staticmethod
    def pattern():
        pass
#.pattern()

class P():
    @staticmethod
    def pattern():
        pass
#.pattern()


class Q():
    @staticmethod
    def pattern():
        pass
#.pattern()


class R():
    @staticmethod
    def pattern():
        pass
#.pattern()

class S():
    @staticmethod
    def pattern():
        pass
#.pattern()

class T():
    @staticmethod
    def pattern():
        pass
#.pattern()
class U():
    @staticmethod
    def pattern():
        pass
#.pattern()

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
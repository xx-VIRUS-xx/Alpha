class A():
    @staticmethod
    def pattern():
        res=[]
        letter='A'
        j=6
        k=1
        res.append(" "*7+letter*6)
        for i in range(6):
            
            if i==2 or i==3:
                res.append(" "*j+letter*((k*2)+6))
            else:
                res.append(" "*j+letter*3+" "*(k*2)+letter*3)
            j-=1
            k+=1
        return res
#A.pattern()

class B():
    @staticmethod
    def pattern():
        res=[]
        letter='B'
        for i in range(7):
            if i%3==0:
                res.append(letter*9)
            else:
                res.append(letter*3 + " "*6+letter)
        return res
#B.pattern()

class C():
    @staticmethod
    def pattern():
        res=[]
        l=['   CCCCCC',' CCC     CC','CCC']
        for i in l:
            res.append(i)
        res.append('CCC')
        for i in l[::-1]:
            res.append(i)
        return res    
#C.pattern()

class D():
    @staticmethod
    def pattern():
        res=[]
        l=['DDDDDDDDDD','DDD      DD','DDD       DD']
        for i in l:
            res.append(i)
        res.append('DDD       DD')
        for i in l[::-1]:
            res.append(i)
        return res
#D.pattern()

class E():
    @staticmethod
    def pattern():
        res=[]
        for i in range(7):
            if i%3==0:
                res.append('E'*12)
            else:
                res.append('E'*3)
        return res
#E.pattern()

class F():
    @staticmethod
    def pattern():
        res=[]
        for i in range(7):
            if i==3 or i==0:
                res.append('F'*12)
            else:
                res.append('F'*3)
        return res
#F.pattern()

class G():
    @staticmethod
    def pattern():
        res=[]
        l=['   GGGGGG',' GGG     GG','GGG']
        for i in l:
            res.append(i)
        res.append('GGG')
        l2=['   GGGGGGG GG',' GGG    GG GG','GGG     GGGGG']
        for i in l2[::-1]:
            res.append(i)
        return res
        #pass
#G.pattern()

class H():
    @staticmethod
    def pattern():
        res=[]
        for i in range(7):
            if i==7//2:
                res.append('HHHHHHHHHHHHHHH')
            else:
                res.append('HHH         HHH')
        return res
#H.pattern()

class I():
    @staticmethod
    def pattern():
        res=[]
        for i in range(7):
            if i%6==0:
                res.append('IIIIIIIIIIIIIII')
            else:
                res.append('      III      ')
        return res
#I.pattern()

class J():
    @staticmethod
    def pattern():
        res=[]
        res.append('JJJJJJJJJJJJJJ')
        res.append('        JJJ      ')
        res.append('        JJJ      ')
        res.append('        JJJ      ')
        res.append('        JJJ      ')
        res.append(' JJJ    JJ      ')
        res.append('   JJJJJ      ')
        return res
#J.pattern()

class K():
    @staticmethod
    def pattern():
        res=[]
        for i in range(3,-4,-1):
            res.append('K'*3+" "*(abs(i)*2)+'KK')
        return res
#K.pattern()

class L():
    @staticmethod
    def pattern():
        res=[]
        for i in range(6):
            res.append('LLL')
        res.append('LLLLLLLLLLLLLLL')
        return res
#L.pattern()

class M():
    @staticmethod
    def pattern():
        res=[]
        j=6
        res.append('MMMMM        MMMMM')
        for i in range(6):
            if i<=3: 
                res.append('MMM'+" "*i+'MMM'+" "*j+'MMM'+" "*i+'MMM')
                j-=2
            else:
                res.append('MMM            MMM')
        return res
#M.pattern()

class N():
    @staticmethod
    def pattern():
        res=[]
        j=8
        res.append('NNNN          NNN')
        for i in range(5):
            res.append('NNN'+' '*i*2+'NNN'+' '*j+'NNN')
            j-=2
        res.append('NNN          NNNN')
        return res
#N.pattern()

class O():
    @staticmethod
    def pattern():
        res=[]
        l=['     OOOOOOO','  OOO       OOO','OOO           OOO']
        for i in l:
            res.append(i)
        res.append('OOO           OOO')
        for i in l[::-1]:
            res.append(i)
        return res
#O.pattern()

class P():
    @staticmethod
    def pattern():
        res=[]
        letter='P'
        for i in range(4):
            if i%3==0:
                res.append(letter*9)
            else:
                res.append(letter*3 + " "*6+letter)
        for i in range(3):
            res.append("PPP")
        return res
#P.pattern()

class Q():
    @staticmethod
    def pattern():
        res=[]
        l=['     QQQQQQQ','  QQQ       QQQ','QQQ           QQQ','QQQ           QQQ']
        for i in l:
            res.append(i)
        l2=['     QQQQQQQ   QQ','  QQQ        QQ','QQQ        QQ QQQ']
        for i in l2[::-1]:
            res.append(i)
        return res
#Q.pattern()

class R():
    @staticmethod
    def pattern():
        res=[]
        letter='R'
        for i in range(4):
            if i%3==0:
                res.append(letter*9)
            else:
                res.append(letter*3 + " "*6+letter)
        for i in range(-1,-4,-1):
            res.append('R'*3+" "*(abs(i)*2)+'RR')
        return res
#R.pattern()

class S():
    @staticmethod
    def pattern():
        res=[]
        l=['   SSSSSS',' SSS     SS','  SSS','    SSSS','       SSS',' SS     SSS','   SSSSSS']
        for i in l:
            res.append(i)
        return res
#S.pattern()

class T():
    @staticmethod
    def pattern():
        res=[]
        for i in range(7):
            if i==0:
                res.append('TTTTTTTTTTTTTTT')
            else:
                res.append('      TTT      ')
            return res
#T.pattern()

class U():
    @staticmethod
    def pattern():
        res=[]
        l=['    UUUUUUUUU','  UU         UU','UUU           UUU']
        for _ in range(4):
            res.append(l[-1])
        for i in l[::-1]:
            res.append(i)
        return res
#U.pattern()

class V():
    @staticmethod
    def pattern():
        res=[]
        letter='V'
        j=1
        k=6
        for i in range(7):
            res.append(" "*j+letter*3+" "*(k*2)+letter*3)
            j+=1
            k-=1
        return res
#V.pattern()

class W():
    @staticmethod
    def pattern():
        res=[]
        j=0

        for i in range(6):
            if i>=2: 
                res.append('WWW'+" "*(5-i)+'WWW'+" "*j+'WWW'+" "*(5-i)+'WWW')
                j+=2
            else:
                res.append('WWW            WWW')
        res.append('WWWWW        WWWWW')
        return res
#W.pattern()

class X():
    @staticmethod
    def pattern():
        res=[]
        j=6
        k=2
        for i in range(3):
            res.append(" "*i+'XXX'+" "*j+'XXX')
            j-=2
        res.append(' '*4+'X'*4)
        for i in range(3):
            res.append(" "*(2-i)+'XXX'+" "*k+'XXX')
            k+=2
        return res
#X.pattern()

class Y():
    @staticmethod
    def pattern():
        res=[]
        j=11
        for i in range(3):
            res.append(" "*(2*i)+'YYY'+" "*j+'YYY')
            j-=4
        res.append(' '*6+'Y'*5)
        for i in range(3):
            res.append(' '*7+'Y'*3)
        return res
#Y.pattern()

class Z():
    @staticmethod
    def pattern():
        res=[]
        res.append('Z'*15)
        j=12
        for i in range(5):
            res.append(' '*j+'ZZZ')
            j-=3
        res.append('Z'*15)
        return res
#Z.pattern()

Alpha_Dict={'A': A,'B': B,'C': C,'D': D,
            'E': E,'F': F ,'G': G ,'H': H ,
            'I': I ,'J': J ,'K': K ,'L': L ,
            'M': M ,'N': N ,'O': O ,'P': P ,
            'Q': Q ,'R': R ,'S': S ,'T': T ,
            'U': U ,'V': V ,'W': W ,'X': X ,
            'Y': Y ,'Z': Z,
            'a': A,'b': B,'c': C,'d': D,
            'e': E,'f': F ,'g': G ,'h': H ,
            'i': I ,'j': J ,'k': K ,'l': L ,
            'm': M ,'n': N ,'o': O ,'p': P ,
            'q': Q ,'r': R ,'s': S ,'t': T ,
            'u': U ,'v': V ,'w': W ,'x': X ,
            'y': Y ,'z': Z  }

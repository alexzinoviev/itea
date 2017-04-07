# class A: pass
#
# class B(A): pass
#
# class C(A): pass
#
# class D(C): pass
#
# class E(C): pass
#
# class F(B, D): pass
#
# class G(D, E): pass
#
# class H(F, G): pass
#
#
# H.mro()
# print(H.mro())

# #-------------------------------
#
#
#
# class A: pass
#
# class B(A): pass
#
# #class C(A, B): pass
#
# class C(B,A): pass
#
#
#
# C.mro()
# print(C.mro())
#
# ------------------


class A:
    def __init__(self):
        print('A')
        super().__init__()


class B:
    def __init__(self):
        print('B')
        super().__init__()


class C(A,B):
    def __init__(self):
        print('C')
        super().__init__() # работает по mro


c = C()
print(c)
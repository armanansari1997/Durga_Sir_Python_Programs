class A: pass
class B: pass
class C: pass
class D(A, B): pass
class E(B, C):pass
class F(D, E, C): pass


print(A.mro())  # AO
print(B.mro())  # BO
print(C.mro())  # CO
print(D.mro())  # DABO
print(E.mro())  # EBCO
print(F.mro())  # FDAEBCO


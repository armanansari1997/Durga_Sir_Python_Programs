class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass


print(A.mro())  # AO
print(B.mro())  # BAO
print(C.mro())  # CAO
print(D.mro())  # DBCAO


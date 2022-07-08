#EXAMEN FINAL RESUELTO

# 1 ¿Cual es el resultado de ejecutra el siguiente bloque de codigo?
#def foo (x,y=1):
#    return x*y
#print(foo(foo(3,2) + foo(3)))
# Rpta. a)9

#2 Conocida la funcion foo, indique que sentencia produciria un error:
#def foo(*args):
#    return sum(args)
#foo(1,2,3,4,5)
#Rpta. b)foo([1,2,3,4,5])

#3 Indique la complejidad del siguiente algoritmo
#SUMA_DE_MATRICES(A,B):
#    m = filas(A)
#    n = columnas(A)
#    S = CrearMatrizDeCeros(m,n)
#    for i in f0,1,...,m-1g
#        for j in f0,1,...,n-1g
#            S[i,j] = A[i,j] + B[i,j]
#return S
#Rpta. c) O(n*m)

#4 ¿Que linea cambiaria del algoritmo INSERTION_SORT para ordenar una secuencia de
# numeros de mayor a menor?

#from mimetypes import init
#from re import A

#INSERTION_SORT(A)
#    for j in {1,2,...,length(A)-1}
#        key= A[j]
#        i=j-1
#        while i>=0 and key<A[i]
#            A[i+1]=A[i]
#            i = i - 1
#        A[i + 1] = key
#return A
#Rpta. c) Linea 4: while i > 0 and key > A[i]

#5 EL siguiente algoritmo invierte el orden de una lista. Encuentre el invariante de
#bucle, e indique el porque de su respuesta

#Linea 6-7-8-9 Ya que esto se mantiene en el porceoso de inicializacion, mantenimiento
#que es cuando se ejecuta el bucle y terminacion despues del bucle

#6¿Cual es el resultado de ejecutar el siguiente bloque de codigo?
#class Foo:
#    def __init__(self,x,y):
#        self.x = x
#        self.y = y
#        self.suma = self.x + self.y
#
#foo = Foo(3,4)
#foo.x = 4
#print(foo.suma)
#Rpta. c)7

#7.¿Cual es el resultado de ejecutar el siguiente bloque de codigo?
class Foo:
    def init (self):
        self.y = 1

class Suma(Foo):
    def __init__(self,y):
        self.y = y
        super(). init ()
    def sumar(self, x):
        return x + self.y

obj = Suma(2)
print(obj.sumar(3))

#Rpta. b) 4
